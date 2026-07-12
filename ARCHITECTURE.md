# Lanoo Architecture

## Overview

Lanoo is a Telegram bot that helps users compare prices of baby and family products.

The project is designed with a layered architecture.

Each module has a single responsibility.

The goal is to keep the code clean, maintainable, and easy to extend.

---

# Project Structure

```
lanoo-bot/

app/
│
├── handlers/
├── services/
├── scrapers/
├── database/
├── keyboards/
├── models/
├── utils/
│
├── bot.py
├── config.py
├── constants.py
├── logger.py
├── messages.py
└── __init__.py

tests/

docs/

main.py
README.md
requirements.txt
Procfile
railway.json
```

---

# Folder Responsibilities

## handlers/

Responsible for handling Telegram commands.

Examples:

- /start
- /help
- /price

Handlers should never contain business logic.

Handlers should only:

- Receive user input.
- Validate simple input.
- Call the appropriate service.
- Send the response back.

---

## services/

Contains business logic.

Examples:

- Search product prices.
- Compare offers.
- Calculate discounts.

Services should never communicate directly with Telegram.

---

## scrapers/

Responsible for collecting data from websites.

Examples:

- Torob
- Digikala
- Amazon
- Trendyol

Scrapers should only return structured data.

---

## database/

Responsible for database operations.

Examples:

- Save users.
- Save products.
- Save alerts.
- Read history.

No Telegram code belongs here.

---

## keyboards/

Contains Telegram keyboards.

Examples:

- Reply Keyboard
- Inline Keyboard

No business logic belongs here.

---

## models/

Contains application models.

Examples:

- Product
- User
- Alert

---

## utils/

Contains helper functions.

Examples:

- Date formatting.
- Currency formatting.
- Validation.

---

# Core Files

## main.py

Project entry point.

Starts the application.

Nothing else.

---

## bot.py

Creates the Telegram Application.

Registers handlers.

Starts polling.

---

## config.py

Loads configuration from environment variables.

Never store secrets inside the source code.

---

## constants.py

Stores application constants.

Examples:

- Bot name
- Version
- Command names

---

## messages.py

Stores every message shown to users.

Never hardcode user-facing text inside handlers.

---

## logger.py

Responsible for logging.

Avoid using print() except during very early development.

---

# Design Rules

## Rule 1

One responsibility per file.

---

## Rule 2

One responsibility per function.

---

## Rule 3

Never hardcode secrets.

Use environment variables.

---

## Rule 4

Never duplicate code.

Extract reusable logic.

---

## Rule 5

Keep handlers small.

Business logic belongs inside services.

---

## Rule 6

Use descriptive names.

Bad:

```
x
```

Good:

```
product_name
```

---

## Rule 7

Keep functions short.

Target:

Less than 40 lines.

---

## Rule 8

Every function must have:

- Type hints
- Docstring

---

## Rule 9

Every important code block should contain comments explaining WHY it exists.

---

## Rule 10

Follow PEP 8.

---

# Data Flow

```
User

↓

Telegram

↓

Handler

↓

Service

↓

Scraper / Database

↓

Service

↓

Handler

↓

Telegram

↓

User
```

---

# Future Features

The architecture is designed to support:

- Price comparison
- Price history
- Price alerts
- Favorites
- Admin panel
- Multiple languages
- PostgreSQL
- REST API
- Docker
- CI/CD

without major restructuring.

---

# Philosophy

Clean code is more important than clever code.

Readable code is better than short code.

Simple solutions are preferred over complex ones.

The project should always be easy to understand for a new developer.