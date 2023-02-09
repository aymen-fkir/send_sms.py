from twilio.rest import Client
from random import randint



# generate the code
def code():
    c = ""
    for i in range(6):
        c+=str(randint(0,9))
    return int(c)
# verification function
def verify(num,n):
    if num == n:
        return True
    else:
        return False
# the sending function using Twilio api
def send(num):
    account_sid = 'account_sid' 
    auth_token = 'account_token' 

    client = Client(account_sid, auth_token) 
     
    message = client.messages.create( 
                                  from_='sender_number', 
                                  messaging_service_sid='the_serveur', 
                                  body= f'{num}',      
                                  to='the_number_you_want_to_send_to' 
                              )
num = code()
send(num)
n = int(input("enter the code : "))
while(verify(num,n)==False):
    n = int(input("enter your phone number: "))
print("welcome user")
