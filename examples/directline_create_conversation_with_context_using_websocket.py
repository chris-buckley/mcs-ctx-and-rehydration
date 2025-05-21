import asyncio
import json
import logging
import os
from datetime import datetime
from typing import Any, Dict, List, Optional, Union, cast

from dotenv import load_dotenv
from websockets.asyncio.client import connect as ws_connect
from websockets.exceptions import (
    ConnectionClosedError,
    ConnectionClosedOK,
    InvalidHandshake,
    InvalidURI,
)

from direct_line.api.conversations_api import ConversationsApi
from direct_line.api_client import ApiClient
from direct_line.configuration import Configuration
from direct_line.exceptions import ApiException
from direct_line.models.activity import Activity
from direct_line.models.activity_set import ActivitySet
from direct_line.models.channel_account import ChannelAccount
from direct_line.models.conversation import Conversation
from direct_line.models.resource_response import ResourceResponse
from direct_line.models.token_parameters import TokenParameters
from utilities.custom_rich_logger import setup_logger, truncate_text
from models.user_context_data import ConversationContextData, use_default_conversation_data

# --- Configuration & Constants ---

load_dotenv()

logger: logging.Logger = setup_logger(logger_name="directline_websocket")
conversation_user_data: ConversationContextData = use_default_conversation_data()


DIRECT_LINE_SECRET: Optional[str] = os.getenv(key="DIRECT_LINE_SECRET")
USER_ID: str = conversation_user_data.user_id
LISTEN_IDLE_TIMEOUT: int = 15
TRACE_HEADERS: Dict[str, str] = {"X-MS-CONVERSATION-TRACE": "true"}
BASE_OUTPUT_DIR: str = "examples/data"
CONVERSATIONS_SUBDIR: str = "conversations"
TIMESTAMP_FORMAT: str = "%Y%m%d_%H%M%S"
SENT_FILENAME: str = "sent_activities.json"
RECEIVED_FILENAME: str = "received_activity_sets.json"


# --- Helper Functions ---

def _summarise_activity_obj(act: Activity) -> str:
    """Generates a concise summary string for an Activity object."""
    if act.text:
        return str(act.text).strip()
    if act.name:
        return f"<event:{act.name}>"
    if act.attachments:
        return f"<{len(act.attachments)} attachment(s)>"
    return f"<{act.type or 'activity'}>"


# --- Core Direct Line Functions ---

async def start_conversation() -> Optional[Conversation]:
    """Initiates a new Direct Line conversation using the secret."""
    if not DIRECT_LINE_SECRET:
        logger.error("DIRECT_LINE_SECRET not found in environment variables.")
        return None

    sdk_config: Configuration = Configuration()
    api_client_secret: ApiClient = ApiClient(
        configuration=sdk_config,
        header_name="Authorization",
        header_value=f"Bearer {DIRECT_LINE_SECRET}",
    )
    conversations_api: ConversationsApi = ConversationsApi(api_client=api_client_secret)

    logger.info("Starting a new conversation...")
    try:
        # Run blocking API call in a separate thread
        conversation_object: Conversation = await asyncio.to_thread(
            conversations_api.conversations_start_conversation,
            token_parameters=TokenParameters(),
        )
        logger.info("Conversation started successfully!")
        logger.info(f"  Conversation ID: {conversation_object.conversation_id}")
        logger.info(f"  Token: {truncate_text(str(conversation_object.token), 20)}...")
        logger.info(f"  Stream URL: {truncate_text(str(conversation_object.stream_url))}")
        logger.info(f"  Expires In: {conversation_object.expires_in} seconds")
        return conversation_object
    except ApiException as e:
        logger.error(f"API Error starting conversation: {e.status} {e.reason}")
        if e.body:
            try:
                error_details: Dict[str, Any] = json.loads(e.body)
                logger.error(f"Details: {json.dumps(error_details, indent=2)}")
            except json.JSONDecodeError:
                logger.error(f"Details (raw): {e.body}")
        return None
    except Exception:
        logger.exception("Unexpected error starting conversation:")
        return None


async def websocket_listener(
    uri: str,
    token: str,
    received_activities_log: List[Dict[str, Any]],
    user_id_to_skip: str,
) -> None:
    """Listens for incoming activities on the WebSocket stream."""
    headers: Dict[str, str] = {"Authorization": f"Bearer {token}", **TRACE_HEADERS}
    safe_uri: str = uri.split("?t=")[0] + "?t=<token_redacted>"
    logger.info(f"Connecting WebSocket -> {truncate_text(text=safe_uri)}")

    try:
        async with ws_connect(
            uri, additional_headers=headers, ping_interval=30, ping_timeout=30
        ) as ws:
            logger.info("WebSocket connected ✔")

            while True:
                try:
                    message: Union[str, bytes] = await asyncio.wait_for(
                        ws.recv(), timeout=LISTEN_IDLE_TIMEOUT
                    )
                except asyncio.TimeoutError:
                    logger.warning(f"No activity for {LISTEN_IDLE_TIMEOUT}s, closing WebSocket.")
                    break
                except (ConnectionClosedOK, ConnectionClosedError):
                    logger.info("WebSocket connection closed.")
                    break

                if not message:
                    continue

                message_str: str = message.decode("utf-8") if isinstance(message, bytes) else message

                try:
                    payload_dict: Dict[str, Any] = json.loads(message_str)
                    received_activities_log.append(payload_dict)

                    activity_set: ActivitySet = ActivitySet.from_dict(payload_dict)

                    if activity_set.watermark:
                        logger.debug(f"Received ActivitySet with watermark: {activity_set.watermark}")

                    if not activity_set.activities:
                        logger.debug("Received ActivitySet with no activities.")
                        continue

                    for act_obj in activity_set.activities:
                        if act_obj.type == "endOfConversation":
                            logger.info("Bot ended conversation (endOfConversation activity). Closing WebSocket.")
                            return # Exit listener gracefully

                        # Skip activities sent by this script's user
                        if act_obj.var_from and act_obj.var_from.id == user_id_to_skip:
                            logger.debug(f"Skipping own activity (type: {act_obj.type})")
                            continue

                        summary: str = _summarise_activity_obj(act_obj)
                        sender_name: str = "Bot"
                        if act_obj.var_from:
                            sender_name = act_obj.var_from.name or act_obj.var_from.id or "Bot"

                        logger.info(f"← {sender_name}: {truncate_text(summary)}")

                except json.JSONDecodeError:
                    logger.warning(f"Received non-JSON WebSocket message: {truncate_text(message_str, 100)}")
                except Exception as e:
                    logger.exception(f"Error processing WebSocket message: {e}")
                    break # Exit loop on processing error

    except ConnectionClosedOK:
        logger.info("WebSocket closed gracefully by server.")
    except ConnectionClosedError as e:
        logger.error(f"WebSocket connection closed with error: {e.code} {e.reason}")
    except InvalidURI:
        logger.error(f"Invalid WebSocket URI: {safe_uri}")
    except InvalidHandshake as e:
        logger.error(f"WebSocket handshake failed: {e}")
    except Exception:
        logger.exception("WebSocket error:")


async def send_activity(
    conversations_api: ConversationsApi,
    conversation_id: str,
    activity: Activity,
    sent_activities_log: List[Dict[str, Any]],
) -> Optional[ResourceResponse]:
    """Sends an activity to the Direct Line conversation."""
    sent_activities_log.append(activity.to_dict())
    activity_type: Optional[str] = activity.type
    activity_name: Optional[str] = getattr(activity, "name", None)

    log_identifier: str = f"'{activity_name}' event" if activity_type == "event" and activity_name else activity_type or "activity"

    logger.info(f"→ Sending {log_identifier}...")
    try:
        # Run blocking API call in a separate thread
        response: ResourceResponse = await asyncio.to_thread(
            conversations_api.conversations_post_activity,
            conversation_id=conversation_id,
            activity=activity,
        )
        logger.info(f"  {log_identifier.capitalize()} sent successfully (ID: {response.id})")
        return response
    except ApiException as e:
        logger.error(f"API Error sending {log_identifier}: {e.status} {e.reason}")
        if e.body:
            try:
                error_details: Dict[str, Any] = json.loads(e.body)
                logger.error(f"Details: {json.dumps(error_details, indent=2)}")
            except json.JSONDecodeError:
                logger.error(f"Details (raw): {e.body}")
        return None
    except Exception:
        logger.exception(f"Unexpected error sending {log_identifier}:")
        return None

# --- Main Execution Logic ---

async def example_usage(user_input: str) -> None:
    """Main function to start conversation, listen, send, and save logs."""
    start_time: datetime = datetime.now()
    logger.info(f"Starting Direct Line WebSocket example at {start_time.isoformat()}")

    if not DIRECT_LINE_SECRET:
        logger.critical("DIRECT_LINE_SECRET environment variable not set. Exiting.")
        return

    # Variables needed across try/finally
    conversation_info: Optional[Conversation] = None
    conv_id: Optional[str] = None
    ws_task: Optional[asyncio.Task[None]] = None
    sent_activities_log: List[Dict[str, Any]] = []
    received_activities_log: List[Dict[str, Any]] = []

    try:
        conversation_info = await start_conversation()
        if not (conversation_info and conversation_info.conversation_id and
                conversation_info.token and conversation_info.stream_url):
            logger.critical("Failed to start conversation. Exiting.")
            return

        conv_id = cast(str, conversation_info.conversation_id)
        conv_token: str = cast(str, conversation_info.token)
        stream_url: str = cast(str, conversation_info.stream_url)

        sdk_config_token: Configuration = Configuration()
        api_client_token: ApiClient = ApiClient(
            configuration=sdk_config_token,
            header_name="Authorization",
            header_value=f"Bearer {conv_token}",
        )
        conversations_api_token: ConversationsApi = ConversationsApi(api_client=api_client_token)

        ws_task = asyncio.create_task(
            websocket_listener(
                uri=stream_url,
                token=conv_token,
                received_activities_log=received_activities_log,
                user_id_to_skip=USER_ID,
            )
        )

        await asyncio.sleep(2) # Allow time for WebSocket to connect

        if ws_task.done():
            exc: Optional[BaseException] = ws_task.exception()
            if exc:
                logger.error(f"WebSocket listener failed to start or connect: {exc}")
                raise exc # Propagate critical error
            else:
                logger.warning("WebSocket listener finished unexpectedly after connection attempt.")
                return # Exit if listener ended prematurely without error

        # --- Send initial activities ---
        initial_event_activity: Activity = Activity(
            type="event",
            name="setConversationContext",
            value=conversation_user_data.model_dump(),
            var_from=ChannelAccount(id=USER_ID),
            locale="en-AU",
            channel_id="directline",
        )
        await send_activity(conversations_api_token, conv_id, initial_event_activity, sent_activities_log)

        greeting_activity: Activity = Activity(
            type="message",
            var_from=ChannelAccount(id=USER_ID),
            text=user_input,
            locale="en-AU",
            channel_id="directline",
        )
        await send_activity(conversations_api_token, conv_id, greeting_activity, sent_activities_log)

        logger.info("Listening for bot replies... (Press Ctrl+C to stop)")
        if ws_task:
            await ws_task # Wait for the listener to complete naturally or be cancelled

    except KeyboardInterrupt:
        logger.warning("Interrupted by user (Ctrl+C)")
    except ApiException as e:
        logger.error(f"Caught API Exception during interaction: {e.status} {e.reason}")
        if e.body: logger.error(f"Details: {e.body}")
    except Exception:
        logger.exception("An unexpected error occurred:")
    finally:
        # --- Politely close the chat (NEW) ---
        if conv_id and "conversations_api_token" in locals() and conversations_api_token:
            try:
                end_activity = Activity(
                    type="endOfConversation",
                    code="completedSuccessfully",
                    var_from=ChannelAccount(id=USER_ID),
                    locale="en-AU",
                    channel_id="directline",
                )
                await send_activity(
                    conversations_api_token,
                    conv_id,
                    end_activity,
                    sent_activities_log,
                )
                logger.info("Sent endOfConversation activity to close the session.")
            except Exception:
                logger.exception("Failed to send endOfConversation activity:")

        # --- Cleanup WebSocket Task ---
        if ws_task and not ws_task.done():
            logger.info("Cancelling WebSocket listener task...")
            ws_task.cancel()
            try:
                await ws_task
            except asyncio.CancelledError:
                logger.info("WebSocket listener task cancelled.")
            except Exception:
                logger.exception("Error during WebSocket task cleanup:")

        # --- Save Conversation Data ---
        logger.info("Attempting to save conversation data...")
        if conv_id:
            try:
                timestamp_str: str = start_time.strftime(TIMESTAMP_FORMAT)
                conversation_dir_name: str = f"{timestamp_str}-{conv_id}"
                output_dir: str = os.path.join(BASE_OUTPUT_DIR, CONVERSATIONS_SUBDIR, conversation_dir_name)

                os.makedirs(output_dir, exist_ok=True)
                logger.info(f"Saving logs to directory: {output_dir}")

                sent_file_path: str = os.path.join(output_dir, SENT_FILENAME)
                with open(sent_file_path, 'w', encoding='utf-8') as f_sent:
                    json.dump(sent_activities_log, f_sent, indent=2, ensure_ascii=False)
                logger.info(f"Saved {len(sent_activities_log)} sent activities to {sent_file_path}")

                received_file_path: str = os.path.join(output_dir, RECEIVED_FILENAME)
                with open(received_file_path, 'w', encoding='utf-8') as f_received:
                    json.dump(received_activities_log, f_received, indent=2, ensure_ascii=False)
                logger.info(f"Saved {len(received_activities_log)} received activity sets to {received_file_path}")

            except OSError as e:
                logger.error(f"Failed to create directory or write log files in {output_dir}: {e}")
            except Exception:
                logger.exception(f"An unexpected error occurred while saving conversation data:")
        else:
            logger.warning("Conversation ID not available. Skipping saving logs.")

        # --- Final Log ---
        end_time: datetime = datetime.now()
        duration: float = (end_time - start_time).total_seconds()
        logger.info(f"Example finished at {end_time.isoformat()}. Duration: {duration:.2f} seconds.")


if __name__ == "__main__":
    # Potentially ask, "Could you walk me through what I can do next on this page?"
    user_input: str = input("Enter a message to send to the bot: ")
    if not USER_ID:
        logger.critical("USER_ID environment variable not set. Please set it.")
    elif not DIRECT_LINE_SECRET:
        logger.critical("DIRECT_LINE_SECRET environment variable not set. Please set it.")
    else:
        asyncio.run(example_usage(user_input=user_input))
