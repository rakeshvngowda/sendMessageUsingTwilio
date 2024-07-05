from twilio.rest import Client
import os
from twilio.base.exceptions import TwilioRestException

class TwilioCOnfig:
    account_sid = os.getenv("ACCOUNT_SID")
    auth_token = os.getenv("AUTH_TOKEN")
    fromNumber = os.getenv("FROM_NUMBER")
    toNumber = os.getenv("TO_NUMBER")


class SendMessageFromTwilio(TwilioCOnfig):
    def __init__(self):
        # super().__init__()
        self.client = Client(self.account_sid, self.auth_token)

    def send_message(self ,message):
        try:
            response = self.client.messages.create(
                from_=self.fromNumber, to=self.toNumber, body=message
            )
            print(f"Messaga SID: {response.sid}")
            return {"status": "message sent successfully", "messageid": response.sid}
        except TwilioRestException as e:
            return {"error": "failed to sent Messaga", "errorMessage": f"Error: {e}"}