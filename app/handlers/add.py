from telegram import Update
from telegram.ext import ContextTypes

from app.scrapers.torob import get_price
from app.storage.database import (
    load_products,
    save_products,
)


async def add_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    if not update.message:
        return

    if not context.args:

        await update.message.reply_text(
            "Usage:\n/add URL"
        )
        return

    url = context.args[0]

    data = await get_price(url)

    products = load_products()

    products.append(
        {
            "chat_id": update.message.chat_id,
            "url": url,
            "title": data["title"],
            "price": data["price"],
        }
    )

    save_products(products)

    await update.message.reply_text(
        f"Added:\n{data['title']}"
    )