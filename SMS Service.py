# -*- coding: utf-8 -*-


from twilio.rest import Client

account_sid = '<account sid>'  #your account sid 
auth_token = '<authorized token>' #your authorized token
client = Client(account_sid, auth_token)

message = client.messages \
    .create(
         body=" ALERT MESSAGE. Someone tired to access the database without permission.\
             Information has been send to your Email. Please Check your Email.",
         messaging_service_sid='<message service sid>',
         to='<phone number>'
     )
print('\n')
print(message.sid)
print("-------Message is send to the number-------")
print('\n')