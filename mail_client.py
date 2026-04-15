import mailslurp_client
import os
from dotenv import load_dotenv
from mailslurp_client.rest import ApiException

load_dotenv(override=True)

class MailSlurpService:

    def __init__(self):
        api_key = os.environ.get('MAILSLURP_API_KEY')
        if not api_key:
            raise ValueError("mailslurp api key is empty")

        self.configuration = mailslurp_client.Configuration()
        self.configuration.api_key['x-api-key'] = api_key

        self.inbox_id = None
        self.api_client = mailslurp_client.ApiClient(self.configuration)
        self.inbox_controller = mailslurp_client.InboxControllerApi(self.api_client)
        self.wait_controller = mailslurp_client.WaitForControllerApi(self.api_client)

    def verify_api_key(self):
            try:
                user_controller = mailslurp_client.UserControllerApi(self.api_client)
                user_controller.get_user_info()
            except ApiException:
                raise ValueError("mailslurp api key is wrong")

    def create_mailbox(self):
        options = mailslurp_client.CreateInboxDto()
        options.use_short_address = True
        try:
            inbox = self.inbox_controller.create_inbox_with_options(options)
            self.inbox_id = inbox.id
            return inbox.email_address
        except ApiException as e:
            raise

    def delete_mailbox(self):
        try:
            self.inbox_controller.delete_inbox(self.inbox_id)
        except ApiException as e:
            raise

    def get_latest_email(self):
        while True:
            try:
                latest_email = self.wait_controller.wait_for_latest_email(
                    inbox_id=self.inbox_id,
                    timeout=30000,
                    unread_only=True
                )

                return latest_email
            except ApiException as e:
                if e.status == 408:
                    continue
                else:
                    raise

