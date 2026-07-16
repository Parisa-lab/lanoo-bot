"""
start.py
"""

from telegram import Update
from telegram.ext import ContextTypes


async def start_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
) -> None:

    if not update.message:
        return

    await update.message.reply_text(
        "Welcome to Lanoo Bot.\n\n"
        "Usage:\n"
        "/price <torob_url>"
    )