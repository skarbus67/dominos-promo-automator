import requests
import os
from dotenv import load_dotenv
from config import BASE_URL, PROMO_PATH, DOMINOS_SITE_KEY, CAPTCHA_TYPE, CAPMONSTER_TASK_API, CAPMONSTER_RESULT_API
from exceptions import CaptchaApiError, ConfigurationError

load_dotenv(override=True)

def get_dominos_captcha():

    api_key = os.environ.get('CAPMONSTERCLOUD_API_KEY')

    if not api_key:
        raise ConfigurationError("api key for capmonster is missing from environment variables")
    
    task_request = {
        "clientKey": api_key,
        "task": {
            "type": CAPTCHA_TYPE,
            "websiteURL": BASE_URL+PROMO_PATH,
            "websiteKey": DOMINOS_SITE_KEY
        }
    }
    
    try:
        task_response = requests.post(CAPMONSTER_TASK_API, json=task_request).json()
    except requests.exceptions.RequestException as e:
        raise CaptchaApiError(f"network error when connecting to capmonster task api: {e}")
    except ValueError:
        raise CaptchaApiError("received invalid json from capmonster task api")
    

    task_id = task_response.get("taskId")

    if not task_id:
        raise CaptchaApiError("taskId was not returned by capmonster")

    result_request = {
        "clientKey":api_key,
        "taskId": task_id
    }

    while True:

        try:
            result_response = requests.post(CAPMONSTER_RESULT_API, json=result_request).json()
        except requests.exceptions.RequestException as e:
            raise CaptchaApiError(f"network error when getting captcha result: {e}")
        except ValueError:
            raise CaptchaApiError("received invalid json from capmonster result api")
        
        status = result_response.get("status")

        if status == "ready":
            grecaptcha_token = result_response.get("solution").get("gRecaptchaResponse")

            if not grecaptcha_token:
                raise CaptchaApiError("gRecaptchaResponse was not returned by capmonster")
            
            return grecaptcha_token
        
        elif status == "processing":
            pass

        else:
            raise CaptchaApiError("captcha solving failed")

