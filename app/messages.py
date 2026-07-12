"""
messages.py

Store all user-facing messages.

This module contains every text shown to users.

Keeping messages separate from the application logic
makes the project easier to maintain, translate,
and update.
"""

# Import application constants.
#
# The bot name is defined in one place
# so we never hardcode it.
from app.constants import BOT_NAME


# ==========================================================
# Welcome Messages
# ==========================================================

# Message displayed when the user sends /start.
#
# The f-string allows us to insert the bot name
# automatically.
WELCOME_MESSAGE = (
    f"👋 Welcome to {BOT_NAME}!\n\n"
    "Your smart assistant for comparing prices of "
    "baby and family products.\n\n"
    "Use /help to see the available commands."
)


# ==========================================================
# Help Messages
# ==========================================================

# Message displayed when the user sends /help.
HELP_MESSAGE = (
    "Available commands:\n\n"
    "/start - Start the bot\n"
    "/help - Show this help message\n"
    "/price - Search product prices"
)


# ==========================================================
# Error Messages
# ==========================================================

# Message displayed when the user enters
# an unsupported command.
UNKNOWN_COMMAND_MESSAGE = (
    "Sorry, I don't recognize that command."
)


# Message displayed when an unexpected error occurs.
INTERNAL_ERROR_MESSAGE = (
    "Something went wrong.\n"
    "Please try again later."
)