import os
from twilio.rest import Client


client = Client(account_sid, auth_token)

client.messages.create(
            to="+17708456280",
            from_="+17708456280",
            body="Congrats, Perla!"
    )
