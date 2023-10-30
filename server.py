import socket, ssl

context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile="cert.pem")

bindsocket = socket.socket()
bindsocket.bind(('localhost', 10023))
bindsocket.listen(5)

def deal_with_client(connstream):
    data = connstream.recv(1024)
    # empty data means the client is finished with us
    while data:
        if not do_something(connstream, data):
            # we'll assume do_something returns False
            # when we're finished with client
            break
        data = connstream.recv(1024)
    # finished with client

def do_something(connstream, data):
    # do somehing with the remote user!
    return False

while True:
    newsocket, fromaddr = bindsocket.accept()

    connstream = context.wrap_socket(newsocket, server_side=True)

    try:
        deal_with_client(connstream)
    finally:
        connstream.shutdown(socket.SHUT_RDWR)
        connstream.close()

