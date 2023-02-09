# we start with importing the twilio library to get the Client library
from twilio.rest import Client

# we put the sid (or account_id) the auth_token (as usal)
account_sid = 'AC55248ab4ccf061220ebf4b967514bd8c' 
auth_token = '*************************' 

client = Client(account_sid, auth_token) 
 
message = client.messages.create( 
                              from_='+17069199386', 
                              messaging_service_sid='MGc49185b85ddc4da9bc85941a36248170', 
                              body='ameny',      
                              to='+216 29581238' 
                          ) 
 
#print(message.sid)

