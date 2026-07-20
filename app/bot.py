"""
bot.py

Create and run the Telegram bot.
"""

import logging

from telegram import Update
from telegram.ext import Application

from app.config import settings
from app.logger import setup_logging
from app.handlers import register_handlers
from app.error_handler import error_handler
from app.jobs import register_jobs

logger = logging.getLogger(__name__)


class LanooBot:

    def __init__(self) -> None:

        setup_logging()

        logger.info(
            "Initializing Lanoo Bot..."
        )


        self.application = (
            Application.builder()
            .token(settings.bot_token)
            .build()
        )

        self.application.add_error_handler(
            error_handler
        )

        logger.info(
            "Telegram Application created successfully."
        )

    def register_handlers(self) -> None:

        logger.info(
            "Registering command handlers..."
        )

        register_handlers(
            self.application
        )

        logger.info(
            "All handlers registered successfully."
        )

    def register_jobs(self) -> None:

        logger.info(
            "Registering jobs..."
        )

        register_jobs(
            self.application
        )

        logger.info(
            "All jobs registered successfully."
        )

    def run(self) -> None:

        logger.info(
            "Starting Lanoo Bot..."
        )

        self.register_handlers()

        self.register_jobs()

        logger.info(
            "Bot started successfully."
        )

        self.application.run_polling(
            drop_pending_updates=True,
            allowed_updates=Update.ALL_TYPES,
        )

    def stop(self) -> None:

        logger.info(
            "Stopping bot..."
        )

        logger.info(
            "Bot stopped successfully."
        )