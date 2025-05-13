from logging import Logger
import os
import json
from dotenv import load_dotenv

from direct_line.api_client import ApiClient
from direct_line.configuration import Configuration
from direct_line.api.conversations_api import ConversationsApi
from direct_line.models.activity import Activity
from direct_line.models.channel_account import ChannelAccount
from direct_line.models.conversation import Conversation
from direct_line.exceptions import ApiException

from utilities.custom_rich_logger import setup_logger, truncate_text

logger: Logger = setup_logger(logger_name="custom_event_sender")

load_dotenv()

DIRECT_LINE_SECRET: str | None = os.getenv("DIRECT_LINE_SECRET")
EXAMPLE_USER_ID: str = os.getenv("DIRECT_LINE_USER_ID", "PythonDirectLineClientUser")

def start_new_conversation_and_get_token(
    direct_line_secret: str,
) -> tuple[str | None, str | None]:
    if not direct_line_secret:
        logger.error("Direct Line secret is missing.")
        return None, None

    sdk_config = Configuration()
    api_client_with_secret = ApiClient(
        configuration=sdk_config,
        header_name="Authorization",
        header_value=f"Bearer {direct_line_secret}",
    )
    conversations_api = ConversationsApi(api_client=api_client_with_secret)

    logger.info("Starting a new conversation...")
    try:
        conversation_object: Conversation = (
            conversations_api.conversations_start_conversation()
        )
        conversation_id = conversation_object.conversation_id
        conversation_token = conversation_object.token

        logger.info(f"Conversation started: {conversation_id}")
        return conversation_id, conversation_token
    except ApiException as e:
        logger.error(f"API Error starting conversation: {e.status} {e.reason}")
        if e.body:
            try:
                error_details = json.loads(e.body)
                logger.error(f"Details: {json.dumps(error_details, indent=2)}")
            except json.JSONDecodeError:
                logger.error(f"Details (raw): {e.body}")
        return None, None
    except Exception as e:
        logger.exception("Unexpected error starting conversation:")
        return None, None

def send_custom_event_activity(
    direct_line_token: str, conversation_id: str, user_id: str
) -> None:
    if not all([direct_line_token, conversation_id, user_id]):
        logger.error("Missing token, conversation ID, or user ID to send event.")
        return

    sdk_config = Configuration()
    api_client_with_token = ApiClient(
        configuration=sdk_config,
        header_name="Authorization",
        header_value=f"Bearer {direct_line_token}",
    )
    conversations_api = ConversationsApi(api_client=api_client_with_token)

    conversation_context_data_payload = {
        "deviceType": "PythonClient",
        "operatingSystem": os.name,
        "customInfo": "Sent via Direct Line SDK",
    }

    event_activity = Activity(
        type="event",
        name="setConversationContext",
        var_from=ChannelAccount(id=user_id),
        value={"ConversationContextData": conversation_context_data_payload},
        channel_id="directline",
    )

    logger.info(f"Sending event '{event_activity.name}' to conversation: {conversation_id}")
    try:
        resource_response = conversations_api.conversations_post_activity(
            conversation_id=conversation_id, activity=event_activity
        )
        logger.info(f"Event activity sent successfully. Response ID: {resource_response.id}")
    except ApiException as e:
        logger.error(f"API Error sending event activity: {e.status} {e.reason}")
        if e.body:
            try:
                error_details = json.loads(e.body)
                logger.error(f"Details: {json.dumps(error_details, indent=2)}")
            except json.JSONDecodeError:
                logger.error(f"Details (raw): {e.body}")
    except Exception as e:
        logger.exception("Unexpected error sending event activity:")

def main() -> None:
    logger.info("Direct Line Custom Event Sender Initializing...")

    if not DIRECT_LINE_SECRET:
        logger.critical("DIRECT_LINE_SECRET is not set.")
        logger.critical("Ensure it is in your .env file or environment variables.")
        return

    conversation_id, conversation_token = start_new_conversation_and_get_token(
        DIRECT_LINE_SECRET
    )

    if not (conversation_id and conversation_token):
        logger.error("Failed to start a conversation. Aborting event send.")
        return

    send_custom_event_activity(
        direct_line_token=conversation_token,
        conversation_id=conversation_id,
        user_id=EXAMPLE_USER_ID,
    )

    logger.info("Script finished.")

if __name__ == "__main__":
    main()