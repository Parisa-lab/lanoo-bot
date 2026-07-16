"""
handlers package

Register all Telegram handlers here.
"""

# ==========================================================
# Debug
# ==========================================================

print("HANDLERS INIT LOADED")

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
# Start Command
# ==========================================================

async def start_command(update, context) -> None:

    if not update.message:
        return

    await update.message.reply_text(
        "Welcome to Lanoo Bot.\n\n"
        "Usage:\n"
        "/price <torob_url>"
    )

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

    print("START HANDLER REGISTERED")

    application.add_handler(
        CommandHandler(
            "price",
            price_command,
        )
    )

    print("PRICE HANDLER REGISTERED")