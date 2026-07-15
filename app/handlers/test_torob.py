import app.scrapers.torob as torob

async def torob_test(update, context):

    await update.message.reply_text(
        torob.__file__
    )