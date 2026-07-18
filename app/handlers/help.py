from telegram import Update
from telegram.ext import ContextTypes


async def help_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
) -> None:

    if not update.message:
        return

    await update.message.reply_text(
        "Commands:\n\n"
        "/start\n"
        "/help\n"
        "/price <torob_url>"
    )