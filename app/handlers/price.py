"""
price.py

Telegram command handler for Torob price lookup.

Usage:

/price https://torob.com/p/xxxxxxxx/

The bot will extract:

- Product title
- Cheapest seller
- Cheapest price
- Product image
"""

from telegram import Update
from telegram.ext import ContextTypes

from app.scrapers.torob import get_price


async def price_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
) -> None:
    """
    Handle /price command.

    Example:

    /price https://torob.com/p/xxxxxxxx/
    """

    if not context.args:

        await update.message.reply_text(
            "Usage:\n"
            "/price https://torob.com/p/xxxxxxxx/"
        )
        return

    url = context.args[0]

    try:

        data = await get_price(url)

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

        message = (
            f"📦 Product\n"
            f"{title}\n\n"
            f"🏪 Seller\n"
            f"{seller}\n\n"
            f"💰 Price\n"
            f"{price}\n\n"
            f"🖼 Image\n"
            f"{image}"
        )

        await update.message.reply_text(
            message
        )

    except Exception as error:

        await update.message.reply_text(
            f"Failed to fetch product.\n\n"
            f"Error:\n{error}"
        )