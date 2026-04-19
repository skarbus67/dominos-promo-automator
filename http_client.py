from curl_cffi import requests
from config import BASE_URL, PROMO_PATH, API_NEWSLETTER_PATH, DOMINOS_SITE_CONFIG
from site_parser import extract_verification_token
from captcha_client import get_dominos_captcha


def newsletter_signup(email):
    session = requests.Session(impersonate="chrome110")
    
    response_get = session.get(BASE_URL + PROMO_PATH)

    html_content = response_get.text
    
    extracted_token = extract_verification_token(html_content)

    captcha = get_dominos_captcha()
    
    payload = {
        "Captcha": captcha,
        "Config": DOMINOS_SITE_CONFIG,
        "Consents": ["2"],
        "Email": email,
        "FormType": "0",
        "g-recaptcha-response": captcha,
        "__RequestVerificationToken": extracted_token
    }

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Origin": BASE_URL,
        "Referer": BASE_URL + PROMO_PATH,
        "__requestverificationtoken": extracted_token
    }
    
    url = BASE_URL + API_NEWSLETTER_PATH

    session.post(url, json=payload, headers=headers)
    
def newsletter_activation(link):
    session = requests.Session(impersonate="chrome110")
    session.get(link)
