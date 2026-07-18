"""
database.py
"""

import sqlite3
from pathlib import Path

DATABASE_FILE = Path(
    "app/database/lanoo.db"
)


def init_database() -> None:

    DATABASE_FILE.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    connection = sqlite3.connect(
        DATABASE_FILE
    )

    cursor = connection.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS prices (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_url TEXT UNIQUE,
            price TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
    )

    connection.commit()
    connection.close()


def get_price(
    product_url: str,
) -> str | None:

    connection = sqlite3.connect(
        DATABASE_FILE
    )

    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT price
        FROM prices
        WHERE product_url = ?
        ORDER BY id DESC
        LIMIT 1
        """,
        (product_url,),
    )

    row = cursor.fetchone()

    connection.close()

    if row:
        return row[0]

    return None


def set_price(
    product_url: str,
    price: str,
) -> None:

    connection = sqlite3.connect(
        DATABASE_FILE
    )

    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT OR REPLACE INTO prices
        (
            product_url,
            price
        )
        VALUES (?, ?)
        """,
        (
            product_url,
            price,
        ),
    )

    connection.commit()
    connection.close()