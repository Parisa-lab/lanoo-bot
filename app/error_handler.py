"""
error_handler.py

Global Telegram error handler.
"""

# ==========================================================
# Standard Library Imports
# ==========================================================

import html
import json
import logging
import traceback

# ==========================================================
# Third-Party Imports
# ==========================================================

from telegram import Update
from telegram.error import Conflict
from telegram.ext import ContextTypes

# ==========================================================
# Logger
# ==========================================================

logger = logging.getLogger(__name__)


async def error_handler(
    update: object,
    context: ContextTypes.DEFAULT_TYPE,
) -> None:
    """
    Global application error handler.

    This function catches every unhandled exception
    raised by python-telegram-bot.
    """

    # ------------------------------------------------------
    # Handle Telegram polling conflicts separately.
    # ------------------------------------------------------

    if isinstance(
        context.error,
        Conflict,
    ):
        logger.warning(
            "Another bot instance is already running."
        )
        return

    # ------------------------------------------------------
    # Log exception.
    # ------------------------------------------------------

    logger.exception(
        "Unhandled exception occurred.",
        exc_info=context.error,
    )

    # ------------------------------------------------------
    # Build traceback.
    # ------------------------------------------------------

    traceback_text = "".join(
        traceback.format_exception(
            None,
            context.error,
            context.error.__traceback__,
        )
    )

    # ------------------------------------------------------
    # Extract update information.
    # ------------------------------------------------------

    update_information = "No update available."

    if isinstance(
        update,
        Update,
    ):
        try:

            update_information = html.escape(
                json.dumps(
                    update.to_dict(),
                    indent=4,
                    ensure_ascii=False,
                )
            )

        except Exception:

            update_information = (
                "Failed to serialize update."
            )

    # ------------------------------------------------------
    # Extract user information.
    # ------------------------------------------------------

    user_id = "Unknown"
    username = "Unknown"
    chat_id = "Unknown"
    message_text = "Unknown"

    if isinstance(
        update,
        Update,
    ):

        if update.effective_user is not None:

            user_id = (
                update.effective_user.id
            )

            username = (
                update.effective_user.username
                or update.effective_user.full_name
            )

        if update.effective_chat is not None:

            chat_id = (
                update.effective_chat.id
            )

        if (
            update.effective_message
            and update.effective_message.text
        ):

            message_text = (
                update.effective_message.text
            )

    # ------------------------------------------------------
    # Build error report.
    # ------------------------------------------------------

    logger.error(
        "\n"
        "=====================================================\n"
        "UNHANDLED APPLICATION ERROR\n"
        "=====================================================\n"
        "User ID      : %s\n"
        "Username     : %s\n"
        "Chat ID      : %s\n"
        "Message      : %s\n\n"
        "Telegram Update\n"
        "-----------------------------------------------------\n"
        "%s\n\n"
        "Python Traceback\n"
        "-----------------------------------------------------\n"
        "%s\n"
        "=====================================================",
        user_id,
        username,
        chat_id,
        message_text,
        update_information,
        traceback_text,
    )