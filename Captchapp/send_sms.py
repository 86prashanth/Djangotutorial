# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
def sendsms():
    account_sid = 'ACe60aadba044134bd01f181a0f1df11e8'
    auth_token ='7e792abdd487331ccfe969fea578af59'
    client = Client(account_sid, auth_token)

    message = client.messages .create(
                        body="Your successfully save the answer",
                        from_='+13254138795',
                        to='+918686686461'
                    )

    print("messages has been sent successfully")
