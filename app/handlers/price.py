"""
app/handlers/price.py

Telegram command handler for Torob price lookup.

Responsibilities:
- Read Telegram command arguments
- Call PriceService
- Save product information if needed
- Display formatted results

The handler should not communicate with the scraper directly.
"""

from __future__ import annotations

import logging

from telegram import InlineKeyboardButton
from telegram import InlineKeyboardMarkup
from telegram import Update
from telegram.ext import ContextTypes

from app.database.repository import add_product
from app.database.repository import get_product_by_url
from app.services.price_service import PriceService

logger = logging.getLogger(__name__)

price_service = PriceService()


async def price_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
) -> None:
    """
    Handle the /price command.

    Example:
        /price https://torob.com/p/xxxxxxxx/
    """

    if not update.message:
        return

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

        data = await price_service.search(url)

        if not data:
            await update.message.reply_text(
                "Unable to fetch product."
            )
            return

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

        existing_product = await get_product_by_url(
            chat_id=update.message.chat_id,
            url=url,
        )

        if not existing_product:

            await add_product(
                chat_id=update.message.chat_id,
                url=url,
                title=title,
                price=price,
            )

            logger.info(
                "Saved new product. chat_id=%s url=%s",
                update.message.chat_id,
                url,
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

        if image:

            await update.message.reply_photo(
                photo=image,
                caption=caption,
                reply_markup=keyboard,
            )

        else:

            await update.message.reply_text(
                text=caption,
                reply_markup=keyboard,
            )

    except Exception:

        logger.exception(
            "Unexpected error in /price command."
        )

        await update.message.reply_text(
            "An unexpected error occurred."
        )