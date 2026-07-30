"""
app/scrapers/torob.py
"""

from __future__ import annotations

import logging
import re
from typing import Any

import httpx
from bs4 import BeautifulSoup

logger = logging.getLogger(__name__)

_DIGIT_TRANSLATION_TABLE = str.maketrans(
    {
        "۰": "0",
        "۱": "1",
        "۲": "2",
        "۳": "3",
        "۴": "4",
        "۵": "5",
        "۶": "6",
        "۷": "7",
        "۸": "8",
        "۹": "9",
        "٠": "0",
        "١": "1",
        "٢": "2",
        "٣": "3",
        "٤": "4",
        "٥": "5",
        "٦": "6",
        "٧": "7",
        "٨": "8",
        "٩": "9",
        "٬": ",",
        "،": ",",
    }
)


class TorobScraper:

    def __init__(self, timeout: float = 30.0) -> None:
        self.timeout = timeout

    def _headers(self) -> dict[str, str]:
        return {
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
            "Accept-Language": "fa-IR,fa;q=0.9,en-US;q=0.8,en;q=0.7",
            "Cache-Control": "no-cache",
            "Pragma": "no-cache",
        }

    @staticmethod
    def _normalize_digits(value: str) -> str:
        return value.translate(
            _DIGIT_TRANSLATION_TABLE
        )

    @staticmethod
    def _clean_title(title: str) -> str:

        title = title.strip()
        title = title.replace(
            "| ترب",
            "",
        )
        title = title.replace(
            "خرید و قیمت",
            "",
        )
        title = re.sub(
            r"\s+",
            " ",
            title,
        )

        return title.strip() or "نامشخص"

    @staticmethod
    def _extract_meta(
        soup: BeautifulSoup,
        *,
        property_name: str | None = None,
        name: str | None = None,
    ) -> str:

        if property_name:

            tag = soup.find(
                "meta",
                attrs={
                    "property": property_name,
                },
            )

            if tag and tag.get("content"):
                return str(
                    tag.get("content")
                ).strip()

        if name:

            tag = soup.find(
                "meta",
                attrs={
                    "name": name,
                },
            )

            if tag and tag.get("content"):
                return str(
                    tag.get("content")
                ).strip()

        return ""

    @classmethod
    def _extract_title(
        cls,
        soup: BeautifulSoup,
    ) -> str:

        candidates = [
            cls._extract_meta(
                soup,
                property_name="og:title",
            ),
            cls._extract_meta(
                soup,
                name="twitter:title",
            ),
        ]

        title_tag = soup.find("title")

        if title_tag:
            candidates.append(
                title_tag.get_text(
                    strip=True
                )
            )

        for candidate in candidates:

            candidate = candidate.strip()

            if candidate:
                return cls._clean_title(
                    candidate
                )

        return "نامشخص"

    @classmethod
    def _extract_image(
        cls,
        soup: BeautifulSoup,
        html: str,
    ) -> str:

        candidates = [
            cls._extract_meta(
                soup,
                property_name="og:image",
            ),
            cls._extract_meta(
                soup,
                name="twitter:image",
            ),
        ]

        for candidate in candidates:

            candidate = candidate.strip()

            if not candidate:
                continue

            if candidate.startswith("//"):
                candidate = (
                    "https:" + candidate
                )

            return candidate

        match = re.search(
            r'"twitter:image"\s+content="([^"]+)"',
            html,
            flags=re.IGNORECASE,
        )

        if match:

            image = match.group(
                1
            ).strip()

            if image.startswith("//"):
                image = "https:" + image

            return image

        return ""

    @classmethod
    def _extract_price(
        cls,
        html: str,
    ) -> tuple[str, int | None]:

        patterns = [
            r"ارزانترین فروشنده این محصول را\s*(.*?)\s*می‌فروشد",
            r"ارزان‌ترین فروشنده این محصول را\s*(.*?)\s*می‌فروشد",
            r"([\d۰-۹٬,]+)\s*تومان",
            r"([\d۰-۹٬,]+)\s*ریال",
        ]

        for pattern in patterns:

            match = re.search(
                pattern,
                html,
                flags=re.DOTALL,
            )

            if not match:
                continue

            raw_price = (
                match.group(1)
                .strip()
            )

            raw_price = cls._normalize_digits(
                raw_price
            )

            raw_price = (
                raw_price
                .replace(",", "")
                .strip()
            )

            digits_only = re.sub(
                r"[^\d]",
                "",
                raw_price,
            )

            if not digits_only:
                continue

            price_value = int(
                digits_only
            )

            if "ریال" in pattern:
                display = (
                    f"{price_value:,} ریال"
                )
            else:
                display = (
                    f"{price_value:,} تومان"
                )

            return (
                display,
                price_value,
            )

        return (
            "نامشخص",
            None,
        )

    async def get_price(
        self,
        url: str,
    ) -> dict[str, Any] | None:

        if (
            not isinstance(url, str)
            or not url.strip()
        ):
            logger.warning(
                "Invalid Torob URL."
            )
            return None

        url = url.strip()

        try:

            async with httpx.AsyncClient(
                headers=self._headers(),
                follow_redirects=True,
                timeout=self.timeout,
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

            title = self._extract_title(
                soup
            )

            price, price_value = (
                self._extract_price(
                    html
                )
            )

            image = self._extract_image(
                soup,
                html,
            )

            logger.info(
                "Extracted image URL: %s",
                image,
            )

            result: dict[str, Any] = {
                "title": title,
                "store": "Torob",
                "seller": "نامشخص",
                "price": price,
                "price_value": price_value,
                "image": image,
                "url": url,
            }

            logger.info(
                "Torob scraping succeeded for URL: %s",
                url,
            )

            return result

        except httpx.HTTPStatusError as error:

            logger.warning(
                "Torob HTTP error for %s: %s",
                url,
                error,
            )

            return None

        except httpx.RequestError as error:

            logger.warning(
                "Torob network error for %s: %s",
                url,
                error,
            )

            return None

        except Exception:

            logger.exception(
                "Unexpected Torob scraping failure for URL: %s",
                url,
            )

            return None

    async def search(
        self,
        query: str,
    ) -> dict[str, Any] | None:

        return await self.get_price(
            query
        )


_default_scraper = TorobScraper()


async def get_price(
    url: str,
) -> dict[str, Any] | None:

    return await _default_scraper.get_price(
        url
    )


if __name__ == "__main__":

    import asyncio

    TEST_URL = (
        "https://torob.com/p/"
        "f498b27b-596c-47c8-a48d-0beed264b2d8/"
    )

    async def _main() -> None:

        result = await get_price(
            TEST_URL
        )

        print(result)

    asyncio.run(_main())