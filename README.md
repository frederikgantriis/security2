# How to Run the program

## 1. Generating certificates

run the `init.sh` script

## 2. Run the server

run the following command:
    
```bash
python3 server.py
```
## 3. Run the client

for each client run the following command:

```bash
python3 client.py <client_name>
```

the client name must be Alice, Bob or Charlie

after starting a client, you will be asked to enter a number for the Federated Learning. Each client will wait to recieve input from the two other clients, before starting the Federated Learning (summation of the three numbers). 

example output from server:
```bash
python3 server.py

Recieved:  -95
Recieved:  912
Recieved:  183
1000
```

example output from clients:
```bash
python3 client.py Alice

Enter result from model:100
saving:  78
Sending:  98
Sending:  -76
Recieved:  398
Recieved:  436
Sending:  912
```
```bash
python3 client.py Bob

Enter result from model:400
saving:  396
Sending:  398
Sending:  -394
Recieved:  98
Recieved:  -311
Sending:  183
```
```bash
python3 client.py Charlie

Enter result from model:500
saving:  375
Sending:  436
Sending:  -311
Recieved:  -76
Recieved:  -394
Sending:  -95
```
