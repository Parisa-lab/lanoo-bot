"""
sender.py

Telegram text messaging utilities.

Every outgoing text message should pass through this
module.

Benefits:

- Centralized message sending
- Consistent formatting
- Consistent logging
- Easier maintenance
- Easier future enhancements
"""

# ==========================================================
# Standard Library Imports
# ==========================================================

import logging

# ==========================================================
# Third-Party Imports
# ==========================================================

from telegram import Message
from telegram import Update
from telegram.constants import ParseMode
from telegram.constants import ChatAction


# ==========================================================
# Local Imports
# ==========================================================

from app.telegram.base import (
    get_chat,
    get_message,
    log_invalid_update,
    log_outgoing_message,
)

# ==========================================================
# Logger
# ==========================================================

logger = logging.getLogger(__name__)

# ==========================================================
# Text Messages
# ==========================================================

async def send_message(
    update: Update,
    text: str,
    *,
    parse_mode: str = ParseMode.HTML,
    disable_web_page_preview: bool = True,
) -> Message | None:
    """
    Send a text message.

    Args:
        update:
            Telegram update.

        text:
            Message text.

        parse_mode:
            Telegram parse mode.

        disable_web_page_preview:
            Disable link previews.

    Returns:
        Message or None.
    """

    # Get Telegram message.
    message = get_message(update)

    # Validate update.
    if message is None:

        log_invalid_update(
            "send_message",
        )

        return None

    # Get chat information.
    chat = get_chat(update)

    # Write debug log.
    log_outgoing_message(
        chat.id if chat else "Unknown",
        "send_message",
    )

    # Send message.
    return await message.reply_text(
        text=text,
        parse_mode=parse_mode,
        disable_web_page_preview=disable_web_page_preview,
    )


# ==========================================================
# Message Editing
# ==========================================================

async def edit_message(
    message: Message,
    text: str,
    *,
    parse_mode: str = ParseMode.HTML,
    disable_web_page_preview: bool = True,
) -> Message:
    """
    Edit an existing message.

    Args:
        message:
            Telegram message.

        text:
            New text.

        parse_mode:
            Telegram parse mode.

        disable_web_page_preview:
            Disable link previews.

    Returns:
        Edited Telegram message.
    """

    logger.debug(
        "Editing message %s",
        message.message_id,
    )

    return await message.edit_text(
        text=text,
        parse_mode=parse_mode,
        disable_web_page_preview=disable_web_page_preview,
    )


# ==========================================================
# Typing Action
# ==========================================================

async def send_typing_action(
    update: Update,
) -> None:
    """
    Send typing action.

    Args:
        update:
            Telegram update.

    Returns:
        None.
    """

    # Get chat.
    chat = get_chat(update)

    # Validate update.
    if chat is None:

        log_invalid_update(
            "send_typing_action",
        )

        return

    # Write debug log.
    log_outgoing_message(
        chat.id,
        "typing",
    )

    await chat.send_action(
       ChatAction.TYPING,
    )


# ==========================================================
# Message Deletion
# ==========================================================

async def delete_message(
    message: Message,
) -> None:
    """
    Delete a Telegram message.

    Args:
        message:
            Telegram message.

    Returns:
        None.
    """

    logger.debug(
        "Deleting message %s",
        message.message_id,
    )

    await message.delete()


# ==========================================================
# Standard Messages
# ==========================================================

async def send_error_message(
    update: Update,
    text: str | None = None,
) -> Message | None:
    """
    Send an error message.

    Args:
        update:
            Telegram update.

        text:
            Optional custom error text.

    Returns:
        Message or None.
    """

    return await send_message(
        update=update,
        text=text or (
            "❌ An unexpected error occurred.\n"
            "Please try again later."
        ),
    )


async def send_success_message(
    update: Update,
    text: str,
) -> Message | None:
    """
    Send a success message.

    Args:
        update:
            Telegram update.

        text:
            Success message.

    Returns:
        Message or None.
    """

    return await send_message(
        update=update,
        text=f"✅ {text}",
    )


async def send_warning_message(
    update: Update,
    text: str,
) -> Message | None:
    """
    Send a warning message.

    Args:
        update:
            Telegram update.

        text:
            Warning message.

    Returns:
        Message or None.
    """

    return await send_message(
        update=update,
        text=f"⚠️ {text}",
    )


async def send_info_message(
    update: Update,
    text: str,
) -> Message | None:
    """
    Send an informational message.

    Args:
        update:
            Telegram update.

        text:
            Information text.

    Returns:
        Message or None.
    """

    return await send_message(
        update=update,
        text=f"ℹ️ {text}",
    )