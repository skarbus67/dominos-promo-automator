import logging
from logging.handlers import RotatingFileHandler

def setup_logger():
    logger = logging.getLogger('dominos_automator')
    logger.setLevel(logging.DEBUG)

    file_log_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    console_log_format = logging.Formatter('%(message)s')

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(console_log_format)

    file_handler = RotatingFileHandler(
        'logs/automator.log',
        maxBytes=5*1024*1024,
        backupCount=10,
        encoding='utf-8'
    )
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(file_log_format)

    if not logger.handlers:
        logger.addHandler(console_handler)
        logger.addHandler(file_handler)

    return logger


logger = setup_logger()