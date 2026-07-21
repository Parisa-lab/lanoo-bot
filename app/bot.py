"""
LanooBot main Telegram application.

This module creates and manages the Telegram bot instance.
Handler registration is delegated to the handlers package.
"""

import logging

from telegram.ext import Application

from app.config import settings
from app.handlers import register_handlers
from app.jobs.price_monitor import register_price_monitor_job
from app.database.session import close_database


logger = logging.getLogger(__name__)


async def error_handler(update, context):
    """
    Handle unexpected Telegram errors.
    """

    logger.exception(
        "Unhandled exception",
        exc_info=context.error,
    )


class LanooBot:
    """
    Main bot controller.
    """

    def __init__(self):
        """
        Initialize Telegram application.
        """

        self.application = (
            Application.builder()
            .token(settings.BOT_TOKEN)
            .build()
        )

        register_handlers(
            self.application
        )

        register_price_monitor_job(
            self.application
        )

        self.application.add_error_handler(
            error_handler
        )

    async def shutdown(self):
        """
        Close resources before shutdown.
        """

        await close_database()

    def run(self):
        """
        Start polling.
        """

        logger.info(
            "Starting LanooBot..."
        )

        self.application.run_polling()