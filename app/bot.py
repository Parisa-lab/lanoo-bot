"""
Telegram bot bootstrap.

Responsible for:

- Creating the Telegram Application
- Registering handlers
- Registering jobs
- Configuring error handling
- Starting the bot

Author: Lanoo
"""

import logging

from telegram.ext import Application
from telegram.ext import CommandHandler

from app.config import settings
from app.database.session import close_database
from app.handlers.add import add_command
from app.handlers.list_products import list_command
from app.jobs.price_monitor import check_prices

logger = logging.getLogger(name)

async def error_handler(
update,
context,
):
"""
Global error handler.
"""

logger.exception(
    "Unhandled exception",
    exc_info=context.error,
)

class LanooBot:
"""
Main Telegram bot application.
"""

def __init__(self) -> None:

    self.application = (
        Application.builder()
        .token(settings.bot_token)
        .build()
    )

    self._register_handlers()
    self._register_jobs()

    self.application.add_error_handler(
        error_handler
    )

def _register_handlers(
    self,
) -> None:
    """
    Register Telegram commands.
    """

    self.application.add_handler(
        CommandHandler(
            "add",
            add_command,
        )
    )

    self.application.add_handler(
        CommandHandler(
            "list",
            list_command,
        )
    )

def _register_jobs(
    self,
) -> None:
    """
    Register recurring background jobs.
    """

    self.application.job_queue.run_repeating(
        check_prices,
        interval=900,
        first=30,
        name="price_monitor",
    )

async def post_shutdown(
    self,
    application: Application,
) -> None:
    """
    Cleanup resources during shutdown.
    """

    await close_database()

def run(self) -> None:
    """
    Start Telegram polling.
    """

    logger.info(
        "Starting Lanoo Bot..."
    )

    self.application.post_shutdown = (
        self.post_shutdown
    )

    self.application.run_polling(
        drop_pending_updates=True
    )