from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import logging

# Initialize Flask app
app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

# Webhook route
@app.route('/webhook', methods=['POST'])
def webhook():
    incoming_msg = request.values.get('Body', '')
    response = MessagingResponse()
    response.message(f"Received: {incoming_msg}")
    return str(response)

# Main entry point
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)