"""
main.py
"""

import asyncio
from app.scrapers.torob import get_price


raise Exception("MAIN FILE LOADED")


if __name__ == "__main__":

    result = asyncio.run(
        get_price(
            "https://torob.com/p/f498b27b-596c-47c8-a48d-0beed264b2d8/"
        )
    )

    print(result)