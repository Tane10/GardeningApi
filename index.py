import requests
import twilio
from flask import Flask, request

app = Flask(__name__)


# Setting up the route response
@app.route("/")
def welcome():
    return "Welcome to here"


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)