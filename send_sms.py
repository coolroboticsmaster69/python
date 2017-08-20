from twilio.rest import TwilioRestClient

account_sid = "ACe8299baa31f2afa4f5c917373fae9a57" # Your Account SID from www.twilio.com/console
auth_token  = "609b95182a0cd8b4efa8aecd5329764f"  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="i can see you,i knowwwwwwwwwwww you ",
    to="+918368822963",    # Replace with your phone number
    from_="+19787672510") # Replace with your Twilio number

print(message.sid)
