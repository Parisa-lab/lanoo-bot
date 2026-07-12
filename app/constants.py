"""
constants.py

Store all application constants.

A constant is a value that should not change while the
application is running.

Keeping constants in one place makes the project easier
to maintain and prevents duplicated values across files.
"""

# ==========================================================
# Application Information
# ==========================================================

# Public name of the Telegram bot.
#
# If we ever change the bot's name,
# we only need to update this value.
BOT_NAME = "Lanoo"


# Current application version.
#
# This value is useful for logging,
# debugging and future releases.
APP_VERSION = "1.0.0"


# ==========================================================
# Telegram Commands
# ==========================================================

# Command executed when a user starts the bot.
START_COMMAND = "start"


# Command that shows help information.
HELP_COMMAND = "help"


# Command used to search product prices.
PRICE_COMMAND = "price"


# ==========================================================
# Telegram Settings
# ==========================================================

# Parse mode used by Telegram.
#
# None means plain text.
#
# Later we may change this to HTML
# or MarkdownV2.
DEFAULT_PARSE_MODE = None


# ==========================================================
# Logging
# ==========================================================

# Default logging level.
#
# Possible values include:
#
# DEBUG
# INFO
# WARNING
# ERROR
# CRITICAL
LOG_LEVEL = "INFO"