"""
Task for each peer:

1. Send parts of number to two other peers
2. compute the sum of the parts recieved from other peers
3. Send the sum to the hospital
"""

import random
import ssl
import socket
import sys
import threading

from fl import Peer, recieve_data, sum_numbers, get_p

numbers = []
peers = []

p = get_p()

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
client_conn.load_verify_locations("cert.pem")
client_conn.verify_mode = ssl.CERT_REQUIRED

# Context for server
server_conn = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
server_conn.load_cert_chain(certfile="cert.pem")

bindsocket = socket.socket()
bindsocket.bind(("localhost", port1))
bindsocket.listen(5)


def send_message(msg, port):
    print("Sending: ", msg)

    # Check if the port is open
    while True:
        try:
            conn = client_conn.wrap_socket(
                socket.socket(socket.AF_INET), server_hostname="localhost"
            )
            conn.connect(("localhost", port))
            break
        except:
            continue

    conn.send(msg.encode())
    conn.close()


def split_number_in_three_uneven(number):

    number1 = random.randint(1, p)
    number2 = random.randint(1, p)
    number3 = (number - number1 - number2) % p

    return number1, number2, number3


msg = input("Enter result from model:")

# Split number in three uneven parts
number1, number2, number3 = split_number_in_three_uneven(int(msg))

print("saving: ", number3)

# Send msg to the two other peers
threading.Thread(target=send_message, args=(str(number1), port2)).start()
threading.Thread(target=send_message, args=(str(number2), port3)).start()

while True:
    newsocket, fromaddr = bindsocket.accept()
    connstream = server_conn.wrap_socket(newsocket, server_side=True)
    numbers = recieve_data(connstream, numbers)

    if len(numbers) == 2:
        numbers.append(number3)
        sum = sum_numbers(numbers) % p
        send_message(str(sum), hospital_port)
        sys.exit(0)
