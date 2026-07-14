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

    application.add_handler(
        CommandHandler(
            "price",
            price_command,
        )
    )