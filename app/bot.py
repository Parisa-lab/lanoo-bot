"""
bot.py

Create and run the Telegram bot.

This module is responsible for:

- Creating the Telegram Application.
- Registering all handlers.
- Starting the bot.
"""

# Import the logging module.
#
# Logging is used instead of print() because it
# provides structured and configurable output.
import logging

# Import Telegram classes.
from telegram.ext import (
    Application,
)

# Import application settings.
#
# The bot token is loaded from environment variables
# using Pydantic Settings.
from app.config import settings

# Import Telegram-specific configuration.
from app.telegram_config import (
    DEFAULT_PARSE_MODE,
    ALLOWED_UPDATES,
)

# Import the logging configuration.
#
# setup_logging() configures the logging system
# before the bot starts.
from app.logger import setup_logging

# Import the function that registers every handler.
from app.handlers import register_handlers


# Create a logger dedicated to this module.
logger = logging.getLogger(__name__)


class LanooBot:
    """
    Telegram bot controller.

    This class is responsible for creating,
    configuring and running the Telegram bot.
    """

    def __init__(self) -> None:
        """
        Initialize the bot.
        """

        # Configure the logging system.
        setup_logging()

        logger.info("Creating Telegram application...