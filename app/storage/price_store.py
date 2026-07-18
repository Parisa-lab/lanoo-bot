"""
price_store.py

Persistent storage for prices.
"""

from pathlib import Path


DATA_DIR = Path("database")
DATA_DIR.mkdir(exist_ok=True)

PRICE_FILE = DATA_DIR / "last_price.txt"


def load_price() -> str | None:
    """
    Load saved price.
    """

    if not PRICE_FILE.exists():
        return None

    return PRICE_FILE.read_text(
        encoding="utf-8"
    ).strip()


def save_price(
    price: str,
) -> None:
    """
    Save latest price.
    """

    PRICE_FILE.write_text(
        price,
        encoding="utf-8",
    )