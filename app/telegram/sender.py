"""
sender.py

Telegram messaging utilities.

Every outgoing message should pass through this module.

Benefits:

- Centralized message sending
- Consistent parse mode
- Automatic logging
- Easier future maintenance
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

# ==========================================================
# Logger
# ==========================================================

logger = logging.getLogger(__name__)


async def send_message(
    update: Update,
    text: str,
    *,
    parse_mode: str = ParseMode.HTML,
    disable_web_page_preview: bool = True,
) -> Message | None:
    """
    Send a message to the current chat.

    Args:
        update:
            Telegram update.

        text:
            Message text.

        parse_mode:
            Telegram parse mode.

        disable_web_page_preview:
            Disable link preview.

    Returns:
        Sent Message object or None.
    """

    # ------------------------------------------------------
    # Validate update.
    # ------------------------------------------------------

    if update.effective_message is None:

        logger.warning(
            "Cannot send message because effective_message is None."
        )

        return None

    # ------------------------------------------------------
    # Write debug log.
    # ------------------------------------------------------

    logger.debug(
        "Sending message to chat %s",
        update.effective_chat.id
        if update.effective_chat
        else "Unknown",
    )

    # ------------------------------------------------------
    # Send the message.
    # ------------------------------------------------------

    return await update.effective_message.reply_text(
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
    Edit an existing Telegram message.

    Args:
        message:
            Message to edit.

        text:
            New message text.

        parse_mode:
            Telegram parse mode.

        disable_web_page_preview:
            Disable link preview.

    Returns:
        Edited Telegram message.
    """

    # Write a debug log.
    logger.debug(
        "Editing message %s",
        message.message_id,
    )

    # Edit the message.
    return await message.edit_text(
        text=text,
        parse_mode=parse_mode,
        disable_web_page_preview=disable_web_page_preview,
    )


# ==========================================================
# Chat Actions
# ==========================================================

async def send_typing_action(
    update: Update,
) -> None:
    """
    Send the typing action to the current chat.

    Args:
        update:
            Telegram update.

    Returns:
        None.
    """

    # Validate chat.
    if update.effective_chat is None:
        return

    logger.debug(
        "Sending typing action."
    )

    await update.effective_chat.send_action(
        "typing",
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
# Error Messages
# ==========================================================

async def send_error_message(
    update: Update,
) -> Message | None:
    """
    Send a generic error message.

    Args:
        update:
            Telegram update.

    Returns:
        Sent message or None.
    """

    logger.warning(
        "Sending generic error message."
    )

    return await send_message(
        update=update,
        text=(
            "⚠️ An unexpected error occurred.\n\n"
            "Please try again later."
        ),
    )