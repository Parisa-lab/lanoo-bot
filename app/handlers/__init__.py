"""
handlers package

Register all Telegram handlers here.
"""

# ==========================================================
# Third-Party Imports
# ==========================================================

from telegram.ext import Application
from telegram.ext import CommandHandler

# ==========================================================
# Local Imports
# ==========================================================

from app.handlers.start import start_command
from app.handlers.help import help_command
from app.handlers.price import price_command

# ==========================================================
# Registration
# ==========================================================

def register_handlers(
    application: Application,
) -> None:
    """
    Register all Telegram handlers.
    """

    print("REGISTER_HANDLERS CALLED")

    application.add_handler(
        CommandHandler(
            "start",
            start_command,
        )
    )

    application.add_handler(
        CommandHandler(
            "help",
            help_command,
        )
    )

    application.add_handler(
        CommandHandler(
            "price",
            price_command,
        )
    )

    print("START HANDLER REGISTERED")
    print("HELP HANDLER REGISTERED")
    print("PRICE HANDLER REGISTERED")