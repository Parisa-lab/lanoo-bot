"""
app/scrapers/torob.py
"""

import asyncio
import httpx
from bs4 import BeautifulSoup


async def get_price(url: str):

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

    soup = BeautifulSoup(response.text, "html.parser")

    # Product title
    title = ""

    title_tag = soup.select_one("h1.Showcase_name1__kioZg")

    if title_tag:
        title = title_tag.get_text(strip=True)

    # Seller and price
    seller = ""
    price = ""

    boxes = soup.select("div.actions_buy_box_text__Ng2e8")

    if len(boxes) >= 2:
        seller = boxes[0].get_text(strip=True)
        price = boxes[1].get_text(strip=True)

    # Product image
    image = ""

    img = soup.select_one("div.Showcase_showcase__I1Z3f img")

    if img:
        image = img.get("src", "")

    return {
        "title": title,
        "price": price,
        "seller": seller,
        "image": image,
    }


if __name__ == "__main__":

    url = (
        "https://torob.com/p/"
        "f498b27b-596c-47c8-a48d-0beed264b2d8/"
    )

    result = asyncio.run(get_price(url))

    print(result)