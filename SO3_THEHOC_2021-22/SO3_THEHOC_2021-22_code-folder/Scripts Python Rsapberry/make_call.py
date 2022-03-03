import os
from twilio.rest import Client

#account_sid = os.environ["TWILIO_AUTH_SID"]
#auth_token = os.environ["TWILIO_AUTH_TOKEN"]

account_sid = "AC82e00e74d0c1a758256c63a421f8451f"
auth_token = "1b413580a9e814781670e50063f9d799"

client = Client(account_sid, auth_token)

call = client.calls.create(
     #to=os.environ["MY_PHONE_NUMBER"],
     to="+34628191144",
     from_="+14752588159",
     url=   "http://static.fullstackpython.com/phone-calls-python.xml"
)

print(call.sid)
