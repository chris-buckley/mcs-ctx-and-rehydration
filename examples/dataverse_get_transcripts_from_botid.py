import logging
import os
from typing import Any, Dict, List, Optional

import msal
from dotenv import load_dotenv
import httpx
from pydantic import BaseModel, Field, ValidationError # Import BaseModel and Field for Pydantic v2

from utilities.custom_rich_logger import setup_logger 
logger: logging.Logger = setup_logger(logger_name="dataverse_client")
from models.dataverse_conversation_transcript import ConversationTranscript


class DataverseEnv(BaseModel):
    """
    A Pydantic BaseModel to hold validated Dataverse environment variables.
    Using model_config = {'frozen': True} makes instances immutable, similar to dataclasses(frozen=True).
    """
    model_config = {'frozen': True} # For Pydantic v2, makes the instance immutable

    client_id: str
    tenant_id: str
    client_secret: str
    web_api_endpoint: str  # Base URL, without trailing slash
    dataverse_endpoint_with_api_version: str # Derived URL for API calls


def load_dataverse_environment_variables() -> DataverseEnv:
    """
    Loads environment variables from .env file and validates them.
    Exits if any required environment variables are missing.
    """
    load_dotenv() # Load variables from .env file

    # Retrieve values directly from os.getenv
    # We still perform initial checks for None to provide user-friendly messages
    # before Pydantic's ValidationError, which might be less clear for missing env vars.
    client_id_val: Optional[str] = os.getenv(key="CLIENT_ID")
    tenant_id_val: Optional[str] = os.getenv(key="TENANT_ID")
    client_secret_val: Optional[str] = os.getenv(key="CLIENT_SECRET")
    # Ensure WEB_API_ENDPOINT does not have a trailing slash for consistent URL construction
    web_api_endpoint_val: Optional[str] = os.getenv(key="WEB_API_ENDPOINT", default="").rstrip("/")

    # Check for missing variables and exit early
    missing: list = []
    if not client_id_val: missing.append("CLIENT_ID")
    if not tenant_id_val: missing.append("TENANT_ID")
    if not client_secret_val: missing.append("CLIENT_SECRET")
    if not web_api_endpoint_val: missing.append("WEB_API_ENDPOINT")

    if missing:
        logger.error(msg="Missing required environment variables. Please check your .env file.")
        logger.error(msg=f"Missing variables: {', '.join(missing)}")
        exit(code=1) # Exit if critical variables are not set

    # At this point, we are guaranteed that these are strings, not None
    # Derive the full Dataverse API endpoint with version
    dataverse_endpoint_with_api_version_val: str = f"{web_api_endpoint_val}/api/data/v9.2"

    logger.info("Environment variables loaded and validated successfully.")
    
    # Instantiate Pydantic model with the validated values
    # Pydantic will perform further type validation if necessary,
    # though here all are strings coming from os.getenv.
    try:
        env_vars = DataverseEnv(
            client_id=client_id_val,
            tenant_id=tenant_id_val,
            client_secret=client_secret_val,
            web_api_endpoint=web_api_endpoint_val,
            dataverse_endpoint_with_api_version=dataverse_endpoint_with_api_version_val
        )
        return env_vars
    except ValidationError as e:
        logger.error(f"Pydantic validation error for environment variables: {e}")
        exit(code=1)


def get_conversation_id_from_prompt() -> str:
    """Prompts the user to enter the PARTIAL conversation ID."""
    conversation_id = input("Enter the PARTIAL conversation ID (e.g., H4hhfErR4i81dC602xLml2-au): ").strip()
    if not conversation_id:
        logger.error("Conversation ID cannot be empty.")
        exit(1)
    return conversation_id

def get_access_token(env: DataverseEnv) -> str:
    """
    Acquires an access token for Dataverse API using client credentials flow.
    Requires CLIENT_ID, TENANT_ID, CLIENT_SECRET, and WEB_API_ENDPOINT.
    """
    logger.info("Acquiring access token...")
    authority: str = f"https://login.microsoftonline.com/{env.tenant_id}"
    # Scope typically uses the base web API endpoint without the /api/data/v9.2 part
    scope: list[str] = [f"{env.web_api_endpoint}/.default"] 
    app = msal.ConfidentialClientApplication(
        client_id=env.client_id, 
        authority=authority, 
        client_credential=env.client_secret,
    )
    result = app.acquire_token_for_client(scopes=scope)
    if "access_token" in result:
        logger.info("✓ Successfully acquired access token")
        return result["access_token"]
    else:
        error_desc = result.get('error_description', 'Unknown error')
        logger.error(f"Error acquiring token: {result.get('error', 'N/A')} - {error_desc}")
        raise Exception(f"Error acquiring token: {error_desc}")


class DataverseClient:
    """Client for interacting with the Dataverse Web API."""
    def __init__(self, base_url: str, access_token: str, client_timeout: float = 30.0):
        self.base_url = base_url.rstrip("/")
        self.headers = {
            "Authorization": f"Bearer {access_token}", "Accept": "application/json",
            "OData-MaxVersion": "4.0", "OData-Version": "4.0",
            "Content-Type": "application/json; charset=utf-8"
        }
        self.client = httpx.Client(timeout=client_timeout)

    def request(self, endpoint: str, method: str = "GET", data: Optional[Dict[str, Any]] = None, params: Optional[Dict[str, Any]] = None) -> Optional[Dict[str, Any]]:
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        try:
            logger.debug(f"Requesting {method} {url} with params: {params} and data: {data}")
            response = self.client.request(method, url, json=data, params=params, headers=self.headers)
            response.raise_for_status()
            if not response.content or response.status_code == 204: return None
            return response.json()
        except httpx.HTTPStatusError as e:
            logger.error(f"Dataverse API HTTP error: {e.response.status_code} - {e.response.text} for URL: {e.request.url}")
            raise
        except httpx.RequestError as e:
            logger.error(f"Dataverse API Request error: {str(e)} for URL: {e.request.url}")
            raise
        except Exception as e:
            logger.error(f"Unexpected error during Dataverse API request to {url}: {str(e)}")
            raise

    def get_entities(self, entity_name: str, select: Optional[List[str]] = None, filter_query: Optional[str] = None, expand: Optional[str] = None, top: Optional[int] = None, order_by: Optional[str] = None) -> List[Dict[str, Any]]:
        params: Dict[str, Any] = {}
        if select and "*" not in select : 
            params["$select"] = ",".join(list(dict.fromkeys(select))) # Ensure unique fields
        if filter_query: params["$filter"] = filter_query
        if expand: params["$expand"] = expand
        if top is not None: params["$top"] = str(top)
        if order_by: params["$orderby"] = order_by
        
        response_data = self.request(entity_name, params=params)
        return response_data.get("value", []) if response_data else []

    def close(self):
        if hasattr(self, 'client') and self.client:
            self.client.close()
            logger.info("DataverseClient's httpx client closed.")

def get_bot_id_by_name(dv_client: DataverseClient, bot_name: str) -> Optional[str]:
    safe_name = bot_name.replace("'", "''")
    filter_q = f"name eq '{safe_name}'"
    bots = dv_client.get_entities(
        entity_name="bots", select=["botid", "name"], filter_query=filter_q, top=1
    )
    if bots:
      logger.info(f"Bot '{bots[0].get('name')}' found with ID '{bots[0]['botid']}'.")
      return bots[0]["botid"]
    else:
      logger.warning(f"Bot with name '{bot_name}' not found.")
      return None

def list_sample_conversation_transcripts(
    dv_client: DataverseClient,
    count: int = 3,
    select_all_fields: bool = False 
) -> None:
    logger.info(f"Fetching {count} sample conversation transcripts for debugging...")
    
    select_fields_list: Optional[List[str]] = None
    if not select_all_fields:
        # More robust default list, excluding fields that often cause "not found" errors initially.
        select_fields_list = [
            "conversationtranscriptid", "name", "createdon", "modifiedon", 
            "subject", "title", 
            # Add other very common, non-solution-specific fields if known
        ]
        select_fields_list = [f for f in select_fields_list if f] # Filter out any None placeholders

    try:
        transcripts = dv_client.get_entities(
            entity_name="conversationtranscripts",
            select=select_fields_list, 
            top=count,
            order_by="createdon desc"
        )

        if not transcripts:
            logger.info("No conversation transcripts found to sample.")
            return

        logger.info(f"Found {len(transcripts)} sample conversation transcripts. Details:")
        for i, transcript in enumerate(transcripts):
            logger.info(f"--- Sample Transcript {i+1} (GUID: {transcript.get('conversationtranscriptid', 'N/A')}) ---")
            for key, value in transcript.items():
                # Log if value is not None/empty or if it's a key we are often interested in
                if value or key in ["conversationtranscriptid", "name", "subject", "title"]: 
                    logger.info(f"  {key}: {value}")
            logger.info("--------------------------------------------------")
        logger.info("ACTION REQUIRED: Review the logged fields above. Identify which field (e.g., 'name', 'title') CONTAINS the partial ID like '{conversation_id}_{bot_id}'.")
        logger.info("This field name will be your 'filter_field' in 'get_conversation_transcript_by_name'.")
        if not select_all_fields:
            logger.info("If the target field or the composite ID is not visible, try running with `select_all_fields=True` in the call to `list_sample_conversation_transcripts` in the main script.")

    except httpx.HTTPStatusError as e:
        logger.error(f"HTTP error while listing sample transcripts: {e.response.status_code} - {e.response.text}")
        if "Could not find a property named" in e.response.text and not select_all_fields:
            logger.error("One of the fields in the default '$select' list for samples doesn't exist. RETRY by setting `select_all_fields=True` in the main script's call to `list_sample_conversation_transcripts`.")
        elif select_all_fields:
             logger.error("Tried fetching all fields for samples, but still encountered an error. Check Dataverse permissions or entity metadata for 'conversationtranscript'.")
    except Exception as e:
        logger.error(f"Unexpected error listing sample transcripts: {str(e)}", exc_info=True)


def get_conversation_transcript_by_name(
    dv_client: DataverseClient,
    partial_conversation_identifier: str, # Renamed to clarify it's partial
    select_fields_override: Optional[List[str]] = None
) -> Optional[Dict[str, Any]]:
    """
    Get a conversation transcript by checking if its identifier field CONTAINS the partial_conversation_identifier.
    The colleague's comment suggests the format is {conversation_id}_{bot_id} likely in the 'name' field.
    """
    # ----- BEGIN USER MODIFICATION AREA (if needed after debugging) -----
    # Based on colleague's input and common practice, 'name' is the most likely field.
    # Confirm with `list_sample_conversation_transcripts(select_all_fields=True)` output.
    filter_field = "name"  # <<<<< This is likely correct now.
    # ----- END USER MODIFICATION AREA -----
    
    default_select_fields = [
        "conversationtranscriptid", filter_field, 
        "content", "metadata", "schematype", "statuscode", "schemaversion", "createdon"
    ]
    
    current_select_fields = select_fields_override if select_fields_override is not None else default_select_fields
    if filter_field not in current_select_fields:
        current_select_fields.append(filter_field)
    current_select_fields = list(dict.fromkeys(current_select_fields)) # Remove duplicates

    safe_partial_identifier = partial_conversation_identifier.replace("'", "''")
    
    # Use OData 'contains' function as per colleague's advice
    filter_q = f"contains({filter_field}, '{safe_partial_identifier}')"

    logger.info(f"Querying 'conversationtranscripts' with $filter=\"{filter_q}\" and $select=\"{','.join(current_select_fields)}\"")

    transcripts = dv_client.get_entities(
        entity_name="conversationtranscripts",
        select=current_select_fields,
        filter_query=filter_q,
        top=1 # Get the first one that matches. If multiple could match, might need more specific criteria or ordering.
    )

    if transcripts:
        transcript_data = transcripts[0]
        retrieved_guid = transcript_data.get('conversationtranscriptid', 'N/A')
        retrieved_filter_field_value = transcript_data.get(filter_field, 'N/A (Field not found in response)')
        logger.info(f"Found conversation transcript. GUID: {retrieved_guid}, Content of '{filter_field}': {retrieved_filter_field_value}")
        return transcript_data
    else:
        logger.warning(f"No conversation transcript found where '{filter_field}' contains '{partial_conversation_identifier}'")
        return None

def minimal_get_conversation_transcript_by_guid(dv_client: DataverseClient, transcript_guid: str) -> Optional[Dict[str, Any]]:
    if not transcript_guid:
        logger.warning("Transcript GUID is empty, cannot fetch.")
        return None
    endpoint = f"conversationtranscripts({transcript_guid})"
    logger.info(f"Fetching conversation transcript by GUID: {transcript_guid}")
    return dv_client.request(endpoint)

def get_all_transcripts_by_user_id(dv_client: DataverseClient, user_id: str):
    # TODO: Example to retrieve all conversation activities from Dataverse API given a userID
    pass

def get_all_transcripts_by_bot_id(dv_client: DataverseClient, bot_id: str):
    # TODO: Example to retrieve all conversation activities from Dataverse API given a botID
    pass

def get_all_transcripts_by_conversation_id(dv_client: DataverseClient, conversation_id: str):
    # TODO: Example to retrieve all conversation activities from Dataverse API given a conversationID
    pass

def start_conversation_with_given_previous_transcript(dv_client: DataverseClient, previous_conversation_id: str):
    # TODO: # Example to support conversation continuation with full context preservation
    pass


def main():
    """Main function to run the Dataverse client operations."""
    dataverse_client: Optional[DataverseClient] = None
    try:
        # Step 1: Load and validate environment variables using Pydantic
        env_vars: DataverseEnv = load_dataverse_environment_variables()

        # Step 2: Acquire access token using loaded env vars
        dataverse_access_token: str = get_access_token(env_vars)
        
        # Step 3: Initialize DataverseClient using loaded env vars
        dataverse_client = DataverseClient(
            base_url=env_vars.dataverse_endpoint_with_api_version,
            access_token=dataverse_access_token
        )
        logger.info("DataverseClient initialized.")

        # --- Remaining application logic, using the initialized client ---

        list_sample_conversation_transcripts(dv_client=dataverse_client, count=3, select_all_fields=True) 

        logger.info("Fetching list of all bots...")
        bots_list: List[Dict[str, Any]] = dataverse_client.get_entities(
            entity_name="bots",
            select=["botid", "name", "schemaname", "createdon"],
            order_by="name"
        )
        if bots_list:
            logger.info(f"Found {len(bots_list)} bots:")
            for bot in bots_list:
                logger.info(f"  - Name: {bot.get('name', 'N/A')}, ID: {bot.get('botid', 'N/A')}")
        else: logger.info("No bots found.")
        
        target_bot_name = "CBA Assistant" 
        logger.info(f"Attempting to find bot by name: '{target_bot_name}'...")
        bot_id_found = get_bot_id_by_name(dataverse_client, target_bot_name)
        
        partial_conversation_id_from_user = get_conversation_id_from_prompt() 
        
        logger.info(f"Attempting to fetch conversation transcript where a field CONTAINS: '{partial_conversation_id_from_user}'...")
        transcript_by_name = get_conversation_transcript_by_name(
            dv_client=dataverse_client,
            partial_conversation_identifier=partial_conversation_id_from_user
        )

        if transcript_by_name:
            transcript_guid = transcript_by_name.get('conversationtranscriptid', 'N/A')
            full_name_field = transcript_by_name.get("name", "N/A") # Assuming 'name' is the target field
            logger.info(f"Successfully retrieved transcript. GUID: {transcript_guid}. Full value of 'name' field: {full_name_field}")
        else:
            logger.info(f"Could not retrieve transcript containing partial ID '{partial_conversation_id_from_user}'.")

    except httpx.HTTPStatusError as e: 
        logger.error(f"A Dataverse API HTTP error occurred. Check previous logs for details.")
    except Exception as e:
        logger.error(f"An unexpected error in main execution: {str(e)}", exc_info=True)
    finally:
        if dataverse_client: 
            dataverse_client.close()
        logger.info("Script finished.")

if __name__ == "__main__":
    main()