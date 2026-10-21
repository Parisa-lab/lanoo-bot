# Lanoo Architecture

## Overview

Lanoo is an asynchronous Telegram bot that tracks product prices on [Torob](https://torob.com), an Iranian price-comparison website. A user sends a Torob product link; the bot reads the product's price from the page, saves the product for that chat, and a background job checks every tracked product every 5 minutes. When a price changes, the bot messages the chat.

The code is split into layers. Each layer has one job and only talks to the layer next to it:

- Handlers talk to Telegram.
- Services hold the logic.
- The scraper reads Torob.
- The repository talks to the database.

## Project structure

```text
lanoo-bot/
├── main.py
├── requirements.txt
├── Procfile
├── .env.example
├── README.md
├── ARCHITECTURE.md
├── CHANGELOG.md
├── CONTRIBUTING.md
└── app/
    ├── bot.py
    ├── config.py
    ├── container.py
    ├── handlers/
    ├── services/
    ├── scrapers/
    ├── repositories/
    ├── database/
    ├── jobs/
    ├── models/
    ├── enums/
    ├── storage/
    ├── telegram/
    ├── data/
    ├── constants.py
    ├── error_handler.py
    ├── logger.py
    ├── message_formatter.py
    ├── messages.py
    ├── telegram_config.py
    └── railway.json
```

The sections below describe the parts the running bot uses. Parts that are not used yet are listed under [Modules not used by the running bot](#modules-not-used-by-the-running-bot).

## Data flow

Looking up and tracking a product (`/price` or `/add`):

```text
User
  -> Telegram
  -> handler (handlers/price.py or add.py)
  -> PriceService.track_product
       -> TorobScraper.get_price      (downloads and reads the Torob page)
       -> ProductRepository           (saves the product in PostgreSQL if it is new)
  -> handler sends the reply (name, image, price, "open on Torob" button)
```

Price-change alerts (runs without any user message):

```text
JobQueue (every 300 seconds)
  -> MonitoringService.check_prices
       -> ProductRepository           (loads every tracked product)
       -> TorobScraper.get_price      (reads the current price)
       -> compares the two prices as numbers
       -> NotificationService         (messages the chat if they differ)
       -> ProductRepository.update_price (saves the new price and a history row)
```

## Entry points

| File | What it does |
|---|---|
| `main.py` | Entry point. Creates the database tables if they do not exist, then starts the bot and stops with an error message if startup fails. |
| `app/bot.py` | `LanooBot` builds the Telegram application, registers the command handlers and the price-monitor job, adds an error handler and starts polling. |
| `app/config.py` | Loads `BOT_TOKEN` and `DATABASE_URL` from environment variables or `.env` with pydantic-settings. No secret is stored in the code. |
| `app/container.py` | Creates the shared `ProductRepository`, `TorobScraper` and `PriceService` once so handlers and the job use the same objects. |

## Layers

### `handlers/`

One file per Telegram command, registered in `handlers/__init__.py`: `/start`, `/help`, `/price`, `/add` and `/list`. A handler checks that the command has the input it needs, calls a service, and sends the reply. It does not scrape pages or write to the database itself.

### `services/`

- `PriceService` looks up a product through the scraper and saves it through the repository if the chat is not already tracking it.
- `MonitoringService` compares each tracked product's saved price with its current price. It first converts prices to numbers (Persian digits, thousands separators and the word "تومان" are removed), and skips a product if either price cannot be read.
- `NotificationService` sends the price-change message, including the old price, the new price and the link, through the Telegram bot.

Services do not use Telegram objects except `NotificationService`, which only sends messages.

### `scrapers/`

`TorobScraper` downloads a Torob product page with `httpx` and reads the title, image and price with BeautifulSoup and regular expressions. It returns the data as a dictionary and does not touch the database or Telegram. Because it reads the page HTML, a change to Torob's layout can break it.

### `repositories/` and `database/`

- `database/models.py` defines two SQLAlchemy tables: `tracked_products` (chat ID, URL, title, last price, creation time; unique per chat and URL) and `price_history` (product, price, time).
- `database/session.py` creates the async engine (PostgreSQL with asyncpg) and the session factory. A plain `postgresql://` URL is converted to the async format.
- `repositories/product_repository.py` (`ProductRepository`) adds products, finds them by chat or URL, lists all products, and updates a price while writing a `price_history` row. `PriceService` and `MonitoringService` use this class.
- `database/repository.py` contains plain-function versions of the same queries. Only the `/list` handler uses it. See the note below.

### `jobs/`

`jobs/price_monitor.py` registers a repeating job with python-telegram-bot's job queue. It first runs 10 seconds after startup, then every 300 seconds.

### `messages.py`

Holds the text of the bot's messages. Most handlers currently contain their own short message strings, so this module is not used yet.

## Deployment

The `Procfile` starts the bot as a worker (`python main.py`). `app/railway.json` sets a restart policy for Railway: restart on failure, up to 10 times. The bot needs `BOT_TOKEN` and `DATABASE_URL`.

## Modules not used by the running bot

These files are in the repository but nothing the bot runs imports them. They are leftovers from earlier versions or ideas for later:

- `app/models/product.py` and `app/message_formatter.py`: a Pydantic `Product` model and a message formatter. The handlers build their messages directly.
- `app/storage/price_store.py`: saves a single price to a text file. The bot stores prices in PostgreSQL instead.
- `app/telegram/`: helper functions for sending Telegram messages.
- `app/error_handler.py`: a more detailed error handler. `bot.py` has its own simpler one.
- `app/logger.py`, `app/constants.py`, `app/enums/`, `app/telegram_config.py`, `app/data/products.json`: configuration and data files that nothing imports yet.

Known inconsistencies:

- The same database queries exist twice, as `ProductRepository` methods and as functions in `database/repository.py`. Moving `/list` to `ProductRepository` would remove the duplicate.
- The `/list` handler calls `get_products_by_chat` from `database/repository.py`, while the other handlers go through `PriceService`.

## Design rules

- One responsibility per file and per function.
- No secrets in the source code; use environment variables.
- Do not duplicate code; extract shared logic.
- Keep handlers small and put logic in services.
- Use descriptive names, type hints and docstrings.
- Follow PEP 8.

## Possible improvements

- A command to stop tracking a product.
- Automated tests.
- Reading the seller name, which is currently shown as unknown.
- Merging the two repository modules.
