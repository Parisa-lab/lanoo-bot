from telegram import Update
from telegram.ext import ContextTypes


from app.scrapers.torob import get_price



from app.database.repository import add_product
from app.database.repository import get_product_by_url




async def add_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    """
    Add a product URL to the tracking database.
    """

    if not update.message:
        return

    if not context.args:
        await update.message.reply_text(
            "Usage:\n/add URL"
        )
        return

    url = context.args[0]

    data = await get_price(url)

    if not data:
        await update.message.reply_text(
            "Unable to fetch product."
        )
        return

    await add_product(
        chat_id=update.message.chat_id,
        url=url,
        title=data["title"],
        price=data["price"],
    )

    await update.message.reply_text(
        f"Added:\n{data['title']}"
    )