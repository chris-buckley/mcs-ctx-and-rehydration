import logging
import os
from typing import Any, Dict, List, Optional
import msal

from dotenv import load_dotenv
import httpx

# Assuming utilities.custom_rich_logger exists and setup_logger is defined
# If not, you might need to replace it with standard logging
try:
    from utilities.custom_rich_logger import setup_logger
    logger: logging.Logger = setup_logger(logger_name="dataverse_client")
except ImportError:
    logger = logging.getLogger("dataverse_client")
    logging.basicConfig(level=logging.INFO, format='[%(asctime)s] %(levelname)-8s %(message)s', datefmt='%H:%M:%S')
    logger.info("custom_rich_logger not found, using standard logging.")


# Load environment variables
load_dotenv()
CLIENT_ID: Optional[str] = os.getenv(key="CLIENT_ID")
TENANT_ID: Optional[str] = os.getenv(key="TENANT_ID")
CLIENT_SECRET: Optional[str] = os.getenv(key="CLIENT_SECRET")
WEB_API_ENDPOINT: str = os.getenv(key="WEB_API_ENDPOINT", default="").rstrip("/")

# Check env vars
if not all([CLIENT_ID, TENANT_ID, CLIENT_SECRET, WEB_API_ENDPOINT]):
    logger.error(msg="Missing required environment variables. Please check your .env file.")
    missing: list = []
    if not CLIENT_ID: missing.append("CLIENT_ID")
    if not TENANT_ID: missing.append("TENANT_ID")
    if not CLIENT_SECRET: missing.append("CLIENT_SECRET")
    if not WEB_API_ENDPOINT: missing.append("WEB_API_ENDPOINT")
    logger.error(msg=f"Missing variables: {', '.join(missing)}")
    exit(code=1)

# Assert that the critical variables are not None after the check for type hinting
assert CLIENT_ID is not None
assert TENANT_ID is not None
assert CLIENT_SECRET is not None

DATAVERSE_ENDPOINT_WITH_API_VERSION: str = f"{WEB_API_ENDPOINT}/api/data/v9.2"

# Acquire access token
def get_access_token() -> str:
    """
    Acquire an access token for the Microsoft Dataverse API.
    Returns:
        str: The access token
    """
    logger.info("Acquiring access token...")
    authority: str = f"https://login.microsoftonline.com/{TENANT_ID}"
    scope: list[str] = [f"{WEB_API_ENDPOINT}/.default"]
    app = msal.ConfidentialClientApplication(
        client_id=CLIENT_ID, authority=authority, client_credential=CLIENT_SECRET,
    )
    result = app.acquire_token_for_client(scopes=scope)
    if "access_token" in result:
        logger.info("✓ Successfully acquired access token")
        return result["access_token"]
    else:
        error_desc = result.get('error_description', 'Unknown error')
        logger.error(f"Error acquiring token: {error_desc}")
        raise Exception(f"Error acquiring token: {error_desc}")

class DataverseClient:
    """Client for interacting with Microsoft Dataverse API"""

    def __init__(self, base_url: str, access_token: str, client_timeout: float = 30.0):
        self.base_url = base_url.rstrip("/")
        self.headers = {
            "Authorization": f"Bearer {access_token}",
            "Accept": "application/json",
            "OData-MaxVersion": "4.0",
            "OData-Version": "4.0",
            "Content-Type": "application/json; charset=utf-8"
        }
        self.client = httpx.Client(timeout=client_timeout)

    def request(self, endpoint: str, method: str = "GET", data: Optional[Dict[str, Any]] = None, params: Optional[Dict[str, Any]] = None) -> Optional[Dict[str, Any]]:
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        try:
            response = self.client.request(
                method,
                url,
                json=data,
                params=params,
                headers=self.headers
            )
            response.raise_for_status()
            if not response.content or response.status_code == 204:
                return None
            return response.json()
        except httpx.HTTPStatusError as e:
            logger.error(f"Dataverse API HTTP error: {e.response.status_code} - {e.response.text} for URL: {e.request.url}")
            raise
        except httpx.RequestError as e:
            logger.error(f"Dataverse API Request error: {str(e)} for URL: {e.request.url}")
            raise
        except Exception as e:
            logger.error(f"Unexpected error during Dataverse API request: {str(e)}")
            raise

    def get_entities(self, entity_name: str, select: Optional[List[str]] = None, filter_query: Optional[str] = None, expand: Optional[str] = None, top: Optional[int] = None, order_by: Optional[str] = None) -> List[Dict[str, Any]]:
        params: Dict[str, Any] = {}
        if select:
            params["$select"] = ",".join(select)
        if filter_query:
            params["$filter"] = filter_query
        if expand:
            params["$expand"] = expand
        if top is not None:
            params["$top"] = str(top)
        if order_by:
            params["$orderby"] = order_by
        response_data = self.request(entity_name, params=params)
        return response_data.get("value", []) if response_data else []

    def close(self):
        if hasattr(self, 'client') and self.client:
            self.client.close()
            logger.info("DataverseClient's httpx client closed.")

# Removed get_bot_id_by_name as it's not directly used in the updated main block for listing all bots.
# You can keep it if you need it for other purposes.

if __name__ == "__main__":
    dataverse_client: Optional[DataverseClient] = None
    try:
        # Acquire access token
        dataverse_access_token: str = get_access_token()
        logger.info(msg="Access token acquired successfully.")

        # Initialize Dataverse Client
        dataverse_client = DataverseClient(
            base_url=DATAVERSE_ENDPOINT_WITH_API_VERSION,
            access_token=dataverse_access_token
        )

        logger.info("Fetching list of all bots...")
        # Select the fields you want to display for each bot.
        # Common fields include 'name', 'botid', 'ownerid', 'createdon', 'modifiedon', 'schemaname'
        # You can find more fields by exploring the 'bot' entity metadata in Dataverse or Power Apps.
        bots_list: List[Dict[str, Any]] = dataverse_client.get_entities(
            entity_name="bots", # Logical name for the Bot entity
            select=["name", "botid", "createdon", "schemaname"], # Add or remove fields as needed
            order_by="name" # Optional: order the results, e.g., by name
        )

        if bots_list:
            logger.info(f"Found {len(bots_list)} bots:")
            for bot in bots_list:
                bot_id = bot.get('botid', 'N/A')
                bot_name = bot.get('name', 'N/A')
                bot_schema_name = bot.get('schemaname', 'N/A')
                bot_created_on = bot.get('createdon', 'N/A')
                logger.info(f"  - Name: {bot_name}, ID: {bot_id}, SchemaName: {bot_schema_name}, Created: {bot_created_on}")
        else:
            logger.info("No bots found in the environment.")

    except httpx.HTTPStatusError as e:
        # This will catch the 403 error if it still occurs,
        # or other HTTP errors from the get_entities call.
        logger.error(f"Failed to fetch bots due to an HTTP error (already logged by DataverseClient).")
        # The specific error (like the 403) is already logged by the DataverseClient.
        # If you still get 403, the permissions/setup issue for the App User in Dataverse needs to be resolved.
    except Exception as e:
        logger.error(f"An error occurred in the main execution: {str(e)}")
    finally:
        if dataverse_client:
            dataverse_client.close()
        logger.info("Script finished.")