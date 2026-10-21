# Lanoo Bot

An asynchronous Telegram bot that tracks product prices on [Torob](https://torob.com), an Iranian price-comparison website. Send the bot a Torob product link and it shows the product's current price. It then checks the price every 5 minutes and sends you a message when it changes.

## Features

- **Price lookup:** send a Torob product URL and get the product name, an image (when the page has one) and the current price, with a button that opens the product on Torob.
- **Price tracking:** products you look up or add are saved per chat, and duplicates within the same chat are ignored.
- **Price-change alerts:** a background job checks every tracked product every 5 minutes and messages the chat with the old price, the new price and the product link.
- **Price history:** every detected change is stored in the database.
- **Persian digits:** prices written with Persian digits and thousands separators are converted to numbers before they are compared.

## Commands

| Command | What it does |
|---|---|
| `/start` | Starts the bot. |
| `/help` | Lists the available commands. |
| `/price <torob_url>` | Shows the product's current price and starts tracking it. |
| `/add <torob_url>` | Starts tracking the product and confirms with its name. |
| `/list` | Lists the products tracked in this chat with their last known price. |

Example:

```text
/price https://torob.com/p/xxxxxxxx/
```

## How it works

1. A command handler passes the URL to `PriceService`.
2. `TorobScraper` downloads the product page with `httpx` and reads the title, image and price with BeautifulSoup and regular expressions.
3. `ProductRepository` saves the product in PostgreSQL through SQLAlchemy's async API.
4. A repeating job from python-telegram-bot's job queue runs `MonitoringService`, which compares each product's saved price with its current price and sends a notification through `NotificationService` when they differ.

The code is split into layers (handlers, services, scrapers, repositories and database), and each layer has a single responsibility. See [ARCHITECTURE.md](ARCHITECTURE.md) for more detail.

## Technologies

- Python
- python-telegram-bot (with the job queue)
- httpx and BeautifulSoup
- SQLAlchemy (async) and asyncpg
- PostgreSQL
- pydantic-settings

## Setup

You need Python 3.11 or newer (recommended), a Telegram bot token and a PostgreSQL database.

1. Create a bot with [@BotFather](https://t.me/BotFather) on Telegram and copy its token.
2. Create a PostgreSQL database.
3. Clone the repository and install the dependencies:

   ```bash
   git clone https://github.com/Parisa-lab/lanoo-bot.git
   cd lanoo-bot
   python -m venv .venv
   source .venv/bin/activate    # on Windows: .venv\Scripts\activate
   python -m pip install -r requirements.txt
   ```

4. Copy `.env.example` to `.env` and fill in your values:

   ```text
   BOT_TOKEN=your_telegram_bot_token
   DATABASE_URL=postgresql+asyncpg://username:password@host:5432/database_name
   ```

   A plain `postgresql://...` URL also works; the app converts it to the async format.

5. Start the bot:

   ```bash
   python main.py
   ```

On startup the bot creates the `tracked_products` and `price_history` tables if they do not exist, then starts polling Telegram. Keep your `.env` file private; it is excluded from Git.

## Deployment

The repository includes a `Procfile` (`worker: python main.py`) so the bot can run as a worker process on platforms that support it. Set `BOT_TOKEN` and `DATABASE_URL` as environment variables on the platform.

## Limitations

- Only Torob product links are supported, and the bot reads the price from the page's HTML, so a change to Torob's page layout can break it.
- The seller name is not extracted, so it is shown as unknown.
- There is no command to stop tracking a product yet.
- Prices are kept as text in the unit Torob shows (Toman or Rial), with no currency conversion.
- There are no automated tests yet.
