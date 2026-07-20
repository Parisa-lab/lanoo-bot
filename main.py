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

logger = logging.getLogger(__name__)


async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(
            Base.metadata.create_all
        )


async def startup():
    logger.info("Creating database tables...")
    await create_tables()
    logger.info("Database ready.")


def main():
    try:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

        loop.run_until_complete(
            startup()
        )

        logger.info("Starting bot...")

        bot = LanooBot()
        bot.run()

    except KeyboardInterrupt:
        logger.info("Application stopped.")

    except Exception:
        logger.exception(
            "Fatal startup error."
        )
        sys.exit(1)


if __name__ == "__main__":
    main()