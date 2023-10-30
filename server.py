'''
Task for hospital:
1. Recieve data from all peers
2. Compute the sum of the data recieved
3. Print the sum
'''

import socket, ssl
import sys

from fl import sum_numbers, recieve_data

context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile="cert.pem")

bindsocket = socket.socket()
bindsocket.bind(('localhost', 10023))
bindsocket.listen(5)

numbers = []

while True:
    newsocket, fromaddr = bindsocket.accept()
    connstream = context.wrap_socket(newsocket, server_side=True)
    numbers = recieve_data(connstream, numbers)

    if len(numbers) == 3:
        sum = sum_numbers(numbers)
        print(sum)
        sys.exit(0)
