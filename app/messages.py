"""
messages.py

Store all user-facing messages.

This module contains every message shown to users.

Keeping messages in a dedicated module has several
advantages:

- The application logic stays clean.
- Messages can be updated without changing handlers.
- Adding multiple languages becomes much easier.
- All user-facing text is stored in one place.
"""

# Import application constants.
#
# The bot name is defined in one place so it is
# never hardcoded throughout the project.
from app.constants import BOT_NAME


# ==========================================================
# Welcome Messages
# ==========================================================

# Message displayed when the user starts the bot.
#
# The bot name is inserted automatically using
# an f-string.
WELCOME_MESSAGE = (
    f"👋 Welcome to {BOT_NAME}!\n\n"
    "Your smart assistant for comparing prices of "
    "baby and family products.\n\n"
    "Use /help to see the available commands."
)


# ==========================================================
# Help Messages
# ==========================================================

# Message displayed when the user requests help.
#
# This message should always reflect the currently
# supported Telegram commands.
HELP_MESSAGE = (
    "Available commands:\n\n"
    "/start - Start the bot\n"
    "/help - Show this help message\n"
    "/price - Search product prices"
)


# ==========================================================
# Price Search Messages
# ==========================================================

# Ask the user to enter a product name.
ASK_PRODUCT_NAME_MESSAGE = (
    "Please enter the product name you want to search for."
)


# Displayed while the bot is searching.
SEARCHING_MESSAGE = (
    "Searching for the best prices..."
)


# Displayed when no products are found.
NO_PRODUCTS_FOUND_MESSAGE = (
    "No matching products were found."
)


# ==========================================================
# Error Messages
# ==========================================================

# Displayed when the user sends
# an unsupported command.
UNKNOWN_COMMAND_MESSAGE = (
    "Sorry, I don't recognize that command."
)


# Displayed when something unexpected happens.
INTERNAL_ERROR_MESSAGE = (
    "Something went wrong.\n"
    "Please try again later."
)


# Displayed when the user's input
# is not valid.
INVALID_INPUT_MESSAGE = (
    "The information you entered is not valid."
)


# ==========================================================
# General Messages
# ==========================================================

# Generic success message.
SUCCESS_MESSAGE = (
    "Done successfully."
)


# Generic cancellation message.
CANCELLED_MESSAGE = (
    "Operation cancelled."
)