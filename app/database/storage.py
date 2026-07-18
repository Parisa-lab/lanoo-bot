"""
storage.py

Simple JSON storage layer.

Can be replaced later with:
- SQLite
- PostgreSQL
- Redis
- MongoDB
without changing business logic.
"""

from pathlib import Path
import json


DATA_DIR = Path("app/database")
DATA_DIR.mkdir(
    parents=True,
    exist_ok=True,
)

PRICE_FILE = DATA_DIR / "prices.json"


def load_prices() -> dict:

    if not PRICE_FILE.exists():
        return {}

    try:

        return json.loads(
            PRICE_FILE.read_text(
                encoding="utf-8"
            )
        )

    except Exception:

        return {}


def save_prices(
    data: dict,
) -> None:

    PRICE_FILE.write_text(
        json.dumps(
            data,
            ensure_ascii=False,
            indent=4,
        ),
        encoding="utf-8",
    )


def get_price(
    product_id: str,
) -> str | None:

    data = load_prices()

    return data.get(product_id)


def set_price(
    product_id: str,
    price: str,
) -> None:

    data = load_prices()

    data[product_id] = price

    save_prices(data)