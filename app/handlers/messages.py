"""
messages.py

Store every message shown to users.

Keeping messages separate from the application logic
makes future maintenance much easier.

If we decide to support multiple languages later,
only this file will need major changes.
"""

from app.constants import BOT_NAME


# ---------------------------------------------------------------------
# Welcome Messages
# ---------------------------------------------------------------------

WELCOME_MESSAGE = (
    f"👋 Welcome to {BOT_NAME}!\n\n"
    "Your smart assistant for comparing prices "
    "of baby and family products.\n\n"
    "Type /help to see available commands."
)


# ---------------------------------------------------------------------
# Help Messages
# ---------------------------------------------------------------------

HELP_MESSAGE = (
    "Available commands\n\n"

    "/start - Start the bot\n"

    "/help - Show help information\n"

    "/price - Search product prices"
)


# ---------------------------------------------------------------------
# Error Messages
# ---------------------------------------------------------------------

UNKNOWN_COMMAND = (
    "Sorry, I don't recognize that command."
)


INTERNAL_ERROR = (
    "Something went wrong.\n"
    "Please try again later."
)