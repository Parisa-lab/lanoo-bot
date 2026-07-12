"""
config.py

Load application configuration.

Configuration values are loaded from environment
variables instead of being hardcoded.

This improves security and allows the application
to run in different environments without changing
the source code.
"""

# Import the os module.
#
# This module allows Python to read
# environment variables from the operating system.
import os


# ==========================================================
# Telegram Configuration
# ==========================================================

# Read the Telegram bot token from
# the environment variables.
#
# The token should NEVER be stored
# directly inside the source code.
BOT_TOKEN = os.getenv("BOT_TOKEN")


# Make sure the token exists.
#
# If BOT_TOKEN is missing,
# stop the application immediately.
#
# Running a Telegram bot without a token
# is impossible.
if BOT_TOKEN is None:
    raise RuntimeError(
        "BOT_TOKEN environment variable is missing."
    )


# ==========================================================
# Telegram Settings
# ==========================================================

# Default parse mode.
#
# None means plain text messages.
#
# Later we can change this to:
#
# "HTML"
#
# or
#
# "MarkdownV2"
#
# without modifying other files.
DEFAULT_PARSE_MODE = None


# ==========================================================
# Logging Configuration
# ==========================================================

# Default logging level.
#
# Available values include:
#
# DEBUG
# INFO
# WARNING
# ERROR
# CRITICAL
#
# The logger module will use this value.
LOG_LEVEL = "INFO"