import ssl, socket

context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
context.load_verify_locations('cert.pem')
context.verify_mode = ssl.CERT_REQUIRED

conn = context.wrap_socket(socket.socket(socket.AF_INET), server_hostname='localhost')

conn.connect(('localhost', 10023))

cert = conn.getpeercert()

while True:
    msg = input("Enter something: ")

    # Send data with certificate
    conn.sendall(msg.encode())


