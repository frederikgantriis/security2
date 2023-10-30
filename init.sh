# Generate a self-signed certificate
openssl req -new -x509 -days 365 -nodes -out cert.pem -keyout cert.pem -subj "/C=DK/ST=New York/L=Brooklyn/O=Example Brooklyn Company/CN=localhost"