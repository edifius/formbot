import os
from twilio.rest import Client

account_sid = "AC8dd7c3947acb406b1dddd6a4bfeedc89"
auth_token = "2BF75A7799C79BCA152D423526132D14"

client = Client(account_sid, auth_token)

client.messages.create(
            to="+17708456280",
            from_="+17708456280",
            body="Congrats, Perla!"
    )
