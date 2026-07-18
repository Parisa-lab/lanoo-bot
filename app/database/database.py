"""
database.py

SQLite database utilities.
"""

import sqlite3
from pathlib import Path

DATABASE_FILE = Path(
    "app/database/lanoo.db"
)


def init_database() -> None:
    """
    Create database and tables.
    """

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
            product_url TEXT NOT NULL,
            price TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
    )

    connection.commit()
    connection.close()