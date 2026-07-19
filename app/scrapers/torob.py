"""
torob.py

Torob scraper.

Extract:
- Product title
- Cheapest price
- Image

Works with current Torob HTML.
"""

import logging
import re

import httpx
from bs4 import BeautifulSoup

logger = logging.getLogger(__name__)


async def get_price(
    url: str,
) -> dict | None:

    headers = {
        "User-Agent": (
            "Mozilla/5.0 "
            "(Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 "
            "(KHTML, like Gecko) "
            "Chrome/138.0.0.0 "
            "Safari/537.36"
        ),
        "Accept": (
            "text/html,"
            "application/xhtml+xml,"
            "application/xml;q=0.9,"
            "image/avif,"
            "image/webp,"
            "*/*;q=0.8"
        ),
        "Accept-Language": "fa-IR,fa;q=0.9",
        "Cache-Control": "no-cache",
    }

    try:

        async with httpx.AsyncClient(
            headers=headers,
            follow_redirects=True,
            timeout=30,
        ) as client:

            response = await client.get(
                url
            )

        if response.status_code == 429:

            logger.warning(
                "Torob rate limit reached."
            )

            return None

        response.raise_for_status()

        html = response.text

        soup = BeautifulSoup(
            html,
            "html.parser",
        )

        # =========================
        # TITLE
        # =========================

        title = "نامشخص"

        title_tag = soup.find(
            "title"
        )

        if title_tag:

            title = title_tag.get_text(
                strip=True
            )

            title = (
                title.replace(
                    "| ترب",
                    "",
                )
                .replace(
                    "خرید و قیمت",
                    "",
                )
                .strip()
            )

        # =========================
        # PRICE
        # =========================

        price = "نامشخص"

        price_match = re.search(
            r"ارزانترین فروشنده این محصول را\s*(.*?)\s*می‌فروشد",
            html,
        )

        if price_match:

            price = (
                price_match.group(1)
                .strip()
            )

        # =========================
        # IMAGE
        # =========================

        image = ""

        image_match = re.search(
            r'"twitter:image"\s+content="([^"]+)"',
            html,
        )

        if image_match:

            image = (
                image_match.group(1)
                .strip()
            )

        result = {
            "title": title,
            "seller": "نامشخص",
            "price": price,
            "image": image,
        }

        logger.info(
            f"SCRAPER RESULT: {result}"
        )

        return result

    except Exception:

        logger.exception(
            "Torob scraping failed."
        )

        return None


if __name__ == "__main__":

    import asyncio

    TEST_URL = (
        "https://torob.com/p/"
        "f498b27b-596c-47c8-a48d-0beed264b2d8/"
    )

    result = asyncio.run(
        get_price(TEST_URL)
    )

    print(result)