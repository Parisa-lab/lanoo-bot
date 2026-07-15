"""
price.py

Telegram command handler for Torob price lookup.

Usage:

/price https://torob.com/p/xxxxxxxx/
"""

from telegram import Update
from telegram.ext import ContextTypes

from app.scrapers.torob import get_price

print("PRICE FILE LOADED")


async def price_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
) -> None:

    print("PRICE COMMAND CALLED")
    print(context.args)

    if update.message:
        print(
            f"CHAT ID = {update.message.chat_id}"
        )

    if not context.args:

        await update.message.reply_text(
            "Usage:\n"
            "/price https://torob.com/p/xxxxxxxx/"
        )
        return

    url = context.args[0]

    try:

        await update.message.reply_text(
            "Fetching product..."
        )

        data = await get_price(url)

        print(data)

        title = data.get(
            "title",
            "Unknown Product",
        )

        seller = data.get(
            "seller",
            "Unknown Seller",
        )

        price = data.get(
            "price",
            "Unknown Price",
        )

        image = data.get(
            "image",
            "",
        )

        caption = (
            f"📦 {title}\n\n"
            f"🏪 {seller}\n"
            f"💰 {price}"
        )

        if image:

            await update.message.reply_photo(
                photo=image,
                caption=caption,
            )

            print("PHOTO SENT")

        else:

            await update.message.reply_text(
                caption
            )

            print("TEXT SENT")

    except Exception as error:

        print(
            f"ERROR = {error}"
        )

        await update.message.reply_text(
            "Failed to fetch product.\n\n"
            f"{error}"
        )