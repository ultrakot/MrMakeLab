#create twilio whatsapp bot
from flask import Flask, request
from twilio.rest import Client


# Twilio API credentials
account_sid = 'ACac1bc4eb9aaff0c68314c7ff9b58b1ec'
auth_token = '2318d56175e01c0e9498f25302a832e5'

# Initialize the Twilio client
client = Client(account_sid, auth_token)

# Send a WhatsApp message
from_whatsapp_number = 'whatsapp:+14155238886'
to_whatsapp_number = 'whatsapp:+972558982149'
message = client.messages.create(
    body="thats another message from the bot",
    from_=from_whatsapp_number,
    to=to_whatsapp_number
)

# Print the message SID
print(message.sid)