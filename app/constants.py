"""
constants.py

Store application constants.

Only application-wide constants belong here.

Do NOT store:

- Telegram commands
- Environment variables
- Configuration values

Those belong in their own dedicated modules.
"""

# ==========================================================
# Application Information
# ==========================================================

# Public name of the Telegram bot.
BOT_NAME = "Lanoo"

# Current application version.
APP_VERSION = "1.0.0"

# ==========================================================
# Application Limits
# ==========================================================

# Maximum accepted product name length.
MAX_PRODUCT_NAME_LENGTH = 100

# Maximum number of products returned
# from a search.
MAX_SEARCH_RESULTS = 10