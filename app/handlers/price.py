"""
app/handlers/price.py

Telegram price lookup command.

The handler delegates all business logic to PriceService.
"""

from __future__ import annotations

import logging

from telegram import InlineKeyboardButton
from telegram import InlineKeyboardMarkup
from telegram import Update
from telegram.ext import ContextTypes

from app.container import price_service

logger = logging.getLogger(__name__)




async def price_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
) -> None:

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

        data = await price_service.track_product(
            chat_id=update.message.chat_id,
            url=url,
        )

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
            "Price command failed."
        )

        await update.message.reply_text(
            "An unexpected error occurred."
        )