import os
import json
import requests
from msal import ConfidentialClientApplication

# --- Configuration - Replace with your actual values or use environment variables ---
# Best practice is to use environment variables for sensitive data
CLIENT_ID = os.getenv("DATAVERSE_CLIENT_ID", "YOUR_APPLICATION_CLIENT_ID")
CLIENT_SECRET = os.getenv("DATAVERSE_CLIENT_SECRET", "YOUR_CLIENT_SECRET")
TENANT_ID = os.getenv("DATAVERSE_TENANT_ID", "YOUR_AZURE_TENANT_ID")
# e.g., https://myorg.crm.dynamics.com
DATAVERSE_ENV_URL = os.getenv(
    "DATAVERSE_ENV_URL", "https://yourorg.crm.dynamics.com")

AUTHORITY_URL = f"https://login.microsoftonline.com/{TENANT_ID}"
# v9.2 is common, adjust if needed
API_BASE_URL = f"{DATAVERSE_ENV_URL}/api/data/v9.2/"
SCOPE = [f"{DATAVERSE_ENV_URL}/.default"]  # Default scope for Dataverse

# --- Helper Function to Get Access Token ---


def get_dataverse_access_token():
    """Acquires an access token for Dataverse using client credentials."""
    app = ConfidentialClientApplication(
        client_id=CLIENT_ID,
        authority=AUTHORITY_URL,
        client_credential=CLIENT_SECRET,
    )
    result = app.acquire_token_silent(scopes=SCOPE, account=None)
    if not result:
        print("No suitable token in cache, acquiring a new one.")
        result = app.acquire_token_for_client(scopes=SCOPE)

    if "access_token" in result:
        return result["access_token"]
    else:
        print("Error acquiring token:")
        print(result.get("error"))
        print(result.get("error_description"))
        print(result.get("correlation_id"))
        return None

# --- Function to Get Conversation Transcript by Conversation ID ---


def get_conversation_transcript_by_id(conversation_id_to_find: str, access_token: str):
    """
    Fetches a specific conversation transcript from Dataverse by its 'conversationid' field.

    Args:
        conversation_id_to_find: The Bot Framework conversation ID to search for.
        access_token: The Dataverse access token.

    Returns:
        A dictionary containing the transcript data if found, else None.
    """
    if not access_token:
        print("Cannot fetch transcript without an access token.")
        return None

    # The entity set name for Conversation Transcripts is 'conversationtranscripts'
    # The field often storing the Bot Framework conversation ID is 'conversationid' (string type)
    # The primary key of the conversationtranscript entity is 'conversationtranscriptid' (GUID)
    # We are assuming 'conversation_id_to_find' refers to the Bot Framework's string ID.
    # If it's the Dataverse primary key (GUID), the filter would be different.

    # OData query to filter by the 'conversationid' field
    # Note: 'conversationid' is typically a string field.
    # If your 'conversationid' field in Dataverse has a different logical name, adjust it.
    odata_filter = f"$filter=conversationid eq '{conversation_id_to_find}'"
    # Select specific columns you need. 'content' usually holds the JSON of the conversation.
    # 'bot_conversationtranscriptid' might be a lookup to the bot.
    # 'createdon', 'modifiedon' are common date fields.
    # 'conversationtranscriptid' is the unique GUID primary key for the transcript record.
    odata_select = "$select=conversationtranscriptid,createdon,modifiedon,content,bot_conversationtranscriptid,schemaname"

    api_url = f"{API_BASE_URL}conversationtranscripts?{odata_select}&{odata_filter}"

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Accept": "application/json",
        "OData-MaxVersion": "4.0",
        "OData-Version": "4.0",
        "Prefer": "odata.include-annotations=\"*\""  # To get formatted values if needed
    }

    print(f"Requesting URL: {api_url}")

    try:
        response = requests.get(api_url, headers=headers)
        response.raise_for_status()  # Raises an HTTPError for bad responses (4XX or 5XX)

        result_json = response.json()
        transcripts = result_json.get("value", [])

        if transcripts:
            if len(transcripts) > 1:
                print(
                    f"Warning: Found {len(transcripts)} transcripts for conversation ID '{conversation_id_to_find}'. Returning the first one.")
            return transcripts[0]  # Return the first matching transcript
        else:
            print(
                f"No transcript found with conversation ID: {conversation_id_to_find}")
            return None

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        print(f"Response content: {response.text}")
    except requests.exceptions.RequestException as req_err:
        print(f"Request error occurred: {req_err}")
    except json.JSONDecodeError:
        print(f"Failed to decode JSON response: {response.text}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    return None


# --- Main Execution ---
if __name__ == "__main__":
    # Replace this with the actual conversation ID you want to fetch
    conversation_id_to_fetch = "YOUR_TARGET_CONVERSATION_ID"

    # Basic validation for placeholder values
    if any(placeholder in [CLIENT_ID, CLIENT_SECRET, TENANT_ID, DATAVERSE_ENV_URL, conversation_id_to_fetch]
           for placeholder in ["YOUR_APPLICATION_CLIENT_ID", "YOUR_CLIENT_SECRET",
                               "YOUR_AZURE_TENANT_ID", "https://yourorg.crm.dynamics.com",
                               "YOUR_TARGET_CONVERSATION_ID"]):
        print("Please update the configuration placeholders (CLIENT_ID, CLIENT_SECRET, TENANT_ID, DATAVERSE_ENV_URL) "
              "and 'conversation_id_to_fetch' with your actual values or set them as environment variables.")
    else:
        token = get_dataverse_access_token()
        if token:
            print("\nSuccessfully acquired access token.")
            transcript = get_conversation_transcript_by_id(
                conversation_id_to_fetch, token)

            if transcript:
                print(
                    f"\n--- Transcript Found for Conversation ID: {conversation_id_to_fetch} ---")
                print(
                    f"Dataverse Transcript Record ID (conversationtranscriptid): {transcript.get('conversationtranscriptid')}")
                print(f"Created On: {transcript.get('createdon')}")
                print(f"Bot Schema Name: {transcript.get('schemaname')}")

                content_json_str = transcript.get("content")
                if content_json_str:
                    print("\n--- Conversation Content (first 500 chars) ---")
                    print(
                        content_json_str[:500] + "..." if len(content_json_str) > 500 else content_json_str)

                    try:
                        # The 'content' field itself is a JSON string, parse it
                        parsed_content = json.loads(content_json_str)
                        print(
                            "\n--- Parsed Conversation Activities (example: first activity type) ---")
                        if isinstance(parsed_content, dict) and "activities" in parsed_content:
                            activities = parsed_content["activities"]
                            if activities and isinstance(activities, list) and len(activities) > 0:
                                print(
                                    f"First activity type: {activities[0].get('type')}")
                                print(
                                    f"Total activities in content: {len(activities)}")
                            else:
                                print("No activities found in the parsed content.")
                        # Sometimes content might be a direct list of activities
                        elif isinstance(parsed_content, list):
                            if parsed_content and len(parsed_content) > 0:
                                print(
                                    f"First activity type: {parsed_content[0].get('type')}")
                                print(
                                    f"Total activities in content: {len(parsed_content)}")
                        else:
                            print(
                                "Parsed content is not in the expected format (dict with 'activities' or list).")

                    except json.JSONDecodeError as e:
                        print(
                            f"\nError parsing conversation content JSON: {e}")
                else:
                    print("\nNo 'content' field found in the transcript.")
            else:
                print(
                    f"\nCould not retrieve transcript for Conversation ID: {conversation_id_to_fetch}")
        else:
            print("\nFailed to acquire access token. Cannot proceed.")
