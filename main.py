"""
Application entry point for Lanoo.

Responsibilities:

- Configure logging
- Create database tables
- Start the Telegram bot
- Handle startup failures gracefully

Author: Lanoo
"""

import asyncio
import logging
import sys

from app.bot import LanooBot
from app.database.models import Base
from app.database.session import engine

---------------------------------------------------------------------

Logging Configuration

---------------------------------------------------------------------

logging.basicConfig(
level=logging.INFO,
format=(
"%(asctime)s | "
"%(levelname)s | "
"%(name)s | "
"%(message)s"
),
)

logger = logging.getLogger(name)

---------------------------------------------------------------------

Database Initialization

---------------------------------------------------------------------

async def create_tables() -> None:
"""
Create database tables if they do not exist.

SQLAlchemy will compare the ORM models against the database
and create missing tables.
"""

async with engine.begin() as conn:
    await conn.run_sync(
        Base.metadata.create_all
    )

async def startup() -> None:
"""
Perform application startup tasks.
"""

logger.info(
    "Initializing database..."
)

await create_tables()

logger.info(
    "Database initialization completed."
)

---------------------------------------------------------------------

Main Application

---------------------------------------------------------------------

def main() -> None:
"""
Application entry point.
"""

try:

    asyncio.run(
        startup()
    )

    logger.info(
        "Starting Telegram bot..."
    )

    bot = LanooBot()
    bot.run()

except KeyboardInterrupt:

    logger.info(
        "Application stopped by user."
    )

except Exception:

    logger.exception(
        "Fatal application error."
    )

    sys.exit(1)

if name == "main":
main()