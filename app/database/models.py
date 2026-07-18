"""
Database models.
"""

from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column,
)

from sqlalchemy import String
from sqlalchemy import BigInteger


class Base(DeclarativeBase):
    pass


class TrackedProduct(Base):

    __tablename__ = "tracked_products"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
    )

    chat_id: Mapped[int] = mapped_column(
        BigInteger,
    )

    url: Mapped[str] = mapped_column(
        String(1000),
    )

    title: Mapped[str] = mapped_column(
        String(1000),
    )

    last_price: Mapped[str] = mapped_column(
        String(255),
    )