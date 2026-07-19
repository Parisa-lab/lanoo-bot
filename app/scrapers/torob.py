"""
torob.py

Torob HTML scraper.

Extract:
- Product title
- Cheapest seller
- Cheapest price
- Main image
"""

import logging

import httpx
from bs4 import BeautifulSoup

logger = logging.getLogger(__name__)


async def get_price(url: str) -> dict | None:

    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/138.0.0.0 Safari/537.36"
        ),
        "Accept": (
            "text/html,application/xhtml+xml,"
            "application/xml;q=0.9,image/avif,"
            "image/webp,*/*;q=0.8"
        ),
        "Accept-Language": "en-US,en;q=0.9",
        "Cache-Control": "no-cache",
    }

    async with httpx.AsyncClient(
        headers=headers,
        follow_redirects=True,
        timeout=30,
    ) as client:

        response = await client.get(url)

    if response.status_code == 429:

        logger.warning(
            "Torob rate limit reached (429)."
        )

        return None

    response.raise_for_status()

    soup = BeautifulSoup(
        response.text,
        "html.parser",
    )

    title = "نامشخص"

    title_tag = soup.select_one(
        "h1.Showcase_name1__kioZg"
    )

    if title_tag:
        title = title_tag.get_text(
            strip=True
        )

    seller = "نامشخص"

    seller_boxes = soup.select(
        "div.actions_buy_box_text__Ng2e8"
    )

    if len(seller_boxes) >= 1:
        seller = seller_boxes[0].get_text(
            strip=True
        )

    price = "نامشخص"

    if len(seller_boxes) >= 2:
        price = seller_boxes[1].get_text(
            strip=True
        )

    image = ""

    img_tag = soup.select_one(
        "div.Showcase_showcase__I1Z3f img"
    )

    if img_tag:

        image = (
            img_tag.get("src")
            or ""
        )

    return {
        "title": title,
        "seller": seller,
        "price": price,
        "image": image,
    }


if __name__ == "__main__":

    import asyncio

    TEST_URL = (
        "https://torob.com/p/"
        "facdcb68-43fb-432a-9088-7bbf4ff45f23/"
    )

    result = asyncio.run(
        get_price(TEST_URL)
    )

    print(result)