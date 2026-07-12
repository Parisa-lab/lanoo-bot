"""
bot.py

Create and run the Telegram bot.

This module is responsible for:

- Creating the Telegram Application
- Configuring the bot
- Registering all handlers
- Starting the polling loop
"""

# Import Python's logging module.
#
# Every module should use logging instead of print().
import logging

# Import Telegram Application.
#
# Application is the main entry point of the
# python-telegram-bot framework.
from telegram.ext import Application

# Import application settings.
#
# The bot token is loaded from environment variables.
from app.config import settings

# Import the logging configuration.
from app.logger import setup_logging

# Import the handler registration function.
#
# Every Telegram command is registered through this
# function.
from app.handlers import register_handlers


# Create a logger for this module.
logger = logging.getLogger(__name__)


class LanooBot:
    """
    Main Telegram bot class.

    This class creates the Telegram Application,
    registers all handlers and starts polling.
    """

    def __init__(self) -> None:
        """
        Initialize the Telegram bot.
        """

        # Configure the logging system.
        #
        # This should be executed only once during
        # application startup.
        setup_logging()

        logger.info("Initializing Lanoo Bot...")

        # Create the Telegram Application.
        #
        # The Application object receives updates from
        # Telegram and dispatches them to handlers.
        self.application = (
            Application.builder()
            .token(settings.bot_token)
            .build()
        )

        logger.info("Telegram Application created successfully.")

    def register_handlers(self) -> None:
        """
        Register every Telegram handler.

        Returns:
            None.
        """

        logger.info("Registering handlers...")

        register_handlers(
            self.application,
        )

        logger.info("Handlers registered successfully.")

    def run(self) -> None:
        """
        Start the Telegram bot.

        Returns:
            None.
        """

        logger.info("Starting bot...")

        # Register all handlers before polling starts.
        self.register_handlers()

        logger.info("Bot is now running.")

        # Start polling Telegram servers.
        #
        # drop_pending_updates=True prevents processing
        # old messages that were sent while the bot
        # was offline.
        self.application.run_polling(
            drop_pending_updates=True,
        )