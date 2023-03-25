from twilio.rest import Client

# Your Twilio account SID and authentication token
account_sid = 'AC0ebc1b09b72e2669b7612ab0b9baf297'
auth_token = 'your_auth_token_here'

# Create a Twilio client object
client = Client(account_sid, auth_token)

# Send a WhatsApp message to multiple recipients
recipients = ['whatsapp:+1234567890', 'whatsapp:+9876543210']
for recipient in recipients:
    message = client.messages.create(
        body='Hello from Python!',
        from_='whatsapp:+14155238886',  # This is your Twilio WhatsApp number
        to=recipient
    )

    print(f'Message sent to {recipient}. SID: {message.sid}')