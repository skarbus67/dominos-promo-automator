from mail_client import MailSlurpService
from mailslurp_client.rest import ApiException
import json
from config import logger
from email_parser import *
from exceptions import *

try:
    mss = MailSlurpService()
    logger.info("authorizing api key...")
    mss.verify_api_key()
    logger.info("succesfuly authorized api key")

    logger.info("creating a new mailbox...")
    mailbox = mss.create_mailbox()
    logger.info("succesfully created new mailbox")
    logger.info(f"mail : {mailbox}")

    logger.info("waiting for email with link activation...")
    mail = mss.get_latest_email()
    logger.debug(f"sender : {mail.sender.email_address}")
    logger.debug(f"subject : {mail.subject}")
    logger.debug(f"body : {mail.body}")
    logger.info(f"activation link : {activation_link_extractor(mail)}")
    logger.info("succesfully recieved email")

    logger.info("waiting for email with promo code...")
    mail = mss.get_latest_email()
    logger.debug(f"sender : {mail.sender.email_address}")
    logger.debug(f"subject : {mail.subject}")
    logger.debug(f"body : {mail.body}")
    logger.info(f"promo code : {promo_code_extractor(mail)}")
    logger.info("succesfully recieved email")

except ApiException as e:
    logger.error(f"api error : {json.loads(e.body)['message']}")
except ConfigurationError as e:
    logger.error(f"configuration error : {e}")
except EmailParsingError as e:
    logger.error(f"email parsing error : {e}")
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
        