"""
Telegram command handler registration.

This module is the single entry point for all bot commands.
"""

import logging

from telegram.ext import (
    Application,
    CommandHandler,
)

from app.handlers.start import start_command
from app.handlers.help import help_command
from app.handlers.price import price_command
from app.handlers.add import add_command
from app.handlers.list_products import list_command


logger = logging.getLogger(__name__)


def register_handlers(
    application: Application,
) -> None:
    """
    Register all Telegram command handlers.

    Args:
        application:
            Telegram application instance.
    """

    handlers = [
        CommandHandler(
            "start",
            start_command,
        ),
        CommandHandler(
            "help",
            help_command,
        ),
        CommandHandler(
            "price",
            price_command,
        ),
        CommandHandler(
            "add",
            add_command,
        ),
        CommandHandler(
            "list",
            list_command,
        ),
    ]

    for handler in handlers:
        application.add_handler(handler)

    logger.info(
        "%s handlers registered",
        len(handlers),
    )