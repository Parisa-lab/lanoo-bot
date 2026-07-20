from sqlalchemy import select

from app.database.models import PriceHistory
from app.database.models import TrackedProduct
from app.database.session import AsyncSessionLocal


async def add_product(
    chat_id: int,
    url: str,
    title: str,
    price: str,
) -> TrackedProduct:

    async with AsyncSessionLocal() as session:

        product = TrackedProduct(
            chat_id=chat_id,
            url=url,
            title=title,
            last_price=price,
        )

        session.add(product)

        await session.commit()
        await session.refresh(product)

        return product


async def get_products_by_chat(
    chat_id: int,
):

    async with AsyncSessionLocal() as session:

        result = await session.execute(
            select(TrackedProduct).where(
                TrackedProduct.chat_id == chat_id
            )
        )

        return result.scalars().all()


async def get_all_products():

    async with AsyncSessionLocal() as session:

        result = await session.execute(
            select(TrackedProduct)
        )

        return result.scalars().all()


async def update_price(
    product_id: int,
    new_price: str,
):

    async with AsyncSessionLocal() as session:

        product = await session.get(
            TrackedProduct,
            product_id,
        )

        if not product:
            return

        product.last_price = new_price

        session.add(
            PriceHistory(
                product_id=product.id,
                price=new_price,
            )
        )

        await session.commit()