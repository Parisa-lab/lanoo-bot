from telegram import Update
from telegram.ext import ContextTypes

from app.database.repository import (
get_products_by_chat,
)

async def list_command(
update: Update,
context: ContextTypes.DEFAULT_TYPE,
):

if not update.message:
    return

products = await get_products_by_chat(
    update.message.chat_id
)

if not products:

    await update.message.reply_text(
        "No products found."
    )
    return

text = ""

for index, product in enumerate(
    products,
    start=1,
):

    text += (
        f"{index}. "
        f"{product.title}\n"
    )

await update.message.reply_text(
    text
)