"""
Database session management for LanooBot.

This module creates the asynchronous SQLAlchemy engine
and provides async database sessions.

Production database:
PostgreSQL + asyncpg
"""

from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from app.config import settings


# Convert Railway's default PostgreSQL URL format
# into SQLAlchemy async format.
database_url = settings.database_url.replace(
    "postgresql://",
    "postgresql+asyncpg://",
)


# Async SQLAlchemy engine.
engine = create_async_engine(
    database_url,
    echo=False,
    pool_pre_ping=True,
)


# Factory for creating async database sessions.
AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


async def close_database() -> None:
    """
    Dispose database connections during application shutdown.
    """

    await engine.dispose()