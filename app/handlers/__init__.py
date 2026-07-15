"""
handlers package

Register all Telegram handlers here.
"""

from telegram.ext import Application
from telegram.ext import CommandHandler

from app.handlers.start import start
from app.handlers.price import price_command




print("HANDLERS INIT LOADED")





def register_handlers(
    application: Application,
) -> None:
    """
    Register all Telegram handlers.
    """

    application.add_handler(
        CommandHandler(
            "start",
            start,
        )
    )

    application.add_handler(
        CommandHandler(
            "price",
            price_command,
        )
    )