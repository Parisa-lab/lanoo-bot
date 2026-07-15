"""
torob.py

Torob HTML scraper.

Extract:
- Product title
- Cheapest seller
- Cheapest price
- Main image
"""
raise Exception("TOROB FILE LOADED")


import httpx
from bs4 import BeautifulSoup


async def get_price(url: str) -> dict:

    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Linux; Android 14) "
            "AppleWebKit/537.36 "
            "Chrome/124.0.0.0 Mobile Safari/537.36"
        )
    }

    async with httpx.AsyncClient(
        headers=headers,
        follow_redirects=True,
        timeout=30,
    ) as client:

        response = await client.get(url)

    response.raise_for_status()

    soup = BeautifulSoup(
        response.text,
        "html.parser",
    )

    # --------------------------------------------------
    # Product title
    # --------------------------------------------------

    title = "نامشخص"

    title_tag = soup.select_one(
        "h1.Showcase_name1__kioZg"
    )

    if title_tag:
        title = title_tag.get_text(
            strip=True
        )

    # --------------------------------------------------
    # Cheapest seller
    # --------------------------------------------------

    seller = "نامشخص"

    seller_boxes = soup.select(
        "div.actions_buy_box_text__Ng2e8"
    )

    if len(seller_boxes) >= 1:
        seller = seller_boxes[0].get_text(
            strip=True
        )

    # --------------------------------------------------
    # Cheapest price
    # --------------------------------------------------

    price = "نامشخص"

    if len(seller_boxes) >= 2:
        price = seller_boxes[1].get_text(
            strip=True
        )

    # --------------------------------------------------
    # Main image
    # --------------------------------------------------

    image = ""

    img_tag = soup.select_one(
        "div.Showcase_showcase__I1Z3f img"
    )

    if img_tag:

        image = (
            img_tag.get("src")
            or ""
        )

    # --------------------------------------------------
    # Return result
    # --------------------------------------------------

    return {
        "title": title,
        "seller": seller,
        "price": price,
        "image": image,
    }


# ------------------------------------------------------
# Local test
# ------------------------------------------------------

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