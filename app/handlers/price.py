from telegram import Update
from telegram.ext import ContextTypes, CommandHandler

from app.scrapers.torob import get_price


async def price_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    url = (
        "https://torob.com/p/f498b27b-596c-47c8-a48d-0beed264b2d8/"
    )

    data = await get_price(url)

    text = (
        f"📦 {data['title']}\n\n"
        f"🏪 {data['seller']}\n"
        f"💰 {data['price']}\n"
        f"🖼 {data['image']}"
    )

    await update.message.reply_text(text)


def register_price_handler(application):
    application.add_handler(
        CommandHandler(
            "price",
            price_command,
        )
    )