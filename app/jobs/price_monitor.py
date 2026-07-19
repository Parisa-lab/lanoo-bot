"""
price_monitor.py

Monitor Torob prices and notify only when price changes.
"""

import logging

from telegram.ext import ContextTypes

from app.scrapers.torob import get_price
from app.database.database import (
    get_price as get_saved_price,
    set_price,
)

logger = logging.getLogger(__name__)

PRODUCT_URL = (
    "https://torob.com/p/f498b27b-596c-47c8-a48d-0beed264b2d8/"
)

CHAT_ID = 625896200


def normalize_price(price: str) -> int:
    """
    Convert Persian price string to integer.

    Example:
    ۱۲٫۶۰۰٫۰۰۰ تومان
    ->
    12600000
    """

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
        .replace(".", "")
        .replace(",", "")
        .replace("تومان", "")
        .replace(" ", "")
        .strip()
    )

    digits_only = "".join(
        ch for ch in cleaned
        if ch.isdigit()
    )

    if not digits_only:
        return 0

    return int(digits_only)


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

        title = data.get(
            "title",
            "نامشخص",
        )

        seller = data.get(
            "seller",
            "نامشخص",
        )

        new_price = data.get(
            "price",
            "نامشخص",
        )

        old_price = get_saved_price(
            PRODUCT_URL
        )

        logger.info(
            f"Saved price: {old_price}"
        )

     

        
        old_price_num = normalize_price(
            old_price
        )

        new_price_num = normalize_price(
            new_price
        )

        if (
            old_price_num == 0
            or new_price_num == 0
        ):
            logger.warning(
                "Invalid price detected."
            )
            return

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
            "🔔 PRICE CHANGED\n\n"
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
            f"Monitor error: {error}"
        )