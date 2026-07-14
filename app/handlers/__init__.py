"""
handlers package
"""

from telegram.ext import Application
from telegram.ext import CommandHandler

from app.handlers.price import price_command


def register_handlers(
    application: Application,
) -> None:
    """
    Register Telegram handlers.
    """

    application.add_handler(
        CommandHandler(
            "price",
            price_command,
        )
    )