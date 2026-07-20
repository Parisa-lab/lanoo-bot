from telegram import Update
from telegram.ext import ContextTypes

from app.database.repository import get_products_by_chat


async def list_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    """
    Display all tracked products for the current chat.
    """

    if not update.message:
        return

    products = await get_products_by_chat(
        update.message.chat_id
    )

    if not products:
        await update.message.reply_text(
            "No tracked products."
        )
        return

    lines = []

    for product in products:
        lines.append(
            f"• {product.title}\n"
            f"Price: {product.last_price}"
        )

    await update.message.reply_text(
        "\n\n".join(lines)
    )