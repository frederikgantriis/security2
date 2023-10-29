# Generate CA key
openssl genrsa -out ca.key 2048

# Generate CA certificate
openssl req -x509 -new -nodes -key ca.key -sha256 -days 1825 -out ca.pem -subj "/C=DK/ST=Copenhagen/L=None/O=None/OU=None/CN=localhost/emailAddress=none"

# Generate server key
openssl genrsa -out server.key 2048

# Generate server certificate
openssl req -new -key server.key -out server.csr -subj "/C=DK/ST=Copenhagen/L=None/O=None/OU=None/CN=localhost/emailAddress=none"

# Sign server certificate with CA
openssl x509 -req -in server.csr -CA ca.pem -CAkey ca.key -CAcreateserial -out server.pem -days 1825 -sha256 -subj "/C=DK/ST=Copenhagen/L=None/O=None/OU=None/CN=localhost/emailAddress=none"

# Generate client key
openssl genrsa -out client.key 2048

# Generate client certificate
openssl req -new -key client.key -out client.csr -subj "/C=DK/ST=Copenhagen/L=None/O=None/OU=None/CN=localhost/emailAddress=none"

# Sign client certificate with CA
openssl x509 -req -in client.csr -CA ca.pem -CAkey ca.key -CAcreateserial -out client.pem -days 1825 -sha256 -subj "/C=DK/ST=Copenhagen/L=None/O=None/OU=None/CN=localhost/emailAddress=none"
