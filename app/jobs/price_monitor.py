"""
price_monitor.py
"""

import logging

from telegram.ext import ContextTypes

from app.scrapers.torob import get_price

logger = logging.getLogger(__name__)

PRODUCT_URL = (
    "https://torob.com/p/f498b27b-596c-47c8-a48d-0beed264b2d8/"
)

CHAT_ID = 625896200


async def monitor_price(
    context: ContextTypes.DEFAULT_TYPE,
) -> None:

    try:

        data = await get_price(
            PRODUCT_URL
        )

        message = (
            f"Product: {data['title']}\n\n"
            f"Seller: {data['seller']}\n\n"
            f"Price: {data['price']}"
        )

        await context.bot.send_message(
            chat_id=CHAT_ID,
            text=message,
        )

        logger.info(
            "Hourly check sent."
        )

    except Exception as error:

        logger.exception(error)