"""
handlers/__init__.py

Register all Telegram command handlers.
"""

# Import Telegram command handler.
from telegram.ext import Application
from telegram.ext import CommandHandler

# Import command names.
from app.telegram.commands import (
    START,
    HELP,
    PRICE,
)

# Import handler functions.
from app.handlers.start import start_handler
from app.handlers.help import help_handler
from app.handlers.price import price_handler


def register_handlers(application: Application) -> None:
    """
    Register every Telegram command handler.

    Args:
        application:
            Telegram Application instance.

    Returns:
        None.
    """

    application.add_handler(
        CommandHandler(
            START,
            start_handler,
        )
    )

    application.add_handler(
        CommandHandler(
            HELP,
            help_handler,
        )
    )

    application.add_handler(
        CommandHandler(
            PRICE,
            price_handler,
        )
    )