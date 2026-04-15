from bs4 import BeautifulSoup
from mailslurp_client import Email
import re
from exceptions import EmailParsingError
from config import PROMO_CODE_PATTERN

def activation_link_extractor(mail: Email):
    bs = BeautifulSoup(mail.body, 'html.parser')
    link_element = bs.find('a', class_='link2')
    if not link_element:
        raise EmailParsingError("did not find activation link inside the mail")
    return link_element.get('href')


def promo_code_extractor(mail : Email):
    bs = BeautifulSoup(mail.body, 'html.parser')
    pattern = PROMO_CODE_PATTERN
    all_p = bs.find_all('p')
    for p in all_p:
        text = p.get_text(strip=True)
        if re.match(pattern, text):
            return text
    raise EmailParsingError("did not find promo code inside the mail")

