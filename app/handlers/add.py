"""
app/handlers/add.py

Telegram command handler for adding a Torob product to the tracking database.

Responsibilities:
- Read command arguments
- Call PriceService
- Save the product if it does not already exist
- Send user-friendly Telegram responses

Business logic should remain in services and repositories.
"""

from __future__ import annotations

import logging

from telegram import Update
from telegram.ext import ContextTypes

from app.database.repository import add_product
from app.database.repository import get_product_by_url
from app.services.price_service import PriceService

logger = logging.getLogger(__name__)

price_service = PriceService()


async def add_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
) -> None:
    """
    Handle the /add command.

    Example:
        /add https://torob.com/p/xxxxxxxx/
    """

    if not update.message:
        return

    if not context.args:
        await update.message.reply_text(
            "Usage:\n/add https://torob.com/p/xxxxxxxx/"
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

        existing_product = await get_product_by_url(
            chat_id=update.message.chat_id,
            url=url,
        )

        if existing_product:
            await update.message.reply_text(
                "This product is already being tracked."
            )
            return

        await add_product(
            chat_id=update.message.chat_id,
            url=url,
            title=data["title"],
            price=data["price"],
        )

        logger.info(
            "Product added. chat_id=%s url=%s",
            update.message.chat_id,
            url,
        )

        await update.message.reply_text(
            f"✅ Added product:\n\n{data['title']}"
        )

    except Exception:
        logger.exception(
            "Unexpected error while adding product."
        )

        await update.message.reply_text(
            "An unexpected error occurred."
        )