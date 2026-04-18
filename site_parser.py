from bs4 import BeautifulSoup
from exceptions import SiteParsingError

def extract_verification_token(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    token_input = soup.find('input', {'name': '__RequestVerificationToken'})
    
    if token_input and 'value' in token_input.attrs:
        return token_input['value']
    raise SiteParsingError("failed extracting verification token")
