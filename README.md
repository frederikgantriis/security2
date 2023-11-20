# How to Run the program

## 1. Generating certificates

run the `init.sh` script

note: if the command doesn't work, there is already a certificate I have generated

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

Recieved:  1411279
Recieved:  1788796
Recieved:  2800943
1000
```

example output from clients:
```bash
python3 client.py Bob

Enter result from model:400
saving:  889371
Sending:  862418
Sending:  248617
Recieved:  978222
Recieved:  933350
Sending:  2800943
```
```bash
python3 client.py Alice

Enter result from model:500
saving:  73321
Sending:  978222
Sending:  948963
Recieved:  862418
Recieved:  853057
Sending:  1788796
```
```bash
python3 client.py Charlie

Enter result from model:100
saving:  213699
Sending:  853057
Sending:  933350
Recieved:  248617
Recieved:  948963
Sending:  1411279
```
