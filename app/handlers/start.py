"""
start.py

Handle the /start Telegram command.

This module contains the function that is executed
when a user sends the /start command.
"""

# Import the Update class.
#
# Update represents everything Telegram sends to our bot.
#
# For example:
# - A message
# - A command
# - A photo
# - A button click
#
# In this file we only care about the /start command.
from telegram import Update


# Import ContextTypes.
#
# Context contains useful information and tools
# provided by the Telegram framework.
#
# We do not use it yet,
# but almost every handler receives it.
from telegram.ext import ContextTypes


# Import the welcome message.
#
# All user-facing messages are stored inside messages.py.
#
# This keeps the code clean and makes future translation easier.
from app.messages import WELCOME_MESSAGE


# Create the function that handles the /start command.
#
# "async" allows the bot to handle many users efficiently
# without blocking while waiting for Telegram's response.
async def start(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
) -> None:
    """
    Handle the /start command.

    Args:
        update:
            Information about the incoming Telegram update.

        context:
            Extra data provided by the Telegram framework.

    Returns:
        None
    """

    # Prevent IDE and linter warnings.
    #
    # We don't use "context" yet,
    # but we will use it later.
    _ = context

    # Make sure a message actually exists.
    #
    # This is a safety check.
    # Normally /start always has a message,
    # but defensive programming is a good habit.
    if update.message is None:
        return

    # Send the welcome message to the user.
    #
    # reply_text() sends a normal text message
    # back to the same chat.
    await update.message.reply_text(
        text=WELCOME_MESSAGE
    )