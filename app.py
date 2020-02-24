import os
from flask import Flask, request
from twilio.rest import Client
from dotenv import load_dotenv
from twilio.twiml.messaging_response import MessagingResponse

from functions import *

load_dotenv()

app = Flask(__name__)

# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')

# print(account_sid)
client = Client(account_sid, auth_token)


# Setting up the route response
@app.route("/")
def welcome():
    return "Welcome to here"


@app.route("/api", methods=['GET', 'POST'])
def replay():
    msg = request.form.get('Body')

    resp = MessagingResponse()

    if "water plant" in msg or "Water plant" in msg:
        water_plants()
        return str(resp)

    else:
        resp.message("do nothing then")

    return str(resp)


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
