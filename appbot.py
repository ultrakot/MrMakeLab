#create twilio whatsapp bot
from flask import Flask, request
from twilio.rest import Client
import get_doc_text

# Twilio API credentials
account_sid = 'ACac1bc4eb9aaff0c68314c7ff9b58b1ec'
auth_token = 'c491dab0d93bb4678a07b611e29c75d0'

# Initialize the Twilio client
client = Client(account_sid, auth_token)

# Send a WhatsApp message
from_whatsapp_number = 'whatsapp:+14155238886'
to_whatsapp_number = 'whatsapp:+972558982149'
message = client.messages.create(
    body= get_doc_text.main(),
    from_=from_whatsapp_number,
    to=to_whatsapp_number
)

# Print the message SID
print(message.sid)