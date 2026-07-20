from sqlalchemy import select


async def get_product_by_url(
    chat_id: int,
    url: str,
):

    async with AsyncSessionLocal() as session:

        result = await session.execute(
            select(TrackedProduct).where(
                TrackedProduct.chat_id == chat_id,
                TrackedProduct.url == url,
            )
        )

        return result.scalar_one_or_none()