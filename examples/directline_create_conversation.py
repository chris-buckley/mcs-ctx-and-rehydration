import os
import logging
from dotenv import load_dotenv

from direct_line.api_client import ApiClient
from direct_line.configuration import Configuration
from direct_line.api.conversations_api import ConversationsApi
from direct_line.exceptions import ApiException

from direct_line.models.conversation import Conversation
from utilities.custom_rich_logger import setup_logger, truncate_text

logger: logging.Logger = setup_logger(logger_name="directline_app")

def create_direct_line_conversation_and_get_token() -> None | tuple[str | None, str | None]:
    load_dotenv()
    direct_line_secret: str | None = os.getenv(key="DIRECT_LINE_SECRET")

    if not direct_line_secret:
        logger.error(msg="DIRECT_LINE_SECRET not found in .env file or environment variables.")
        return None

    sdk_config = Configuration()

    api_client = ApiClient(
        configuration=sdk_config,
        header_name="Authorization",
        header_value=f"Bearer {direct_line_secret}"
    )

    conversations_api = ConversationsApi(api_client=api_client)

    logger.info(msg="Starting a new conversation...")
    try:
        conversation_object: Conversation = conversations_api.conversations_start_conversation()

        conversation_id: str | None = conversation_object.conversation_id
        conversation_token: str | None = conversation_object.token
        stream_url: str | None = conversation_object.stream_url
        expires_in: int | None = conversation_object.expires_in

        logger.info(msg="Conversation started successfully!")
        logger.info(msg=f"  Conversation ID: {conversation_id}")
        logger.info(msg=f"  Conversation Token: {truncate_text(text=conversation_token, limit=40)}")
        logger.info(msg=f"  Stream URL: {truncate_text(text=str(object=stream_url))}")
        logger.info(msg=f"  Token Expires In (seconds): {expires_in}")

        return conversation_id, conversation_token

    except ApiException as e:
        logger.error(msg=f"Error starting conversation: {e}")
        if e.body:
            logger.error(msg=f"Error details: {e.body}")
        return None

if __name__ == "__main__":
    result: None | tuple[str | None, str | None] = create_direct_line_conversation_and_get_token()
    if result:
        conv_id, token = result
        logger.info(f"\nReady to use Conversation ID '{conv_id}' with Token '{truncate_text(token, limit=20)}...'")