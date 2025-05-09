"""
start_conversation_with_context.py — Direct Line Example to start a conversation
with context and save the transcript.

--------------------- Flow ---------------------
• Start a conversation with the Direct Line API.
• Send an initial event and a greeting message.
• Listen for bot replies via WebSocket.
• Save the full transcript to disk.

Dependencies:
    python-dotenv
    httpx>=0.25
    directline_client
    websockets>=14
"""

from __future__ import annotations

import asyncio
import contextlib
import inspect
import json
import logging
import os
import time
from datetime import datetime
from typing import Any, Dict, List, Optional, cast

import httpx
import websockets
from dotenv import load_dotenv
from websockets.legacy.client import connect as ws_connect_legacy  # type: ignore

# Direct Line client imports
from directline_client import AuthenticatedClient
from directline_client.api.conversations import (
    conversations_post_activity,
    conversations_start_conversation,
)
from directline_client.models import (
    Activity,
    ActivityValue,
    ChannelAccount,
    Conversation,
    ResourceResponse,
    TokenParameters,
)
from directline_client.types import Response

# ──────────────────────────────  CONFIG  ────────────────────────────── #

DEBUG: bool = False               # flip True for wire-level traces
MAX_LOG_TEXT_LEN: int = 120       # truncate long text when not debugging

load_dotenv()

TOKEN: str = os.getenv("DIRECT_LINE_SECRET", "")
if not TOKEN:
    raise RuntimeError(
        "Set your Direct Line secret in the DIRECT_LINE_SECRET environment variable."
    )

USER_ID: str = "example_user_123"
BASE_URL: str = "https://directline.botframework.com"
TRACE_HEADERS: Dict[str, str] = {"X-MS-CONVERSATION-TRACE": "true"}
OUTPUT_DIR_BASE: str = "data/conversation_activities"

# ────────────────────  LIGHTWEIGHT COLOURED LOGGING  ─────────────────── #


class _Ansi:
    RESET = "\033[0m"
    DIM = "\033[2m"
    RED, GRN, YLW, CYN, MAG = (
        "\033[91m", "\033[92m", "\033[93m", "\033[96m", "\033[95m"
    )


class _ColourFormatter(logging.Formatter):
    _LVL = {
        logging.DEBUG: _Ansi.CYN,
        logging.INFO:  _Ansi.GRN,
        logging.WARNING: _Ansi.YLW,
        logging.ERROR: _Ansi.RED,
        logging.CRITICAL: _Ansi.MAG,
    }

    def format(self, record: logging.LogRecord) -> str:  # noqa: D401
        colour = self._LVL.get(record.levelno, _Ansi.RESET)
        record.levelname = f"{colour}{record.levelname}{_Ansi.RESET}"
        return super().format(record)


_log = logging.getLogger("directline")
_log.setLevel(logging.DEBUG if DEBUG else logging.INFO)
_handler = logging.StreamHandler()
_handler.setFormatter(
    _ColourFormatter(
        f"{_Ansi.DIM}%(asctime)s{_Ansi.RESET}  %(levelname)s  %(message)s"
    )
)
_log.addHandler(_handler)

if DEBUG:
    httpx_logger = logging.getLogger("httpx")
    httpx_logger.setLevel(logging.DEBUG)
    httpx_logger.addHandler(_handler)

# ─────────────────────────  HELPER: TEXT TRUNCATION  ─────────────────── #


def _short(text: str, limit: int = MAX_LOG_TEXT_LEN) -> str:
    """Return *text* truncated to *limit* chars (only when DEBUG is False)."""
    if DEBUG or len(text) <= limit:
        return text
    return text[: limit - 1] + "…"

# ──────────────  HELPER: SUMMARISE ACTIVITY WHEN TEXT IS BLANK  ───────── #


def _summarise_activity(act: Dict[str, Any]) -> str:
    """Provide a concise fallback description for activities with no text."""
    txt: str = str(act.get("text", "") or "").strip()
    if txt:
        return txt
    if act.get("name"):
        return f"<event:{act['name']}>"
    if (attachments := act.get("attachments")):
        return f"<{len(attachments)} attachment(s)>"
    return f"<{act.get('type', 'activity')}>"

# ────────────────────────  HTTPX HOOKS (optional)  ────────────────────── #


def _safe_decode(raw: Optional[bytes]) -> str:
    if not raw:
        return ""
    try:
        return raw.decode()
    except UnicodeDecodeError:
        return f"<{len(raw)}-byte binary>"


async def _log_req(request: httpx.Request) -> None:
    request.extensions["t0"] = time.perf_counter()
    if not DEBUG:
        return
    body = _safe_decode(await request.aread())
    _log.debug(
        "%s⇢ %s %s\n%s\n\n%s",
        _Ansi.CYN,
        request.method,
        request.url,
        body or "<empty>",
    )


async def _log_res(response: httpx.Response) -> None:
    if not DEBUG:
        return
    t0: float = response.request.extensions.get(
        "t0", 0.0)  # type: ignore[assignment]
    ms: int = int((time.perf_counter() - t0) * 1000)
    await response.aread()
    _log.debug(
        "%s⇠ %s %s (%d ms)\n%s\n\n%s",
        _Ansi.CYN,
        response.status_code,
        response.request.url,
        ms,
        _safe_decode(response.content) or "<empty>",
    )

# ─────────────────────────  WEBSOCKET LISTENER  ───────────────────────── #

LISTEN_IDLE_TIMEOUT = 60


async def _ws_listener(
    uri: str,
    conv_token: str,
    sink: List[Dict[str, Any]],
) -> None:
    """Open the Direct Line WS stream and push every payload into *sink*.

    • Ignores empty / non-JSON frames instead of exploding.
    • Closes the socket after LISTEN_IDLE_TIMEOUT s of quiet.
    """
    headers: Dict[str, str] = {
        "Authorization": f"Bearer {conv_token}", **TRACE_HEADERS
    }
    safe_uri = uri.split("&t=")[0] + "&t=<redacted>"
    _log.info("Connecting WebSocket → %s", safe_uri)

    sig = inspect.signature(ws_connect_legacy)
    kw: Dict[str, Any] = {
        ("additional_headers" if "additional_headers" in sig.parameters else "extra_headers"): headers,  # noqa: E501
        "ping_interval": 30,
        "ping_timeout": 30,
    }

    try:
        # type: ignore[arg-type]
        async with ws_connect_legacy(uri, **kw) as ws:
            _log.info("WebSocket ✔ connected")

            while True:
                try:
                    raw = await asyncio.wait_for(ws.recv(), timeout=LISTEN_IDLE_TIMEOUT)
                except asyncio.TimeoutError:
                    _log.warning(
                        "No activity for %s s — closing WS", LISTEN_IDLE_TIMEOUT)
                    break

                if not raw:                       # ignore empty ping/pong frames
                    continue

                try:
                    payload: Dict[str, Any] = json.loads(raw)
                except json.JSONDecodeError:
                    _log.debug("Ignoring non-JSON frame: %r", raw[:60])
                    continue

                sink.append({"data": payload})

                if payload.get("type") == "endOfConversation":
                    _log.info("Bot ended the conversation — closing WS")
                    break

                for act in payload.get("activities", []):
                    if act.get("from", {}).get("id") == USER_ID:
                        continue  # skip echoes of our own msgs
                    _log.info(
                        "← %s: %s",
                        act.get("from", {}).get("name", "Bot"),
                        _short(_summarise_activity(act)),
                    )
    except websockets.exceptions.ConnectionClosedOK:
        _log.info("WebSocket closed gracefully")
    except Exception:
        _log.exception("WebSocket error")

# ──────────────────────────────  EXAMPLE  ─────────────────────────────── #


async def example_usage() -> None:
    start_dt = datetime.now()
    ts = start_dt.strftime("%Y%m%d_%H%M%S")

    run_data: Dict[str, Any] = {
        "runInfo": {
            "scriptStartTime": start_dt.isoformat(),
            "userId": USER_ID,
            "baseUrl": BASE_URL,
        },
        "conversationInfo": None,
        "sentActivities": [],
        "receivedActivitiesRaw": [],
    }

    output_path: Optional[str] = None
    ws_task: Optional[asyncio.Task[None]] = None

    try:
        # STEP 1 — start conversation with Direct Line secret
        async with AuthenticatedClient(
            base_url=BASE_URL,
            token=TOKEN,
            httpx_args={"event_hooks": {"request": [
                _log_req], "response": [_log_res]}},
            raise_on_unexpected_status=True,
        ) as client:
            _log.info("Creating conversation …")
            conv_res: Response[Conversation] = await conversations_start_conversation.asyncio_detailed(  # noqa: E501
                client=client,
                body=TokenParameters(),
            )
            parsed: Conversation | None
            conv: Conversation = cast(Conversation, conv_res.parsed)

        conv_id = cast(str, conv.conversation_id)
        conv_token = cast(str, conv.token)
        stream_url = cast(str, conv.stream_url)
        _log.info(
            "Conversation %s ready (token expires in %s s)",
            conv_id, conv.expires_in,
        )

        run_data["conversationInfo"] = conv.to_dict()
        output_dir = os.path.join(OUTPUT_DIR_BASE, conv_id)
        output_path = os.path.join(output_dir, f"{ts}_{conv_id}.json")
        run_data["runInfo"]["outputFile"] = output_path  # type: ignore[index]

        # STEP 2 — use the conversation-specific token for WS + sends
        async with AuthenticatedClient(
            base_url=BASE_URL,
            token=conv_token,
            httpx_args={"event_hooks": {"request": [
                _log_req], "response": [_log_res]}},
            raise_on_unexpected_status=True,
        ) as client:
            ws_task = asyncio.create_task(
                _ws_listener(stream_url, conv_token,
                             run_data["receivedActivitiesRaw"])
            )

            await asyncio.sleep(1)  # let WS connect

            async def _send(activity: Activity) -> Response[ResourceResponse]:
                """Send *activity* to the bot and return the HTTP envelope."""
                run_data["sentActivities"].append(activity.to_dict())
                return await conversations_post_activity.asyncio_detailed(
                    client=client,
                    conversation_id=conv_id,
                    body=activity,
                )

            # initial event
            await _send(
                Activity(
                    type_="event",
                    name="initialUserData",
                    value=ActivityValue.from_dict(
                        {
                            "userId": USER_ID,
                            "initialContext": "refactored_example",
                            "preferredLanguage": "en-US",
                            "isAuthenticated": False,
                        }
                    ),
                    from_=ChannelAccount(id=USER_ID),
                    locale="en-AU",
                )
            )
            _log.info("→ initialUserData event sent")

            # greeting message
            await _send(
                Activity(
                    type_="message",
                    from_=ChannelAccount(id=USER_ID),
                    text="👋 Hello from Python (minimal-log sample)!",
                    locale="en-AU",
                )
            )
            _log.info("→ greeting message sent")

            _log.info("Listening for bot replies …  (Ctrl-C to quit)")
            await ws_task
    except KeyboardInterrupt:
        _log.warning("Interrupted by user (Ctrl-C)")
    except Exception:
        _log.exception("Fatal error")
    finally:
        if ws_task and not ws_task.done():
            ws_task.cancel()
            with contextlib.suppress(asyncio.CancelledError):
                await ws_task

        if output_path and run_data.get("conversationInfo"):
            os.makedirs(os.path.dirname(output_path), exist_ok=True)
            with open(output_path, "w", encoding="utf-8") as f:
                json.dump(run_data, f, indent=2,
                          default=str, ensure_ascii=False)
            _log.info("Transcript saved → %s", output_path)
        _log.info("Done.")

# ─────────────────────────  CLI ENTRYPOINT  ───────────────────────────── #

if __name__ == "__main__":
    asyncio.run(example_usage())
