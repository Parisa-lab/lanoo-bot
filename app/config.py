"""
config.py

Load application configuration.

This module is responsible for loading configuration
values from environment variables.

Configuration values may change between environments
(local development, Railway, Docker, etc.), so they
must never be hardcoded inside the application logic.
"""

# Import the logging module.
#
# We use its predefined logging constants instead
# of plain strings such as "INFO" or "DEBUG".
import logging

# Import the os module.
#
# This module allows Python to read environment
# variables from the operating system.
import os


# ==========================================================
# Telegram Configuration
# ==========================================================

# Read the Telegram bot token from the environment.
#
# Never store the bot token directly inside the source code.
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Stop the application immediately if the token
# has not been configured.
if not BOT_TOKEN:
    raise RuntimeError(
        "BOT_TOKEN environment variable is missing."
    )


# ==========================================================
# Telegram Settings
# ==========================================================

# Default parse mode.
#
# None means plain text.
#
# Later we may change this to:
# - "HTML"
# - "MarkdownV2"
DEFAULT_PARSE_MODE = None


# ==========================================================
# Logging Configuration
# ==========================================================

# Default logging level.
#
# We use the logging module constants instead of strings.
#
# Available options include:
#
# logging.DEBUG
# logging.INFO
# logging.WARNING
# logging.ERROR
# logging.CRITICAL
LOG_LEVEL = logging.INFO