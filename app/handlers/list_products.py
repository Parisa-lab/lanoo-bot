from telegram import Update
from telegram.ext import ContextTypes

from app.storage.database import load_products


async def list_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    if not update.message:
        return

    products = load_products()

    my_products = [
        p
        for p in products
        if p["chat_id"]
        == update.message.chat_id
    ]

    if not my_products:

        await update.message.reply_text(
            "No products found."
        )
        return

    text = ""

    for i, product in enumerate(
        my_products,
        start=1,
    ):
        text += (
            f"{i}. "
            f"{product['title']}\n"
        )

    await update.message.reply_text(
        text
    )