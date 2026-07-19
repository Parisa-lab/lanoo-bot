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


def normalize_price(price: str) -> int:

    persian_digits = "۰۱۲۳۴۵۶۷۸۹"
    english_digits = "0123456789"

    translation = str.maketrans(
        persian_digits,
        english_digits,
    )

    cleaned = (
        str(price)
        .translate(translation)
        .replace("٫", "")
        .replace(",", "")
        .replace("تومان", "")
        .replace(" ", "")
        .strip()
    )

    return int(cleaned)


async def monitor_price(
    context: ContextTypes.DEFAULT_TYPE,
) -> None:

    try:

        data = await get_price(
            PRODUCT_URL
        )

        if data is None:

            logger.warning(
                "Skipping check because Torob returned 429."
            )

            return

        title = data["title"]
        seller = data["seller"]
        new_price = data["price"]

        old_price = get_saved_price(
            PRODUCT_URL
        )

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

        old_price_num = normalize_price(
            old_price
        )

        new_price_num = normalize_price(
            new_price
        )

        if old_price_num == new_price_num:

            logger.info(
                "Price unchanged."
            )

            return

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

        logger.exception(
            "Price monitor failed: %s",
            error,
        )