import os
from flask import Flask, request
from twilio.rest import Client
from dotenv import load_dotenv
from twilio.twiml.messaging_response import MessagingResponse

import piFunctions as rasp_func

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
    msg_lower = request.form.get('Body').lower()
    resp = MessagingResponse()

    if "water plant" in msg_lower:
        resp.message("will try to water your plants")
        resp.message(rasp_func.auto_water())

    elif "check status" in msg_lower:
        resp.message("Checking everything is ok")
        resp.message(rasp_func.check_status())

    elif "soil info" in msg_lower:
        resp.message(rasp_func.soil_tracker())

    elif "temp" in msg_lower or "temperature" in msg_lower:
        resp.message(rasp_func.temp_humidity_check())

    elif "pictures" in msg_lower or "plant pictures" in msg_lower:
        resp.message(rasp_func.picture_plants())

    elif "device shutdown pin" in msg_lower or "device reset pin" in msg_lower:

        if 'pin: ' in msg_lower:
            pin_index = msg_lower.find('pin: ')
            pin_start_idx = pin_index + 5
            pin_end_idx = pin_start_idx + 4
            pin = msg_lower[pin_start_idx:pin_end_idx]
            resp.message(rasp_func.shutdown(pin))

        elif 'pin ' in msg_lower:
            pin_index = msg_lower.find('pin ')
            pin_start_idx = pin_index + 4
            pin_end_idx = pin_start_idx + 4
            pin = msg_lower[pin_start_idx:pin_end_idx]
            resp.message(rasp_func.shutdown(pin))

    else:
        resp.message("do nothing then")

    return str(resp)


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
