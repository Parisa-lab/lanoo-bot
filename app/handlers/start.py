"""
start.py

Handle the /start command.

This module contains the handler responsible for
welcoming new users when they start the bot.
"""

# Import Telegram classes.
#
# Update contains information about the incoming
# Telegram update.
from telegram import Update

# ContextTypes provides the correct type hints
# for the callback context.
from telegram.ext import ContextTypes

# Import the welcome message.
#
# All user-facing messages are stored inside
# messages.py.
from app.messages import WELCOME_MESSAGE


async def start_handler(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
) -> None:
    """
    Handle the /start command.

    This function sends the welcome message
    to the user.

    Args:
        update:
            Incoming Telegram update.

        context:
            Telegram callback context.

    Returns:
        None.
    """

    # The Update object normally contains a Message
    # when the user sends a command.
    #
    # This check prevents unexpected runtime errors
    # if the update does not include a message.
    if update.message is None:
        return

    # Send the welcome message.
    await update.message.reply_text(
        text=WELCOME_MESSAGE,
    )