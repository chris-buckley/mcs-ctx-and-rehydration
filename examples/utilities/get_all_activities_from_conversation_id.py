import os
import json
from pathlib import Path
from typing import Optional, List, Dict, Any

from dotenv import load_dotenv

from direct_line.api_client import ApiClient
from direct_line.api.conversations_api import ConversationsApi
from direct_line.models.activity import Activity
from direct_line.models.activity_set import ActivitySet
from direct_line.exceptions import ApiException

# This import is specified by the user.
from utilities.custom_rich_logger import setup_logger, truncate_text

logger = setup_logger()


def get_all_activities_from_conversation_id(
    conversation_id: str,
) -> Optional[ActivitySet]:
    """
    Fetch **all** activities for the supplied `conversation_id` via the Direct
    Line API and return them collected inside a single `ActivitySet`.

    Returns
    -------
    ActivitySet | None
        • `ActivitySet` on success.  
        • `None` on failure (errors are already logged).
    """
    load_dotenv()
    direct_line_secret: Optional[str] = os.getenv("DIRECT_LINE_SECRET")

    if not direct_line_secret:
        logger.error(
            "DIRECT_LINE_SECRET not found in .env file or environment variables."
        )
        return None

    api_client = ApiClient()
    conversations_api = ConversationsApi(api_client=api_client)
    auth_headers: Dict[str, str] = {"Authorization": f"Bearer {direct_line_secret}"}

    collected: List[Activity] = []
    current_watermark: Optional[str] = None

    logger.info("Fetching activities for conversation ID: %s", conversation_id)

    try:
        while True:
            logger.debug(
                "Calling API with watermark=%s", current_watermark or "initial"
            )
            activity_set: ActivitySet = conversations_api.conversations_get_activities(
                conversation_id=conversation_id,
                watermark=current_watermark,
                _headers=auth_headers,
            )

            if not activity_set.activities:
                logger.info("No more activities returned – fetch finished.")
                break

            collected.extend(activity_set.activities)
            logger.info(
                "Fetched %d new activities (total=%d).",
                len(activity_set.activities),
                len(collected),
            )

            # Prepare for next loop
            if activity_set.watermark == current_watermark:
                logger.warning(
                    "Watermark repeated without change; assuming end of history."
                )
                break

            current_watermark = activity_set.watermark

    except ApiException as e:
        extra = ""
        if hasattr(e, "body") and e.body:
            try:
                extra = f" Details: {truncate_text(json.loads(e.body), 200)}"
            except (json.JSONDecodeError, TypeError):
                extra = f" Body: {truncate_text(str(e.body), 200)}"
        logger.error("API error %s %s.%s", e.status, e.reason, extra)
        return None
    except Exception as e:  # noqa: BLE001
        logger.error("Unexpected error: %s - %s", e.__class__.__name__, e)
        return None

    logger.debug(
        "Returning ActivitySet with %d activities, watermark=%s",
        len(collected),
        current_watermark,
    )
    return ActivitySet(activities=collected, watermark=current_watermark)


def save_all_activities_from_conversation_id(conversation_id: str) -> None:
    """
    Fetch all activities for a conversation and save them to:
    examples/data/conversations_from_activities/<conversation_id>.json
    """
    activity_set: Optional[ActivitySet] = get_all_activities_from_conversation_id(
        conversation_id
    )
    if activity_set is None:  # errors already logged
        return

    activities_data: List[Dict[str, Any]] = [
        activity.to_dict() for activity in activity_set.activities or []
    ]

    output_dir = Path("examples/data/conversations_from_activities")
    try:
        output_dir.mkdir(parents=True, exist_ok=True)
    except OSError as e:
        logger.error("Cannot create output dir %s: %s", output_dir, e)
        return

    file_path = output_dir / f"{conversation_id}.json"
    try:
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(activities_data, f, indent=2)
        logger.info(
            "Saved %d activities to %s",
            len(activity_set.activities or []),
            file_path,
        )
    except IOError as e:
        logger.error("File-write error for %s: %s", file_path, e)
    except Exception as e:  # noqa: BLE001
        logger.error(
            "Unexpected error during file writing: %s - %s",
            e.__class__.__name__,
            e,
        )

if __name__ == "__main__":
    logger.info("Script execution started (example usage).")

    placeholder_id = "your_conversation_id_here"
    example_conversation_id_input: str = input(
        f"Enter the conversation ID to fetch activities from "
        f"(or leave as '{placeholder_id}' to skip): "
    ).strip()

    if (
        not example_conversation_id_input
        or example_conversation_id_input == placeholder_id
    ):
        logger.info(
            "Input is '%s', treated as placeholder/empty. Skipping actual fetch.",
            example_conversation_id_input,
        )
    elif not os.getenv("DIRECT_LINE_SECRET") and not Path(".env").exists():
        logger.warning(
            "DIRECT_LINE_SECRET not found in environment and no .env file detected."
        )
        logger.warning(
            "Please set DIRECT_LINE_SECRET in a .env file or environment variable "
            "for the example to run."
        )
    else:
        # 1) Fetch into memory
        activity_set = get_all_activities_from_conversation_id(
            example_conversation_id_input
        )
        if activity_set:
            logger.info(
                "Fetched %d activities in-memory. Latest watermark: %s.",
                len(activity_set.activities or []),
                activity_set.watermark,
            )

        # 2) Save to disk
        save_all_activities_from_conversation_id(example_conversation_id_input)

    logger.info("Script execution finished (example usage).")
