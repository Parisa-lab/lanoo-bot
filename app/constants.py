"""
constants.py

Store application constants.

This module contains values that are fixed during the
lifetime of the application.

Do NOT store configuration values here.

Examples of configuration values:
- Bot Token
- Database URL
- Logging Level

Those values belong in config.py.
"""

# ==========================================================
# Application Information
# ==========================================================

# Public name of the Telegram bot.
BOT_NAME = "Lanoo"

# Current application version.
APP_VERSION = "1.0.0"


# ==========================================================
# Telegram Commands
# ==========================================================

# Command executed when the user starts the bot.
START_COMMAND = "start"

# Command that displays help information.
HELP_COMMAND = "help"

# Command used to search product prices.
PRICE_COMMAND = "price"


# ==========================================================
# Application Limits
# ==========================================================

# Maximum length of a product name accepted
# from the user.
#
# This value helps prevent extremely long
# messages and unnecessary processing.
MAX_PRODUCT_NAME_LENGTH = 100


# Maximum number of search results returned
# to the user.
#
# Showing too many products makes the bot
# difficult to use.
MAX_SEARCH_RESULTS = 10