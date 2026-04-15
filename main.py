import mail_client

from mail_client import MailSlurpService

from mailslurp_client.rest import ApiException
import json


try:
    mss = MailSlurpService()
    print("authorizing api key...")
    mss.verify_api_key()
    print("succesfuly authorized api key")
    print("creating a new mailbox...")
    #mail = mss.create_mailbox()
    print("succesfully created new mailbox")
    #print(f"mail : {mail}")
    print("waiting for email...")
    sender, subject, body = mss.get_latest_email()
    print(f"sednder : {sender}")
    print(f"subject : {subject}")
    print(f"body : {body}")
except ApiException as e:
    print(f"api error : {json.loads(e.body)['message']}")
except ValueError as e:
    print(f"configuration error : {e}")
except Exception as e:
    print(f"unrecognized error : {e}")

finally:
    print("deleting email...")
    if mss.inbox_id:
        try:
            mss.delete_mailbox()
        except ApiException as e:
            print(f"api error : {json.loads(e.body)['message']}")
        print("succesfully deleted")
    else:
        print("mailbox not found")

    

