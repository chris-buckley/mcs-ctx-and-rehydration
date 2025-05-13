import logging
import os
from typing import List, Optional

from rich.logging import RichHandler

DEFAULT_MAX_LOG_TEXT_LEN: int = 80

def setup_logger(
    logger_name: str = "app",
    log_level_override: Optional[int] = None,
    debug_mode: Optional[bool] = None,
    rich_markup: bool = True,
    show_path: bool = True,
    enable_httpx_logging: bool = True,
    keywords: Optional[List[str]] = None,
) -> logging.Logger:

    if debug_mode is None:
        debug_mode_env = os.getenv("LOG_DEBUG_MODE", "false")
        effective_debug_mode = debug_mode_env.lower() == "true"
    else:
        effective_debug_mode = debug_mode

    if log_level_override is not None:
        effective_log_level = log_level_override
    else:
        effective_log_level = logging.DEBUG if effective_debug_mode else logging.INFO

    logger = logging.getLogger(logger_name)
    logger.setLevel(effective_log_level)

    if logger.hasHandlers():
        logger.handlers.clear()

    handler = RichHandler(
        rich_tracebacks=True,
        show_time=True,
        show_level=True,
        show_path=show_path if effective_debug_mode else False,
        markup=rich_markup,
        keywords=keywords if keywords else [],
        tracebacks_show_locals=effective_debug_mode,
        log_time_format="[%X]",
    )

    logger.addHandler(handler)
    logger.propagate = False

    if effective_debug_mode and enable_httpx_logging:
        httpx_logger = logging.getLogger("httpx")
        if not httpx_logger.handlers:
            httpx_logger.addHandler(handler)
        httpx_logger.setLevel(logging.DEBUG)
        httpx_logger.propagate = False

    return logger

def truncate_text(
    text: str,
    limit: int = DEFAULT_MAX_LOG_TEXT_LEN,
    is_debugging: bool = False,
    ellipsis_char: str = "\u2026",
) -> str:
    if is_debugging or not limit or len(text) <= limit:
        return text
    return text[: limit - 1] + ellipsis_char