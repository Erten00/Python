from twilio.rest import Client

# Twilio profil SID i token za autentifikaciju
account_sid = 'AC2b3ba8384c1c7b54075e20b12e81fcf4'
auth_token = 'c6afcdd6f509e40b97a1de41861215d4'

# Twilio klijent objekat
client = Client(account_sid, auth_token)

# Send a WhatsApp message to multiple recipients
recipients = ['whatsapp:+381621594100', 'whatsapp:+381628908616']
for recipient in recipients:
    message = client.messages.create(
        body='!',
        from_='whatsapp:+14155238886',  # This is your Twilio WhatsApp number
        to=recipient
    )

    print(f'Message sent to {recipient}. SID: {message.sid}')
