import logging

def configure_logger(level: str = "INFO", name: str = "vision_pipeline") -> logging.Logger:
    """
    Configure and return the application logger.
    """

    logging.basicConfig(
        level=getattr(logging, level.upper()),
        format="[%(name)s] [%(levelname)s] %(message)s", # %(asctime)s
        # datefmt="%Y-%m-%d %H:%M:%S", 
    )

    return logging.getLogger(name)