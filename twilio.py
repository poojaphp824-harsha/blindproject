# Find these values at https://twilio.com/user/account
account_sid = "AC86aa5aef0db58b9e31b4b98f9c46c476"
auth_token = "cb8dacaa0fd8746eb6142bf4bc03e17f"

client = Client(account_sid, auth_token)

client.api.account.messages.create(
    to="+91-9483959670",
    from_="+1(256) 782-9493 ",
    body="Hello there!")

