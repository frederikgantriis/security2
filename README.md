# Generate CA
## Generate CA-key (ca.crt)
```
openssl genrsa -out ca.key 2048
```

## Generate CA-certificate (ca.crt)
```
openssl req -x509 -new -nodes -key ca.key -sha256 -days 1825 -out ca.crt
```

## Generate server-key (server.key)
```
openssl genrsa -out server.key 2048
```

## Generate server-certificate (server.crt)
```
openssl req -new -key server.key -out server.csr
```

## Generate server-certificate (server.crt)
```
openssl x509 -req -in server.csr -CA ca.crt -CAkey ca.key -CAcreateserial -out server.crt -days 1825 -sha256
```

## Generate client-key (client.key)
```
openssl genrsa -out client.key 2048
```

## Generate client-certificate (client.crt)
```
openssl req -new -key client.key -out client.csr
```

## Generate client-certificate (client.crt)
```
openssl x509 -req -in client.csr -CA ca.crt -CAkey ca.key -CAcreateserial -out client.crt -days 1825 -sha256
```

## Generate client-p12 (client.p12)
```
openssl pkcs12 -export -clcerts -in client.crt -inkey client.key -out client.p12
```

## Generate client-pem (client.pem)
```
openssl pkcs12 -in client.p12 -out client.pem -clcerts
```