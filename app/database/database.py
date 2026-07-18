"""
database.py

SQLite database layer.
"""

import sqlite3
from pathlib import Path

DB_FILE = Path(
    "app/database/lanoo.db"
)


def get_connection():

    return sqlite3.connect(
        DB_FILE
    )


def initialize_database() -> None:
    """
    Create database tables.
    """

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS prices (
            product_url TEXT PRIMARY KEY,
            price TEXT NOT NULL
        )
        """
    )

    conn.commit()

    conn.close()


def get_price(
    product_url: str,
) -> str | None:

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT price
        FROM prices
        WHERE product_url = ?
        """,
        (
            product_url,
        ),
    )

    row = cursor.fetchone()

    conn.close()

    if row is None:
        return None

    return row[0]


def set_price(
    product_url: str,
    price: str,
) -> None:

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT OR REPLACE INTO prices
        (
            product_url,
            price
        )
        VALUES
        (
            ?,
            ?
        )
        """,
        (
            product_url,
            price,
        ),
    )

    conn.commit()

    conn.close()