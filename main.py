from mail_client import MailSlurpService
from mailslurp_client.rest import ApiException
import json
from config import logger

try:
    mss = MailSlurpService()
    logger.info("authorizing api key...")
    mss.verify_api_key()
    logger.info("succesfuly authorized api key")
    logger.info("creating a new mailbox...")
    mail = mss.create_mailbox()
    logger.info("succesfully created new mailbox")
    logger.info(f"mail : {mail}")
    logger.info("waiting for email...")
    sender, subject, body = mss.get_latest_email()
    logger.debug(f"sednder : {sender}")
    logger.debug(f"subject : {subject}")
    logger.debug(f"body : {body}")
    logger.info("succesfully recieved email")
except ApiException as e:
    logger.error(f"api error : {json.loads(e.body)['message']}")
except ValueError as e:
    logger.error(f"configuration error : {e}")
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

    

