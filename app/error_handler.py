"""
error_handler.py

Global Telegram error handler.

This module catches every unhandled exception raised
inside the Telegram application and writes detailed
information into the application logs.
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
    Handle every unhandled exception.

    This function is automatically called by
    python-telegram-bot whenever an exception
    reaches the application level.

    Args:
        update:
            Telegram update that caused the error.

        context:
            Telegram callback context.

    Returns:
        None.
    """

    # ------------------------------------------------------
    # Log the exception itself.
    # ------------------------------------------------------

    logger.exception(
        "Unhandled exception occurred.",
        exc_info=context.error,
    )

    # ------------------------------------------------------
    # Build a complete Python traceback.
    # ------------------------------------------------------

    traceback_text = "".join(
        traceback.format_exception(
            None,
            context.error,
            context.error.__traceback__,
        )
    )

    # ------------------------------------------------------
    # Prepare Telegram update information.
    # ------------------------------------------------------

    update_information = "No update available."

    if isinstance(update, Update):

        update_information = html.escape(
            json.dumps(
                update.to_dict(),
                indent=4,
                ensure_ascii=False,
            )
        )

    # ------------------------------------------------------
    # Extract useful information from the update.
    # ------------------------------------------------------

    user_id = "Unknown"
    username = "Unknown"
    chat_id = "Unknown"
    message_text = "Unknown"

    if isinstance(update, Update):

        # Extract user information.
        if update.effective_user is not None:

            user_id = update.effective_user.id
            username = (
                update.effective_user.username
                or update.effective_user.full_name
            )

        # Extract chat information.
        if update.effective_chat is not None:

            chat_id = update.effective_chat.id

        # Extract received message.
        if (
            update.effective_message is not None
            and update.effective_message.text
        ):

            message_text = update.effective_message.text

    # ------------------------------------------------------
    # Write a detailed error report.
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
        "%s"
        "\n=====================================================",
        user_id,
        username,
        chat_id,
        message_text,
        update_information,
        traceback_text,
    )

    # ------------------------------------------------------
    # Future Improvements
    # ------------------------------------------------------
    #
    # Future versions may also:
    #
    # • Send the error report to the bot administrator.
    # • Store errors inside a database.
    # • Send notifications to Telegram or Discord.
    # • Report errors to services such as Sentry.