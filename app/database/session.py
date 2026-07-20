"""
Database session management.

This module creates the SQLAlchemy async engine and session factory
used throughout the application.

Supported databases:

- PostgreSQL (recommended)

Environment:
DATABASE_URL=postgresql+asyncpg://...

Author: Lanoo
"""

from sqlalchemy.ext.asyncio import (
    AsyncSession,
)
from sqlalchemy.ext.asyncio import (
    async_sessionmaker,
)
from sqlalchemy.ext.asyncio import (
    create_async_engine,
)

from app.config import settings


# ---------------------------------------------------------------------
# Database Engine
# ---------------------------------------------------------------------

engine = create_async_engine(
    settings.database_url,
    echo=False,
    pool_pre_ping=True,
    pool_size=10,
    max_overflow=20,
)


# ---------------------------------------------------------------------
# Session Factory
# ---------------------------------------------------------------------

AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


async def get_session():
    """
    Yield a database session.

    Useful for dependency injection and testing.
    """

    async with AsyncSessionLocal() as session:
        yield session


async def close_database() -> None:
    """
    Gracefully dispose database connections.
    """

    await engine.dispose()