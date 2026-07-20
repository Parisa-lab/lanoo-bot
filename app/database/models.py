"""
Database models for the Lanoo Telegram Bot.

This module defines all SQLAlchemy ORM entities used by the application.
The schema is designed to support:

- Product tracking
- Multi-user monitoring
- Price history
- Future analytics features

Author: Lanoo
"""

from datetime import datetime

from sqlalchemy import BigInteger
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

class Base(DeclarativeBase):
"""
Base class for all ORM models.
"""

pass

class TrackedProduct(Base):
"""
Product tracked by a Telegram user.
"""

__tablename__ = "tracked_products"

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

class PriceHistory(Base):
"""
Historical prices for tracked products.
"""

__tablename__ = "price_history"

id: Mapped[int] = mapped_column(
    Integer,
    primary_key=True,
    autoincrement=True,
)

product_id: Mapped[int] = mapped_column(
    ForeignKey("tracked_products.id"),
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

"""