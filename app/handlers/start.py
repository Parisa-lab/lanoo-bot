"""
start.py

This module handles the /start command.

Every time a user sends /start,
the function inside this file will be executed.
"""

# Import the Update class.
#
# Update represents a single event received from Telegram.
#
# An event can be:
# - A message
# - A command
# - A button click
# - A photo
# - A document
#
# In this project we mainly receive messages.
from telegram import Update


# Import ContextTypes.
#
# Context gives our function access
# to useful information provided
# by python-telegram-bot.
#
# We do not need it yet,
# but we include it because
# almost every handler uses it.
from telegram.ext import ContextTypes


# Create a function that handles the /start command.
#
# async means this function runs asynchronously.
#
# Telegram bots spend a lot of time waiting
# for network responses.
#
# Using async allows the bot
# to serve many users efficiently.
async def start(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
) -> None:
    """
    Handle the /start command.

    Args:
        update:
            Information about the current Telegram update.

        context:
            Extra data provided by the Telegram framework.

    Returns:
        None
    """

    # Create the welcome message.
    #
    # Keeping the message inside a variable
    # makes the code easier to read.
    #
    # Later we will move all messages
    # into messages.py.
    welcome_message = (
        "👋 Welcome to Lanoo!\n\n"
        "Lanoo helps you compare prices "
        "for baby and family products.\n\n"
        "More features are coming soon."
    )

    # Send the welcome message
    # back to the same chat
    # where the command was received.
    #
    # update.message represents
    # the incoming Telegram message.
    #
    # reply_text() sends a text message.
    await update.message.reply_text(
        welcome_message
    ) 