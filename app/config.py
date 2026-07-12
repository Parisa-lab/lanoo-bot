"""
config.py

Load application configuration.

This module is responsible for loading application-wide
configuration values from environment variables.

Configuration values may differ between environments
(local development, Railway, Docker, etc.).
"""

# Import the os module.
#
# This module allows Python to read environment
# variables from the operating system.
import os


# ==========================================================
# Telegram Bot Configuration
# ==========================================================

# Read the Telegram bot token.
#
# Never hardcode secrets inside the source code.
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Stop the application if the token
# has not been configured.
if not BOT_TOKEN:
    raise RuntimeError(
        "BOT_TOKEN environment variable is missing."
    )