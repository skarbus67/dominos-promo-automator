import logging
import os

DOMINOS_SENDER_EMAIL = "dominos@dominospizza.pl"
SUBJECT_PROMO_CODE = "Witaj w newsletterze Domino's!"
SUBJECT_ACTIVATION = "Potwierdzenie subskrypcji newslettera Domino's"

def setup_logger():

    if not os.path.exists('logs'):
        os.makedirs('logs')

    logger = logging.getLogger('dominos_automator')
    logger.setLevel(logging.DEBUG)

    file_log_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    console_log_format = logging.Formatter('%(message)s')

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(console_log_format)

    file_handler = logging.FileHandler('logs/automator.log', encoding='utf-8')
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(file_log_format)

    if not logger.handlers:
        logger.addHandler(console_handler)
        logger.addHandler(file_handler)

    return logger


logger = setup_logger()