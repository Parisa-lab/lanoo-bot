"""
base.py

Shared Telegram utilities.

This module contains helper functions shared by all
Telegram messaging modules.

Responsibilities:

- Validate Telegram updates
- Retrieve effective message
- Retrieve effective chat
- Provide common logging helpers
"""

# ==========================================================
# Standard Library Imports
# ==========================================================

import logging

# ==========================================================
# Third-Party Imports
# ==========================================================

from telegram import Chat
from telegram import Message
from telegram import Update

# ==========================================================
# Logger
# ==========================================================

logger = logging.getLogger(__name__)


# ==========================================================
# Update Validation
# ==========================================================

def get_message(
    update: Update,
) -> Message | None:
    """
    Return the effective Telegram message.

    Args:
        update:
            Incoming Telegram update.

    Returns:
        Message or None.
    """

    if update.effective_message is None:

        logger.warning(
            "Telegram update does not contain an effective message."
        )

        return None

    return update.effective_message


def get_chat(
    update: Update,
) -> Chat | None:
    """
    Return the effective Telegram chat.

    Args:
        update:
            Incoming Telegram update.

    Returns:
        Chat or None.
    """

    if update.effective_chat is None:

        logger.warning(
            "Telegram update does not contain an effective chat."
        )

        return None

    return update.effective_chat


# ==========================================================
# Logging Helpers
# ==========================================================

def log_outgoing_message(
    chat_id: int | str,
    operation: str,
) -> None:
    """
    Log every outgoing Telegram operation.

    Args:
        chat_id:
            Telegram chat id.

        operation:
            Operation name.

    Returns:
        None.
    """

    logger.debug(
        "[Chat %s] %s",
        chat_id,
        operation,
    )


def log_invalid_update(
    operation: str,
) -> None:
    """
    Log invalid Telegram updates.

    Args:
        operation:
            Operation name.

    Returns:
        None.
    """

    logger.warning(
        "Cannot execute '%s' because the Telegram update is invalid.",
        operation,
    )