"""
telegram_config.py

Store Telegram-specific configuration.

Keeping Telegram settings separate from the main
application configuration makes the project easier
to maintain as it grows.
"""

# Import the ParseMode enum.
#
# Using the enum avoids typing strings such as
# "HTML" or "MarkdownV2".
from telegram.constants import ParseMode


# ==========================================================
# Message Formatting
# ==========================================================

# Default parse mode used by the bot.
#
# Supported values include:
#
# ParseMode.HTML
# ParseMode.MARKDOWN_V2
#
# We start with HTML because it is simpler
# and less error-prone than MarkdownV2.
DEFAULT_PARSE_MODE = ParseMode.HTML


# ==========================================================
# Telegram Limits
# ==========================================================

# Maximum number of buttons allowed
# in a single keyboard row.
#
# This is our own design limit, not
# Telegram's maximum.
MAX_BUTTONS_PER_ROW = 3


# ==========================================================
# Polling Configuration
# ==========================================================

# Receive every update type.
#
# Later we can limit this to messages only
# if needed.
ALLOWED_UPDATES = None