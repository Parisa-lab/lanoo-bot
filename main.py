"""
Application entry point for Lanoo.

Initializes the database and starts the Telegram bot.
"""

import asyncio
import logging
import sys

from app.bot import LanooBot
from app.database.models import Base
from app.database.session import engine

logging.basicConfig(
level=logging.INFO,
format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
)

logger = logging.getLogger(name)

async def create_tables() -> None:
"""
Create database tables if they do not already exist.
"""

async with engine.begin() as conn:
    await conn.run_sync(
        Base.metadata.create_all
    )

async def startup() -> None:
"""
Run startup tasks.
"""

logger.info(
    "Creating database tables..."
)

await create_tables()

logger.info(
    "Database ready."
)

def main() -> None:
"""
Main application entry point.
"""

try:

    asyncio.run(
        startup()
    )

    logger.info(
        "Starting bot..."
    )

    bot = LanooBot()

    bot.run()

except KeyboardInterrupt:

    logger.info(
        "Application stopped."
    )

except Exception:

    logger.exception(
        "Fatal startup error."
    )

    sys.exit(1)

if name == "main":
main()