import json
from pathlib import Path

DB_FILE = Path("data/products.json")


def load_products():

    if not DB_FILE.exists():
        return []

    with open(
        DB_FILE,
        "r",
        encoding="utf-8",
    ) as file:

        return json.load(file)


def save_products(products):

    with open(
        DB_FILE,
        "w",
        encoding="utf-8",
    ) as file:

        json.dump(
            products,
            file,
            ensure_ascii=False,
            indent=2,
        )