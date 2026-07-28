"""
app/handlers/add.py

Telegram command handler for adding products.

The handler contains no scraper or database logic.
"""

from __future__ import annotations

import logging

from telegram import Update
from telegram.ext import ContextTypes

from app.container import price_service


logger = logging.getLogger(__name__)



async def add_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
) -> None:

    if not update.message:
        return

    if not context.args:

        await update.message.reply_text(
            "Usage:\n/add URL"
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

        await update.message.reply_text(
            f"✅ Added:\n\n{data['title']}"
        )

    except Exception:

        logger.exception(
            "Failed to add product."
        )

        await update.message.reply_text(
            "An unexpected error occurred."
        )