"""
Price monitoring job for Lanoo.

This module is responsible for:
- Checking tracked products periodically.
- Fetching current prices from scrapers.
- Detecting price changes.
- Notifying users through Telegram.
- Updating stored prices.

The job is registered through register_price_monitor_job()
and executed by python-telegram-bot JobQueue.
"""

import logging

from telegram.ext import ContextTypes

from app.database.repository import get_all_products
from app.database.repository import update_price
from app.scrapers.torob import get_price


logger = logging.getLogger(__name__)


def normalize_price(price: str) -> int:
    """
    Convert Persian or formatted price text into an integer.

    Examples:
        "۱٬۲۰۰٬۰۰۰ تومان" -> 1200000
        "1,200,000" -> 1200000

    Args:
        price:
            Price string.

    Returns:
        Integer representation of the price.
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
        .replace("٬", "")
        .replace(",", "")
        .replace("٫", "")
        .replace(".", "")
        .replace("تومان", "")
        .replace(" ", "")
        .strip()
    )

    digits = "".join(
        character
        for character in cleaned
        if character.isdigit()
    )

    if not digits:
        return 0

    return int(digits)


async def check_prices(
    context: ContextTypes.DEFAULT_TYPE,
) -> None:
    """
    Check all tracked products and notify users
    when a price change is detected.

    Args:
        context:
            Telegram callback context.
    """

    try:

        products = await get_all_products()

        logger.info(
            "Checking %s tracked products",
            len(products),
        )

        for product in products:

            try:

                data = await get_price(
                    product.url,
                )

                if not data:

                    logger.warning(
                        "No scraper data for product %s",
                        product.id,
                    )

                    continue

                current_price = str(
                    data.get(
                        "price",
                        "",
                    )
                )

                old_price = str(
                    product.last_price,
                )

                current_price_num = normalize_price(
                    current_price,
                )

                old_price_num = normalize_price(
                    old_price,
                )

                logger.info(
                    "Product %s | old=%s | new=%s",
                    product.id,
                    old_price_num,
                    current_price_num,
                )

                if (
                    current_price_num == 0
                    or old_price_num == 0
                ):

                    logger.warning(
                        "Invalid price detected for product %s",
                        product.id,
                    )

                    continue

                if (
                    current_price_num
                    == old_price_num
                ):

                    logger.info(
                        "Price unchanged for product %s",
                        product.id,
                    )

                    continue

                await context.bot.send_message(
                    chat_id=product.chat_id,
                    text=(
                        "📉 Price Change Detected\n\n"
                        f"Product: {product.title}\n\n"
                        f"Old Price: {old_price}\n"
                        f"New Price: {current_price}\n\n"
                        f"{product.url}"
                    ),
                )

                await update_price(
                    product_id=product.id,
                    new_price=current_price,
                )

                logger.info(
                    "Price updated for product %s",
                    product.id,
                )

            except Exception:

                logger.exception(
                    "Failed processing product %s",
                    product.id,
                )

    except Exception:

        logger.exception(
            "Price monitor job failed",
        )


def register_price_monitor_job(
    application,
) -> None:
    """
    Register price monitoring as a recurring job.

    Args:
        application:
            Telegram Application instance.

    The job runs every hour and checks
    all tracked products for price changes.
    """

    if application.job_queue is None:

        logger.warning(
            "Job queue is unavailable. "
            "Price monitoring was not registered.",
        )

        return

    application.job_queue.run_repeating(
        check_prices,
        interval=3600,
        first=10,
        name="price_monitor",
    )

    logger.info(
        "Price monitoring job registered successfully",
    )