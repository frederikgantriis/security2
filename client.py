import ssl, socket

context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
context.load_verify_locations('server.crt')

conn = context.wrap_socket(socket.socket(socket.AF_INET), server_hostname='localhost')

conn.connect(('localhost', 10023))

cert = conn.getpeercert()

print(cert)

while True:
    msg = input("Enter something: ")
    conn.sendall(bytes(msg, 'utf-8'))

