"""
Database session management.

Creates the async SQLAlchemy engine and session factory
used by the Lanoo application.

Author: Lanoo
"""

from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from app.config import settings


engine = create_async_engine(
    settings.database_url,
    echo=False,
    pool_pre_ping=True,
)


AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


async def get_session():
    """
    Provide an async database session.

    Used by repositories and dependency injection.
    """

    async with AsyncSessionLocal() as session:
        yield session


async def close_database() -> None:
    """
    Close database connections gracefully.
    """

    await engine.dispose()