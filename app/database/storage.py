from pathlib import Path

DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)

PRICE_FILE = DATA_DIR / "last_price.txt"


def load_price():
    if not PRICE_FILE.exists():
        return None

    return PRICE_FILE.read_text(
        encoding="utf-8"
    ).strip()


def save_price(price: str):
    PRICE_FILE.write_text(
        price,
        encoding="utf-8",
    )