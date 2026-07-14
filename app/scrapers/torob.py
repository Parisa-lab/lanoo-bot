import re
import httpx
from bs4 import BeautifulSoup


async def get_price(url: str):

    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Linux; Android 14)"
            " AppleWebKit/537.36"
            " Chrome/124.0.0.0 Mobile Safari/537.36"
        )
    }

    async with httpx.AsyncClient(
        headers=headers,
        follow_redirects=True,
        timeout=30
    ) as client:

        response = await client.get(url)

    soup = BeautifulSoup(response.text, "html.parser")

    # نام محصول
    title = ""

    title_tag = soup.select_one("h1.Showcase_name1__kioZg")

    if title_tag:
        title = title_tag.get_text(strip=True)

    # فروشنده و قیمت
    seller = ""
    price = ""

    boxes = soup.select("div.actions_buy_box_text__Ng2e8")

    if len(boxes) >= 2:
        seller = boxes[0].get_text(strip=True)
        price = boxes[1].get_text(strip=True)

    # عکس
    image = ""

    img = soup.select_one("div.Showcase_showcase__I1Z3f img")

    if img:
        image = img.get("src", "")

    return {
        "title": title,
        "price": price,
        "seller": seller,
        "image": image
    }