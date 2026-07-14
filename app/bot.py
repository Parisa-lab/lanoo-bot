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

import logging

# ---------------------------------------------------------
# Third-Party Imports
# ---------------------------------------------------------

from telegram import Update
from telegram.ext import Application

# ---------------------------------------------------------
# Local Imports
# ---------------------------------------------------------

from app.config import settings
from app.logger import setup_logging
from app.handlers import register_handlers
from app.error_handler import error_handler

# ---------------------------------------------------------
# Logger
# ---------------------------------------------------------

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
        setup_logging()

        # Startup log.
        logger.info(
            "Initializing Lanoo Bot..."
        )

        # Create Telegram application.
        self.application = (
            Application.builder()
            .token(settings.bot_token)
            .build()
        )

        # Register global error handler.
        #
        # Every unhandled exception in any handler
        # will be sent to error_handler().
        self.application.add_error_handler(
            error_handler,
        )

        logger.info(
            "Telegram Application created successfully."
        )

    def register_handlers(self) -> None:
        """
        Register all Telegram handlers.
        """

        logger.info(
            "Registering command handlers..."
        )

        register_handlers(
            self.application,
        )

        logger.info(
            "All handlers registered successfully."
        )

    def run(self) -> None:
        """
        Start the Telegram bot.

        Returns:
            None.
        """

        logger.info(
            "Starting Lanoo Bot..."
        )

        # Register handlers.
        self.register_handlers()

        logger.info(
            "Bot started successfully."
        )

        # Start polling.
        #
        # drop_pending_updates=True:
        # Ignore messages received while the bot
        # was offline.
        #
        # allowed_updates=Update.ALL_TYPES:
        # Receive all Telegram update types.
        self.application.run_polling(
            drop_pending_updates=True,
            allowed_updates=Update.ALL_TYPES,
        )

        logger.info(
            "Bot stopped."
        )

    def stop(self) -> None:
        """
        Stop the Telegram bot.

        Returns:
            None.
        """

        logger.info(
            "Stopping bot..."
        )

        if self.application is not None:
            self.application.stop()

        logger.info(
            "Bot stopped successfully."
        )