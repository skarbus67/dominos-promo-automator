import logging
import os

CAPMONSTER_TASK_API = "https://api.capmonster.cloud/createTask"
CAPMONSTER_RESULT_API = "https://api.capmonster.cloud/getTaskResult"

DOMINOS_SITE_CONFIG = "b69800d2-7fc0-4d4e-a7bc-2e419ed7d4f2"
DOMINOS_SITE_KEY = "6Ley0gcaAAAAABVSBf1QCyxDzW9SpZqcRAJ8jkin"
CAPTCHA_TYPE = "RecaptchaV2TaskProxyless"

BASE_URL = "https://www.dominospizza.pl"
PROMO_PATH = "/korzysci"
API_NEWSLETTER_PATH = "/iapi/newsletter/subscribe"

DOMINOS_SENDER_EMAIL = "dominos@dominospizza.pl"
SUBJECT_PROMO_CODE = "Witaj w newsletterze Domino's!"
SUBJECT_ACTIVATION = "Potwierdzenie subskrypcji newslettera Domino's"

PROMO_CODE_PATTERN = r'^[A-Z0-9]{8}$'

ACCEPT_COOKIES_BUTTON_ID = "onetrust-accept-btn-handler"
EMAIL_INPUT_ID = "Email"
CONSENTS_CHECKBOX_ID = "Consents-2"
RECIEVE_PROMO_BUTTON_NAME = "Odbierz rabat"

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