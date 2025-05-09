#!/usr/bin/env python
# coding: utf‑8
"""
conversation_activity_viewer.py: Fetches Direct Line activities for a specified
conversation using the Direct Line Secret, writes them to a JSON file,
and shows a detailed, colourised console log. Also saves all console output to a log file.
"""

from __future__ import annotations

import asyncio
import json
import os
import argparse
import sys
from typing import Any, Union, cast, Optional, List, Dict, Tuple
from datetime import datetime, timezone, tzinfo as TzInfo

from dotenv import load_dotenv
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.syntax import Syntax
from rich.text import Text
from rich.markup import escape
import rich.errors  # For MarkupError type hint in robust_json_default
import httpx  # For exception handling

from directline_client import AuthenticatedClient
from directline_client.api.conversations import conversations_get_activities
from directline_client.models.activity import Activity
from directline_client.models.activity_set import ActivitySet
from directline_client.models.channel_account import ChannelAccount
from directline_client.types import Response, UNSET, Unset

# --------------------------------------------------------------------------- #
#                           CONFIGURATION & CONSTANTS                         #
# --------------------------------------------------------------------------- #
OUTPUT_DIR: str = "conversation_activities"
LOG_FILE_BASENAME: str = "cav_log"  # Conversation Activity Viewer Log

# Ensure output directory exists early
try:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
except OSError as e:
    print(f"Fatal: Could not create output directory {OUTPUT_DIR}: {e}")
    sys.exit(1)

# Initialize Rich Console for recording
console: Console = Console(highlight=False, record=True, width=120)

load_dotenv()

# Direct Line Secret is mandatory
DIRECT_LINE_SECRET: str = os.getenv("DIRECT_LINE_SECRET", "")
if not DIRECT_LINE_SECRET:
    console.print("[bold red]Error: Direct Line secret not found.[/bold red]")
    console.print(
        "Please set the DIRECT_LINE_SECRET environment variable (e.g., in a .env file)."
    )
    # Attempt to save log even for this early exit
    _timestamp_str_error = datetime.now().strftime('%Y%m%d_%H%M%S')
    _error_log_path = os.path.join(
        OUTPUT_DIR, f"{LOG_FILE_BASENAME}_directline_secret_error_{_timestamp_str_error}.txt")
    try:
        console.save_text(_error_log_path)
        print(
            f"Early exit error log saved to: {os.path.abspath(_error_log_path)}", flush=True)
    except Exception as e_save_log:
        print(
            f"Error saving early exit log to {_error_log_path}: {e_save_log}", flush=True)
    sys.exit(1)

BASE_URL: str = os.getenv("DL_BASE_URL", "https://directline.botframework.com")

# --------------------------------------------------------------------------- #
#                               UTILITY FUNCTIONS                             #
# --------------------------------------------------------------------------- #


def _sanitize_for_filename(name: str) -> str:
    """Sanitizes a string to be filesystem-friendly."""
    return "".join(c if c.isalnum() or c in ('_', '-') else '_' for c in name)


def save_recorded_output(console_instance: Console, id_for_filename: Optional[str] = "session") -> None:
    """Saves the recorded console output to a text file."""
    timestamp_str: str = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename_parts: List[str] = [LOG_FILE_BASENAME]

    if id_for_filename:
        safe_id_for_filename: str = _sanitize_for_filename(id_for_filename)
        filename_parts.append(safe_id_for_filename)

    filename_parts.append(timestamp_str)
    log_filename: str = f"{'_'.join(filename_parts)}.txt"
    log_path: str = os.path.join(OUTPUT_DIR, log_filename)
    log_path_abs: str = os.path.abspath(log_path)

    print(f"\nAttempting to save console log to: {log_path_abs}", flush=True)
    try:
        console_instance.save_text(log_path)
        print(f"Console log successfully saved to: {log_path_abs}", flush=True)
    except Exception as e_save_log:
        print(
            f"Error saving console log to {log_path_abs}: {e_save_log}", flush=True)

# --------------------------------------------------------------------------- #
#                         JSON SERIALIZATION HELPER                           #
# --------------------------------------------------------------------------- #


def robust_json_default(obj: Any) -> Any:
    """
    A robust JSON default serializer that handles Rich Text objects,
    datetime, and Unset types.
    """
    if isinstance(obj, Text):
        try:
            # str(Text_obj) calls Text_obj.plain, which can raise MarkupError
            return str(obj)
        except rich.errors.MarkupError:
            plain_text: str = ""
            if hasattr(obj, '_text') and isinstance(obj._text, list):
                # type: ignore # _text is List[Tuple[str, Optional[Style]]]
                for segment_text, _ in obj._text:
                    plain_text += segment_text
            else:
                plain_text = f"[Unserializable Rich Text Object: type {type(obj).__name__}]"
            return plain_text
    elif isinstance(obj, datetime):
        if obj.tzinfo is None:
            return obj.replace(tzinfo=timezone.utc).isoformat()
        return obj.isoformat()
    elif obj is UNSET or isinstance(obj, Unset):
        return None  # Represent UNSET as null in JSON
    try:
        return str(obj)
    except Exception as e:
        raise TypeError(
            f"Object of type {obj.__class__.__name__} is not JSON serializable and str() failed: {e}")

# --------------------------------------------------------------------------- #
#                         ACTIVITY PRETTY PRINTER                             #
# --------------------------------------------------------------------------- #


def format_timestamp(ts: Union[datetime, Unset, None]) -> Text:
    """Formats a timestamp for display, handling Unset and None."""
    if not isinstance(ts, datetime):
        return Text("N/A", style="dim")
    try:
        current_tz: Optional[TzInfo] = ts.tzinfo
        aware_ts: datetime
        if current_tz is None or current_tz.utcoffset(ts) is None:
            aware_ts = ts.replace(tzinfo=timezone.utc)
        else:
            aware_ts = ts
        local_ts: datetime = aware_ts.astimezone()
        return Text(local_ts.strftime('%Y-%m-%d %H:%M:%S %Z'), style="cyan dim")
    except Exception:  # pylint: disable=broad-except
        return Text(str(ts), style="red dim")  # Fallback for unexpected errors


def format_value(val: Any) -> Union[str, Syntax, Text]:
    """Formats a generic value for display, handling dicts/lists as JSON."""
    if val is UNSET or val is None:
        return Text("N/A", style="dim")
    if isinstance(val, (dict, list)):
        try:
            json_str: str = json.dumps(
                val, indent=2, ensure_ascii=False, default=robust_json_default
            )
            return Syntax(json_str, "json", theme="material", line_numbers=False, word_wrap=True)
        except Exception:  # pylint: disable=broad-except
            return str(val)  # Fallback to plain string
    return str(val)


def display_activity(activity: Activity, index: int) -> None:
    """Displays a single activity in a Rich Panel."""
    act_type: str = "UNKNOWN"
    if activity.type_ is not UNSET and activity.type_ is not None:
        act_type = str(activity.type_).upper()

    from_id: str = "N/A"
    role: str = "n/a"
    if activity.from_ is not UNSET and activity.from_ is not None:
        # activity.from_ is type ChannelAccount | Unset | None
        channel_account: ChannelAccount = cast(ChannelAccount, activity.from_)
        if channel_account.id is not UNSET and channel_account.id is not None:
            from_id = str(channel_account.id)

        role_attr = channel_account.role
        if role_attr is not UNSET and role_attr is not None:
            role = str(role_attr).lower()

    panel_title_style: str = "bold magenta"
    content_color: str = "white"
    from_style: str = "dim"

    if act_type == "MESSAGE":
        if role == "user":
            panel_title_style, content_color, from_style = "bold yellow", "yellow", "yellow"
        elif role == "bot":
            panel_title_style, content_color, from_style = "bold green", "green", "green"
    elif act_type == "EVENT":
        panel_title_style, content_color, from_style = "bold blue", "blue", "blue"
    elif act_type == "INVOKE":
        panel_title_style, content_color, from_style = "bold bright_cyan", "bright_cyan", "bright_cyan"
    elif act_type == "CONVERSATIONUPDATE":
        panel_title_style = "bold bright_magenta"
    elif act_type == "TYPING":
        panel_title_style = "dim"

    title_text: Text = Text.assemble(
        (f"#{index + 1} ", "bold dim"), (f"{act_type} ", panel_title_style),
        ("from ", "dim"), (escape(from_id), from_style),
        (f" ({escape(role)})" if role != "n/a" else "", f"{from_style} dim")
    )

    grid: Table = Table.grid(expand=True, padding=(0, 1))
    grid.add_column(style="dim italic", width=15)  # Label column
    grid.add_column()  # Value column

    grid.add_row("ID:", Text(str(activity.id) if activity.id not in (
        UNSET, None) else "N/A", style="cyan dim"))
    grid.add_row("Timestamp:", format_timestamp(activity.timestamp))

    has_substantive_content: bool = False
    if activity.name not in (UNSET, None):
        grid.add_row("Name:", Text(str(activity.name), style=content_color))
        has_substantive_content = True
    if activity.text not in (UNSET, None):
        grid.add_row("Text:", Text(str(activity.text), style=content_color))
        has_substantive_content = True
    if activity.locale not in (UNSET, None):
        grid.add_row("Locale:", Text(str(activity.locale), style="dim"))
        has_substantive_content = True  # Locale can be important content
    if activity.input_hint not in (UNSET, None):
        grid.add_row("Input Hint:", Text(
            str(activity.input_hint), style="dim"))
    if activity.reply_to_id not in (UNSET, None):
        grid.add_row("ReplyTo ID:", Text(
            str(activity.reply_to_id), style="dim"))

    if activity.value not in (UNSET, None):
        value_data: Any = getattr(
            activity.value, 'additional_properties', activity.value)
        grid.add_row("Value:", format_value(value_data))
        has_substantive_content = True

    if not has_substantive_content and act_type not in ("TYPING", "CONVERSATIONUPDATE"):
        grid.add_row("Details:", Text(
            "(Minimal activity content)", style="dim italic"))

    console.print(Panel(grid, title=title_text,
                  border_style=panel_title_style, expand=False, padding=(1, 2)))
    console.line()

# --------------------------------------------------------------------------- #
#                                MAIN TASK                                    #
# --------------------------------------------------------------------------- #


async def view_conversation_activities(
    conversation_id: str,
    user_id: Optional[str],
    watermark: Optional[str]
) -> None:
    """Fetches, displays, and saves conversation activities."""
    console.rule(
        "[bold sky_blue1]Direct Line Activity Viewer[/bold sky_blue1]")
    console.print(
        f"[dim]Conversation ID :[/dim] [bold cyan]{escape(conversation_id)}[/bold cyan]")
    if user_id:
        console.print(
            f"[dim]User ID (info)  :[/dim] [cyan]{escape(user_id)}[/cyan]")
    if watermark:
        console.print(
            f"[dim]Watermark (req) :[/dim] [cyan]{escape(watermark)}[/cyan]")
    console.print(
        f"[dim]Using Base URL  :[/dim] [blue]{escape(BASE_URL)}[/blue]")
    console.print(
        f"[dim]Output Dir      :[/dim] [blue]{escape(OUTPUT_DIR)}[/blue]")
    console.line()

    activities_list: List[Activity] = []
    new_watermark: Optional[str] = None

    try:
        async with AuthenticatedClient(
            base_url=BASE_URL, token=DIRECT_LINE_SECRET, raise_on_unexpected_status=False,
        ) as client:
            console.print("[yellow]Attempting to fetch activities...[/yellow]")

            watermark_arg: Union[str,
                                 Unset] = watermark if watermark else UNSET
            response: Response[Union[ActivitySet, Any]] = await conversations_get_activities.asyncio_detailed(
                client=client, conversation_id=conversation_id, watermark=watermark_arg,
            )

            if 200 <= response.status_code < 300:
                console.print(
                    f"[green]Successfully fetched activity set (HTTP {response.status_code}).[/green]")
                activities_data: ActivitySet = cast(
                    ActivitySet, response.parsed)

                _fetched_activities: Union[List[Activity],
                                           Unset, None] = activities_data.activities
                if isinstance(_fetched_activities, list):
                    activities_list = _fetched_activities

                _fetched_watermark: Union[str, Unset,
                                          None] = activities_data.watermark
                if _fetched_watermark is not UNSET and _fetched_watermark is not None:
                    new_watermark = str(_fetched_watermark)

                timestamp_str: str = datetime.now().strftime('%Y%m%d_%H%M%S')
                safe_conv_id: str = _sanitize_for_filename(conversation_id)
                filename: str = f"{safe_conv_id}_{timestamp_str}_activities.json"
                out_path: str = os.path.join(OUTPUT_DIR, filename)

                try:
                    with open(out_path, "w", encoding="utf-8") as fp:
                        dict_data: Dict[str, Any] = activities_data.to_dict()
                        json.dump(dict_data, fp, ensure_ascii=False,
                                  indent=2, default=robust_json_default)

                    abs_path_for_link: str = os.path.abspath(out_path)
                    console.print(
                        f"[dim]Saved raw JSON to:[/dim] [green link='file://{abs_path_for_link}']{escape(out_path)}[/green]"
                    )
                except Exception as e_save:  # pylint: disable=broad-except
                    console.print(
                        f"[red]Error saving JSON to {escape(out_path)}: {escape(str(e_save))}[/red]")
            else:
                console.print(
                    f"[bold red]Error fetching activities (HTTP {response.status_code}):[/bold red]")
                try:
                    error_content: str = response.content.decode(
                        errors='replace')
                    # Attempt to pretty-print if JSON, otherwise show raw
                    try:
                        parsed_error_content: Any = json.loads(error_content)
                        pretty_error_content: str = json.dumps(
                            parsed_error_content, indent=2, default=robust_json_default)
                        console.print(Syntax(
                            pretty_error_content, "json", theme="material", line_numbers=False, word_wrap=True))
                    except json.JSONDecodeError:
                        # Show as plain text if not JSON
                        console.print(Text(error_content))
                except Exception:  # pylint: disable=broad-except
                    console.print(
                        f"[red]{escape(str(response.content))}[/red]")
                return

    except httpx.HTTPStatusError as e_http:
        console.print(
            f"[bold red]HTTP Status Error: {escape(str(e_http.response.status_code))}[/bold red]")
        error_text: str = e_http.response.text
        try:
            parsed_error: Any = json.loads(error_text)
            console.print(Syntax(json.dumps(parsed_error, indent=2), "json",
                          theme="material", line_numbers=False, word_wrap=True))
        except json.JSONDecodeError:
            console.print(escape(error_text))
        return
    except httpx.RequestError as e_req:
        console.print(
            f"[bold red]Request Error: {escape(str(e_req))}[/bold red]")
        console.print(
            f"Could not connect to {escape(str(e_req.request.url))}. Check network or BASE_URL.")
        return
    except Exception:  # pylint: disable=broad-except
        console.print("[bold red]An unexpected error occurred:[/bold red]")
        console.print_exception()  # show_locals defaults to False, cleaner for console
        return

    console.line()
    if activities_list:
        console.print(
            f"[bold]Displaying {len(activities_list)} activities:[/bold]")
        console.line()
        for i, activity_item in enumerate(activities_list):
            display_activity(activity_item, i)
    else:
        console.print("[yellow]No activities found in this set.[/yellow]")

    console.line()
    if new_watermark:
        console.print(
            f"[dim]New Watermark for next fetch:[/dim] [bold cyan]{escape(new_watermark)}[/bold cyan]")
    else:
        console.print(
            "[dim]No new watermark received in this activity set.[/dim]")
    console.rule(style="sky_blue1")

# --------------------------------------------------------------------------- #
#                                   ENTRY                                     #
# --------------------------------------------------------------------------- #
if __name__ == "__main__":
    log_file_identifier: str = "startup"

    parser: argparse.ArgumentParser = argparse.ArgumentParser(
        description="Fetch and display Direct Line conversation activities using Direct Line Secret.",
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument(
        "conversation_id", type=str, help="The specific Conversation ID to fetch activities for.")
    parser.add_argument(
        "-u", "--user-id", type=str, required=False,
        help="Optional User ID associated with the conversation (for informational purposes).")
    parser.add_argument(
        "-w", "--watermark", type=str, required=False,
        help="Optional watermark to get activities since the last fetch.")

    try:
        args: argparse.Namespace = parser.parse_args()
        log_file_identifier = args.conversation_id if args.conversation_id else "no_conv_id"

        asyncio.run(view_conversation_activities(
            args.conversation_id, args.user_id, args.watermark
        ))

    except SystemExit as e_sys_exit:
        # Argparse handles help printing. If error (non-zero code), log our message.
        if e_sys_exit.code != 0:
            console.print(
                f"[bold red]SystemExit: Argument parsing error (Exit code {e_sys_exit.code}).[/bold red]")
        # Re-raise to allow proper exit and message display by argparse
        raise
    except KeyboardInterrupt:
        console.print("\n[yellow]Operation interrupted by user.[/yellow]")
    except Exception:  # pylint: disable=broad-except
        console.print(
            "\n[bold red]A critical error occurred in main execution:[/bold red]")
        console.print_exception()
    finally:
        save_recorded_output(console, log_file_identifier)
