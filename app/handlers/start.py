from telegram import Update
from telegram.ext import ContextTypes

from app.scrapers.torob import get_price


async def start(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
) -> None:

    await update.message.reply_text(
        "شروع تست توروب..."
    )

    url = (
        "https://torob.com/p/"
        "f498b27b-596c-47c8-a48d-0beed264b2d8/"
    )

    data = await get_price(url)

    text = (
        f"📦 {data['title']}\n\n"
        f"💰 {data['price']}\n"
        f"🏪 {data['seller']}\n\n"
        f"🖼 {data['image']}"
    )

    await update.message.reply_text(text)