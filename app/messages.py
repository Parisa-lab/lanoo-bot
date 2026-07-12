"""
messages.py

Store all user-facing messages.

This module contains every message displayed to users.

Keeping messages separate from the application logic
provides several benefits:

- Cleaner code.
- Easier maintenance.
- Easier localization.
- Easier testing.
- Consistent user experience.
"""

# Import application constants.
#
# The bot name is defined in one place and reused
# throughout the application.
from app.constants import BOT_NAME


# ==========================================================
# Welcome Messages
# ==========================================================

# Welcome message displayed after /start.
WELCOME_MESSAGE = (
    f"👋 Welcome to {BOT_NAME}!\n\n"
    "Your smart assistant for comparing prices of "
    "baby and family products.\n\n"
    "Use /help to see the available commands."
)


# ==========================================================
# Help Messages
# ==========================================================

# Help message listing all supported commands.
HELP_MESSAGE = (
    "Available commands\n\n"
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

# Displayed while the search is running.
SEARCHING_MESSAGE = (
    "Searching for the best prices..."
)

# Displayed when no matching products are found.
NO_PRODUCTS_FOUND_MESSAGE = (
    "No matching products were found."
)

# Template used when products are found.
#
# Example:
#
# Found 8 matching products.
PRODUCTS_FOUND_MESSAGE = (
    "Found {count} matching products."
)

# Template used for every product.
#
# Example:
#
# Baby Stroller
# 💰 Price: 18,900,000 IRR
# 🛒 Store: Torob
PRODUCT_TEMPLATE = (
    "📦 {name}\n"
    "💰 Price: {price}\n"
    "🏪 Store: {store}"
)

# Template used when displaying a product link.
#
# Example:
#
# 🔗 https://...
PRODUCT_LINK_TEMPLATE = (
    "🔗 {url}"
)


# ==========================================================
# Validation Messages
# ==========================================================

# Displayed when the user sends invalid input.
INVALID_INPUT_MESSAGE = (
    "The information you entered is not valid."
)

# Displayed when the product name is too long.
PRODUCT_NAME_TOO_LONG_MESSAGE = (
    "The product name is too long."
)

# Displayed when the product name is empty.
EMPTY_PRODUCT_NAME_MESSAGE = (
    "Please enter a product name."
)


# ==========================================================
# Error Messages
# ==========================================================

# Displayed when an unknown command is received.
UNKNOWN_COMMAND_MESSAGE = (
    "Sorry, I don't recognize that command."
)

# Displayed when an unexpected error occurs.
INTERNAL_ERROR_MESSAGE = (
    "Something went wrong.\n"
    "Please try again later."
)

# Displayed when a website cannot be reached.
NETWORK_ERROR_MESSAGE = (
    "Unable to connect to the requested website."
)

# Displayed when the request takes too long.
TIMEOUT_MESSAGE = (
    "The request timed out.\n"
    "Please try again."
)


# ==========================================================
# General Messages
# ==========================================================

SUCCESS_MESSAGE = (
    "Operation completed successfully."
)

CANCELLED_MESSAGE = (
    "Operation cancelled."
)

COMING_SOON_MESSAGE = (
    "This feature is coming soon."
)