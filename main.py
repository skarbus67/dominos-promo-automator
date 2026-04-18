from mail_client import MailSlurpService
from mailslurp_client.rest import ApiException
import json
from config import *
from email_parser import *
from exceptions import *
from form_automator import *
import os
from dotenv import load_dotenv
from http_client import newsletter_activation, newsletter_signup


load_dotenv(override=True)
use_playwright = os.environ.get('USE_PLAYWRIGHT')


def wait_for_specific_email(mss, expected_sender, expected_subject):
    while True:
        mail = mss.get_latest_email()
        sender = mail.sender.email_address if mail.sender else "no sender"
        subject = mail.subject if mail.subject else "no subject"

        logger.debug(f"recieved a new mail (sender: {sender}, subject: {subject})")
        if expected_sender == sender and expected_subject == subject:
            return mail
            
def sumbit_form_untill_succesfull(dsa: DominosSiteAutomator):
    while(not dsa.is_submit_successful()):
        dsa.submit_form()
    
    
try:
    mss = MailSlurpService()
    logger.info("authorizing api key...")
    mss.verify_api_key()
    logger.info("succesfuly authorized api key")

    logger.info("creating a new mailbox...")
    mailbox = mss.create_mailbox()
    logger.info("succesfully created new mailbox")
    logger.info(f"mail : {mailbox}")

    if(use_playwright == "true"):
        dsa = DominosSiteAutomator()
        dsa.launch_dominos_site()
        dsa.accept_cookies()
        dsa.fill_email(mailbox)
        dsa.check_consents()
        sumbit_form_untill_succesfull(dsa)
        dsa.close_current_page()

    else:
        newsletter_signup(mailbox)

    logger.info("waiting for email with link activation...")
    mail = wait_for_specific_email(mss, DOMINOS_SENDER_EMAIL, SUBJECT_ACTIVATION)
    link = activation_link_extractor(mail)
    logger.info(f"activation link : {link}")
    logger.info("succesfully recieved email")

    if(use_playwright == "true"):
        dsa.launch_activation_site(link)
        dsa.close_current_page()
        dsa.stop_playwright()
    else:
        newsletter_activation(link)

    logger.info("waiting for email with promo code...")
    mail = wait_for_specific_email(mss, DOMINOS_SENDER_EMAIL, SUBJECT_PROMO_CODE)
    logger.info(f"promo code : {promo_code_extractor(mail)}")
    logger.info("succesfully recieved email")

except KeyboardInterrupt as e:
    logger.warning("interrupted with keyboard")
except ApiException as e:
    logger.error(f"api error : {json.loads(e.body)['message']}")
except ConfigurationError as e:
    logger.error(f"configuration error : {e}")
except EmailParsingError as e:
    logger.error(f"email parsing error : {e}")
except AutomationError as e:
    logger.error(f"form automation error : {e}")
except Exception as e:
    logger.critical(f"unrecognized error : {e}")

finally:
    logger.info("deleting email...")
    if mss.inbox_id:
        try:
            mss.delete_mailbox()
        except ApiException as e:
            logger.error(f"api error : {json.loads(e.body)['message']}")
        logger.info("succesfully deleted")
    else:
        logger.warning("mailbox not found")
