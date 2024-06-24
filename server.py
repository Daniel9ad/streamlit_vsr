import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = "AC0e5bd9b0050252fee5d586318426381d"
auth_token = "0d3beb4f7db6e5dcaf551f51497178bf"
client = Client(account_sid, auth_token)

token = client.tokens.create()

print(token.ice_servers)
