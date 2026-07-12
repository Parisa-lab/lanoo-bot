"""
help.py

Handle the /help command.

This module sends a help message describing how
users can interact with the bot.
"""

# Import Telegram update object.
from telegram import Update

# Import Telegram callback context.
from telegram.ext import ContextTypes

# Import the help message.
from app.messages import HELP_MESSAGE

# Import the message sender.
from app.telegram import send_message


async def help_handler(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
) -> None:
    """
    Handle the /help command.

    Args:
        update:
            Incoming Telegram update.

        context:
            Telegram callback context.

    Returns:
        None.
    """

    # The context parameter is currently unused.
    _ = context

    # Send the help message.
    await send_message(
        update=update,
        text=HELP_MESSAGE,
    )