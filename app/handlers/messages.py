"""
messages.py

Store all user-facing messages in one place.

Keeping messages separate from the business logic makes
the project easier to maintain, translate, and extend.
"""


# ---------------------------------------------------------------------
# Welcome Messages
# ---------------------------------------------------------------------

WELCOME_MESSAGE = (
    "👋 Welcome to Lanoo!\n\n"
    "Your smart assistant for comparing prices of baby "
    "and family products.\n\n"
    "Use /help to see the available commands."
)


# ---------------------------------------------------------------------
# Help Messages
# ---------------------------------------------------------------------

HELP_MESSAGE = (
    "Available commands:\n\n"
    "/start - Start the bot\n"
    "/help - Show this help message\n"
    "/price - Search for a product price"
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