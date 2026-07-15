from telegram import Update
from telegram.ext import ContextTypes

from app.scrapers.torob import get_price


async def price_command(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
) -> None:

    print("PRICE COMMAND CALLED")
    print(context.args)

    await update.message.reply_text(
        "Command received."
    )

    if not context.args:

        await update.message.reply_text(
            "Usage:\n"
            "/price https://torob.com/p/xxxxxxxx/"
        )
        return

    url = context.args[0]

    try:

        await update.message.reply_text(
            "Fetching product..."
        )

        data = await get_price(url)

        print(data)

        title = data.get(
            "title",
            "Unknown Product",
        )

        seller = data.get(
            "seller",
            "Unknown Seller",
        )

        price = data.get(
            "price",
            "Unknown Price",
        )

        image = data.get(
            "image",
            "",
        )

        message = (
            f"📦 {title}\n\n"
            f"🏪 {seller}\n"
            f"💰 {price}\n\n"
            f"🖼 {image}"
        )

        await update.message.reply_text(
            message
        )

        print("MESSAGE SENT")

    except Exception as error:

        print(error)

        await update.message.reply_text(
            f"ERROR:\n{error}"
        )