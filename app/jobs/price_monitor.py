"""
price_monitor.py

Monitor Torob prices and notify only when price changes.
"""

import logging

from telegram.ext import ContextTypes

from app.scrapers.torob import get_price
from app.database import (
    get_price as get_saved_price,
    set_price,
)

logger = logging.getLogger(__name__)

PRODUCT_URL = (
    "https://torob.com/p/f498b27b-596c-47c8-a48d-0beed264b2d8/"
)

CHAT_ID = 625896200


async def monitor_price(
    context: ContextTypes.DEFAULT_TYPE,
) -> None:
    """
    Check product price.
    Send message only if changed.
    """

    try:

        data = await get_price(
            PRODUCT_URL
        )

        title = data["title"]
        seller = data["seller"]
        new_price = data["price"]

        old_price = get_saved_price(
            PRODUCT_URL
        )

        # First run

        if old_price is None:

            set_price(
                PRODUCT_URL,
                new_price,
            )

            await context.bot.send_message(
                chat_id=CHAT_ID,
                text=(
                    "Price monitor started.\n\n"
                    f"Product: {title}\n"
                    f"Current Price: {new_price}"
                ),
            )

            logger.info(
                "Initial price saved."
            )

            return

        # No change
        new_price = old_price - 1000
        if old_price == new_price:

            logger.info(
                "Price unchanged."
            )

            return

        # Price changed

        set_price(
            PRODUCT_URL,
            new_price,
        )

        message = (
            "PRICE CHANGED\n\n"
            f"Product:\n{title}\n\n"
            f"Seller:\n{seller}\n\n"
            f"Old Price:\n{old_price}\n\n"
            f"New Price:\n{new_price}"
        )

        await context.bot.send_message(
            chat_id=CHAT_ID,
            text=message,
        )

        logger.info(
            "Price change notification sent."
        )

    except Exception as error:

        logger.exception(error)