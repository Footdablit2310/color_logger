import logging

def create_logger(name: str, clear_handlers: bool = True, default_level: int = logging.DEBUG) -> logging.Logger:
    """Creates a colored logger with the specified name and configuration."""