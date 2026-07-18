from telegram import Update
from telegram.ext import ContextTypes


async def help_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
) -> None:

    await update.message.reply_text(
        "Commands:\n\n"
        "/start - Start bot\n"
        "/help - Show help\n"
        "/price <torob_url> - Get product price"
    )