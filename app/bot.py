"""
bot.py

Create and start the Telegram bot.

This module is responsible for:

- Creating the Telegram Application.
- Registering all command handlers.
- Starting the bot.
"""

# Import the logging module.
#
# Logging is much better than using print().
# It helps us monitor the application
# and diagnose problems.
import logging


# Import the Application class.
#
# Application is the main object of every Telegram bot.
from telegram.ext import Application


# Import the CommandHandler class.
#
# CommandHandler connects Telegram commands
# to Python functions.
from telegram.ext import CommandHandler


# Import the bot token.
#
# The token is loaded from environment variables
# inside config.py.
from app.config import BOT_TOKEN


# Import command names.
#
# Keeping command names in constants.py
# avoids hardcoding strings.
from app.constants import (
    START_COMMAND,
)


# Import command handlers.
#
# The handlers package exports all public handlers.
from app.handlers import (
    start,
)


# Create a logger for this module.
#
# Every module should have its own logger.
logger = logging.getLogger(__name__)


def run_bot() -> None:
    """
    Create and start the Telegram bot.

    Returns:
        None
    """

    # Write an informational log message.
    logger.info("Creating Telegram application.")

    # Create the Telegram application.
    #
    # builder() creates a builder object.
    #
    # token() sets the bot token.
    #
    # build() creates the Application instance.
    application = (
        Application
        .builder()
        .token(BOT_TOKEN)
        .build()
    )

    # Register the /start command.
    #
    # When a user sends /start,
    # the start() function will run.
    application.add_handler(
        CommandHandler(
            START_COMMAND,
            start,
        )
    )

    # Write another log message.
    logger.info("Starting polling...")

    # Start listening for Telegram updates.
    application.run_polling()