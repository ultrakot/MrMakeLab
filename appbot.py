#create twilio whatsapp bot
from flask import Flask, request
from twilio.rest import Client


# Twilio API credentials
account_sid = 'ACac1bc4eb9aaff0c68314c7ff9b58b1ec'
auth_token = 'd546c2d3debd3ed58812af093347f739'

# Initialize the Twilio client
client = Client(account_sid, auth_token)

# Send a WhatsApp message
from_whatsapp_number = 'whatsapp:+14155238886'
to_whatsapp_number = 'whatsapp:+972558982149'
message = client.messages.create(
    body="YAY",
    from_=from_whatsapp_number,
    to=to_whatsapp_number
)

# Print the message SID
print(message.sid)