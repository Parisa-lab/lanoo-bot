from app.config import settings
from app.bot import LanooBot

if __name__ == "__main__":

    print("BOT_TOKEN =", settings.bot_token)
    print("ENVIRONMENT =", settings.environment)
    print("DEBUG =", settings.debug)

    bot = LanooBot()

    bot.run()