def __init__(self) -> None:

    setup_logging()

    logger.info(
        "Initializing Lanoo Bot..."
    )

    self.application = (
        Application.builder()
        .token(settings.bot_token)
        .build()
    )

    initialize_database()

    self.application.add_error_handler(
        error_handler
    )

    logger.info(
        "Telegram Application created successfully."
    )