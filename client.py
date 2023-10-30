import random
import ssl, socket
import sys
import threading
import time

from fl import Peer, recieve_data, sum_numbers

numbers = []
peers = [] 

port1 = 0
port2 = 0
port3 = 0
hospital_port = 10023

if sys.argv[1] == "Alice":
    port1 = Peer.Alice.value
    port2 = Peer.Bob.value
    port3 = Peer.Charlie.value
elif sys.argv[1] == "Bob":
    port1 = Peer.Bob.value
    port2 = Peer.Alice.value
    port3 = Peer.Charlie.value
else:
    port1 = Peer.Charlie.value
    port2 = Peer.Alice.value
    port3 = Peer.Bob.value

# Context for client
client_conn = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
client_conn.load_verify_locations('cert.pem')
client_conn.verify_mode = ssl.CERT_REQUIRED

# Context for server
server_conn = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
server_conn.load_cert_chain(certfile="cert.pem")

bindsocket = socket.socket()
bindsocket.bind(('localhost', port1))
bindsocket.listen(5)

def send_message(msg, port):
    print("Sending: ", msg, "in 10 seconds")
    time.sleep(10)
    
    conn = client_conn.wrap_socket(socket.socket(socket.AF_INET), server_hostname='localhost')
    conn.connect(('localhost', port))
    conn.send(msg.encode())
    conn.close()

def split_number_in_three_uneven(number):
    number1 = number - random.randint(1, number - 1)

    number = number - number1

    number2 = number - random.randint(1, number - 1)

    number3 = number - number2

    return number1, number2, number3

msg = input("Enter result from model:")

# Split number in three uneven parts
number1, number2, number3 = split_number_in_three_uneven(int(msg))

print("saving: ", number1)

# Send msg to the two other peers
threading.Thread(target=send_message, args=(str(number2), port2)).start()
threading.Thread(target=send_message, args=(str(number3), port3)).start()


while True:
    newsocket, fromaddr = bindsocket.accept()
    connstream = server_conn.wrap_socket(newsocket, server_side=True)
    numbers = recieve_data(connstream, numbers)

    if len(numbers) == 2:
        numbers.append(number1)
        sum = sum_numbers(numbers)
        send_message(str(sum), hospital_port)
        sys.exit(0)

'''
Task for each peer:

1. Send parts of number to two other peers
2. compute the sum of the parts recieved from other peers
3. Send the sum to the hospital
'''

