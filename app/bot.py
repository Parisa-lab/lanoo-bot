"""
bot.py

Create and run the Telegram bot.

This module is responsible for:

- Creating the Telegram Application
- Registering all handlers
- Registering the global error handler
- Starting the polling loop
"""

# ---------------------------------------------------------
# Standard Library Imports
# ---------------------------------------------------------

# Import Python logging module.
import logging

# ---------------------------------------------------------
# Third-Party Imports
# ---------------------------------------------------------

# Telegram Application.
#
# This is the main object of python-telegram-bot.
from telegram.ext import Application

# ---------------------------------------------------------
# Local Imports
# ---------------------------------------------------------

# Import application settings.
#
# The bot token is loaded from environment variables.
from app.config import settings

# Import logging configuration.
from app.logger import setup_logging

# Import handler registration function.
from app.handlers import register_handlers

# Import global error handler.
from app.error_handler import error_handler

# ---------------------------------------------------------
# Logger
# ---------------------------------------------------------

# Create a logger dedicated to this module.
logger = logging.getLogger(__name__)


class LanooBot:
    """
    Main Telegram bot.

    This class is responsible for creating
    and running the Telegram application.
    """

    def __init__(self) -> None:
        """
        Initialize the Telegram bot.
        """

        # Configure logging.
        #
        # This function should only run once
        # during application startup.
        setup_logging()

        # Write a startup message.
        logger.info("Initializing Lanoo Bot...")

        # Create the Telegram Application.
        #
        # The Application object receives updates
        # from Telegram servers.
        self.application = (
            Application.builder()
            .token(settings.bot_token)
            .build()
        )

        # Log successful initialization.
        logger.info(
            "Telegram Application created successfully."
        )

    def register_handlers(self) -> None:
        """
        Register every Telegram handler.
        """

        # Log current operation.
        logger.info("Registering command handlers...")

        # Register all command handlers.
        register_handlers(
            self.application,
        )

        # Register the global error handler.
        #
        # Every unhandled exception inside
        # any command will arrive here.
        self.application.add_error_handler(
            error_handler,
        )

        # Log success.
        logger.info(
            "All handlers registered successfully."
        )

    def run(self) -> None:
        """
        Start the Telegram bot.

        This method starts polling Telegram servers
        and keeps the application running until it
        is stopped manually.

        Returns:
            None.
        """

        # Write a startup message.
        logger.info("Starting Lanoo Bot...")

        # Register every command handler.
        #
        # This method also registers the global
        # error handler.
        self.register_handlers()

        # Write a success message.
        logger.info("Bot started successfully.")

        # Start receiving updates from Telegram.
        #
        # drop_pending_updates=True tells Telegram
        # to ignore old messages that arrived while
        # the bot was offline.
        self.application.run_polling(
            drop_pending_updates=True,
        )

        # This line is reached only after the bot
        # has stopped running.
        logger.info("Bot stopped.")

    def stop(self) -> None:
        """
        Stop the Telegram bot.

        Returns:
            None.
        """

        # Write a shutdown message.
        logger.info("Stopping bot...")

        # Stop polling if the application exists.
        if self.application is not None:
            self.application.stop()

        # Write a final log message.
        logger.info("Bot stopped successfully.")