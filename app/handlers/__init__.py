"""
handlers package
"""

from telegram.ext import Application
from telegram.ext import CommandHandler

from app.handlers.start import start_command
from app.handlers.price import price_command


def register_handlers(
    application: Application,
) -> None:

    application.add_handler(
        CommandHandler(
            "start",
            start_command,
        )
    )

    application.add_handler(
        CommandHandler(
            "price",
            price_command,
        )
    )