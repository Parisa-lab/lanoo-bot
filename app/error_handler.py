"""
error_handler.py

Global Telegram error handler.

This module logs every unhandled exception that
occurs while processing Telegram updates.
"""

import html
import json
import logging
import traceback

from telegram import Update
from telegram.ext import ContextTypes

logger = logging.getLogger(__name__)


async def error_handler(
    update: object,
    context: ContextTypes.DEFAULT_TYPE,
) -> None:
    """
    Handle every unhandled exception.
    """

    logger.exception(
        "Unhandled exception:",
        exc_info=context.error,
    )

    error_trace = "".join(
        traceback.format_exception(
            None,
            context.error,
            context.error.__traceback__,
        )
    )

    update_json = ""

    if isinstance(update, Update):
        update_json = html.escape(
            json.dumps(
                update.to_dict(),
                indent=2,
                ensure_ascii=False,
            )
        )

    logger.error(
        "\n"
        "================ ERROR ================\n"
        "Telegram Update:\n%s\n\n"
        "Traceback:\n%s\n"
        "=======================================",
        update_json,
        error_trace,
    )