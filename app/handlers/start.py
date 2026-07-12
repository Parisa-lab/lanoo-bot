"""
start.py

Handle the /start command.

This module contains the handler responsible for
welcoming users when they start the bot.
"""

# Import Telegram update object.
#
# Update contains all information received from Telegram,
# including messages, commands and callback queries.
from telegram import Update

# Import Telegram context types.
#
# ContextTypes provides type hints for the callback context.
from telegram.ext import ContextTypes

# Import the welcome message.
#
# All user-facing messages are stored inside messages.py.
from app.messages import WELCOME_MESSAGE


async def start_handler(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
) -> None:
    """
    Handle the /start command.

    This function is executed whenever a user sends
    the /start command.

    It sends a welcome message to the user.

    Args:
        update:
            Incoming Telegram update.

        context:
            Telegram callback context.

    Returns:
        None.
    """

    # The context parameter is not used yet.
    #
    # It will be used later for features such as:
    # - User data
    # - Conversation states
    # - Background jobs
    # - Bot data
    #
    # Assigning it to "_" tells linters that this
    # is intentional.
    _ = context

    # Make sure the update contains a message.
    #
    # Although Telegram usually sends a message for
    # commands, checking for None prevents unexpected
    # runtime errors.
    if update.message is None:
        return

    # Send the welcome message to the user.
    await update.message.reply_text(
        text=WELCOME_MESSAGE,
    )