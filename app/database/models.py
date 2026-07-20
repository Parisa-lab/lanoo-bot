from datetime import datetime

from sqlalchemy import BigInteger
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import UniqueConstraint
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship


class Base(DeclarativeBase):
    pass


class TrackedProduct(Base):

    __tablename__ = "tracked_products"

    __table_args__ = (
        UniqueConstraint(
            "chat_id",
            "url",
            name="uq_chat_product",
        ),
    )

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True,
    )

    chat_id: Mapped[int] = mapped_column(
        BigInteger,
        index=True,
    )

    url: Mapped[str] = mapped_column(
        String(1000),
        nullable=False,
    )

    title: Mapped[str] = mapped_column(
        String(1000),
        nullable=False,
    )

    last_price: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
    )

    price_history: Mapped[list["PriceHistory"]] = relationship(
        back_populates="product",
        cascade="all, delete-orphan",
    )


class PriceHistory(Base):

    __tablename__ = "price_history"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True,
    )

    product_id: Mapped[int] = mapped_column(
        ForeignKey(
            "tracked_products.id",
            ondelete="CASCADE",
        ),
        nullable=False,
    )

    price: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
    )

    product: Mapped["TrackedProduct"] = relationship(
        back_populates="price_history",
    )