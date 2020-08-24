from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/")
def hello():
    return "<center><h1>Lets Chat! Have a Nice Day :)</h1></center>"

@app.route("/sms", methods=['POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Fetch the message
    msg = request.form.get('Body')

    # Create reply
    resp = MessagingResponse()
    if msg=='hi':
    
        resp.message("Hello")
    elif msg=='good morning':
        resp.message("Very Good Morning")
    elif msg=='how are you':
        resp.message("Well, good and what about You?")
    else:
        resp.message("You said: {}".format(msg))

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)