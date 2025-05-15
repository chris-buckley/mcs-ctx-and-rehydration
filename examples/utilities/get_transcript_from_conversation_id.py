from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
from typing import List, Optional, Set

from direct_line.models.activity import Activity
from direct_line.models.activity_set import ActivitySet

from utilities.get_all_activities_from_conversation_id import (
    get_all_activities_from_conversation_id,
)
from utilities.custom_rich_logger import setup_logger, truncate_text
from models.transcript import Transcript, Message



logger = setup_logger()

def _activity_to_message(activity: Activity) -> Optional[Message]:
    """
    Convert a Direct Line `Activity` (of type == "message") to our internal
    `Message` schema.  If required keys are missing, return ``None`` and log.
    """
    try:
        sender: str | None = ""
        if not activity.var_from.name:
            sender: str | None = activity.var_from.id
        else:
            sender: str | None = activity.var_from.name

        return Message(
            timestamp=activity.timestamp.isoformat(),
            from_id=str(sender),
            message=activity.text or "",
        )

    except Exception as exc:  # noqa: BLE001
        logger.warning(
            "Cannot convert activity %s to Message: %s – skipped.",
            getattr(activity, "id", "<no-id>"),
            exc,
        )
        return None


def get_transcript_from_conversation_id(conversation_id: str) -> Optional[Transcript]:
    """
    Fetch **all** activities for the given conversation and return a `Transcript`
    object that includes only those with ``type == "message"``.

    Returns
    -------
    Transcript | None
        • Populated `Transcript` on success.  
        • `None` on failure (errors already logged).
    """
    activity_set: Optional[ActivitySet] = get_all_activities_from_conversation_id(
        conversation_id
    )
    if activity_set is None:  # Errors already logged inside the helper.
        return None

    logger.info(
        "Transforming %d activities into Transcript messages.",
        len(activity_set.activities or []),
    )

    messages: List[Message] = []

    for activity in activity_set.activities or []:
        if activity.type != "message":
            continue

        msg: Optional[Message] = _activity_to_message(activity)
        if msg is None:
            continue

        messages.append(msg)

    if not messages:
        logger.warning(
            "No message-type activities found for conversation %s.", conversation_id
        )
        return None

    # Ensure chronological order (oldest → newest) just in case.
    messages.sort(key=lambda m: m.timestamp)

    transcript = Transcript(
        conversation_id=conversation_id,
        messages=messages,
    )

    logger.debug(
        "Transcript built: %d messages, %d participants.",
        len(transcript.messages),
    )
    return transcript


# --------------------------------------------------------------------------- #
# Optional helper: save Transcript to disk                                    #
# --------------------------------------------------------------------------- #
def save_transcript_to_json(transcript: Transcript, output_dir: Path | str | None = None) -> Path:
    """
    Persist a Transcript to `examples/data/transcripts/<conversation_id>.json`.

    Returns the path written on success.  Raises on IO errors so callers can
    decide how to handle them.
    """
    if output_dir is None:
        output_dir = Path("examples/data/transcripts")
    output_path: Path = Path(output_dir) / f"{transcript.conversation_id}.json"

    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, "w", encoding="utf-8") as fp:
        fp.write(transcript.model_dump_json(indent=2))

    logger.info("Transcript saved to %s", output_path)
    return output_path
