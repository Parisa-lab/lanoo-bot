# Contributing to Lanoo

Thank you for contributing to Lanoo.

Our goal is to build a clean, maintainable, and production-ready Telegram bot.

Please read these guidelines before contributing.

---

# Code Style

Follow the PEP 8 style guide.

Write readable code.

Readable code is always preferred over clever code.

---

# Project Structure

Every file should have only one responsibility.

Examples:

- handlers -> Telegram commands
- services -> Business logic
- scrapers -> Website scraping
- database -> Database operations
- keyboards -> Telegram keyboards
- utils -> Helper functions

---

# Functions

Every function must:

- Have a clear name.
- Have type hints.
- Have a docstring.
- Stay as short as possible.

Target:

Less than 40 lines.

---

# Variables

Use descriptive names.

Good:

product_name

Bad:

x

---

# Constants

Never hardcode values that may change.

Store them inside:

app/constants.py

---

# Messages

Never write user-facing text inside handlers.

Store every message inside:

app/messages.py

---

# Secrets

Never commit secrets.

Examples:

- Bot Token
- API Keys
- Database Password

Use environment variables instead.

---

# Comments

Write comments that explain WHY.

Avoid comments that only repeat WHAT the code already says.

Comments must be written in English.

---

# Imports

Group imports in this order:

1. Standard library

2. Third-party packages

3. Local project imports

Leave one blank line between groups.

---

# Commits

Use meaningful commit messages.

Examples:

feat: add start command

fix: handle missing message

refactor: split handlers

docs: update architecture

style: format code

---

# Pull Requests

Keep pull requests small.

One feature per pull request.

Explain why the change is needed.

---

# Testing

New features should include tests whenever possible.

---

# Philosophy

Keep the code simple.

Keep the code readable.

Think about future maintenance before writing code.

Every decision should make the project easier to extend.