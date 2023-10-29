import ssl, socket

context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
context.verify_mode = ssl.CERT_REQUIRED
context.load_verify_locations('server.pem')
context.load_cert_chain(certfile="client.pem", keyfile="client.key")

conn = context.wrap_socket(socket.socket(socket.AF_INET), server_hostname='localhost')

conn.connect(('localhost', 10023))

cert = conn.getpeercert()

print(cert)

while True:
    msg = input("Enter something: ")

    # Send data with certificate
    conn.sendall(msg.encode())


