import os
from twilio.rest import Client
from Django import settings 

def send_sms_otp(phone_number, otp):
    client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
    message = client.messages.create(
                body=f'Your OTP is: {otp}',
                from_=settings.TWILIO_PHONE_NUMBER,
                to=phone_number
            )