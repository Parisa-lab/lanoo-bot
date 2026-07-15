"""
price.py

Telegram command handler for Torob price lookup.

Usage:

/price https://torob.com/p/xxxxxxxx/
"""

import traceback

from telegram import Update
from telegram import InlineKeyboardButton
from telegram import InlineKeyboardMarkup
from telegram.ext import ContextTypes

from app.scrapers.torob import get_price

print("PRICE FILE LOADED")


async def price_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
) -> None:
    """
    Handle /price command.
    """

    print("PRICE COMMAND CALLED")
    print(context.args)

    if not update.message:
        return

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
            f"📦 Product\n"
            f"{title}\n\n"
            f"🏪 Seller\n"
            f"{seller}\n\n"
            f"💰 Price\n"
            f"{price}"
        )

        keyboard = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="🛒 View on Torob",
                        url=url,
                    )
                ]
            ]
        )

        print("SENDING RESULT")

        if image:

            await update.message.reply_photo(
                photo=image,
                caption=caption,
                reply_markup=keyboard,
            )

            print("PHOTO SENT")

        else:

            await update.message.reply_text(
                text=caption,
                reply_markup=keyboard,
            )

            print("TEXT SENT")

    except Exception as error:

        print("ERROR OCCURRED")
        traceback.print_exc()

        await update.message.reply_text(
            f"ERROR:\n{repr(error)}"
        )