#!/bin/python3

import socket
# from xmlrpc import client

# clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# #Host = "172.21.127.246"

# host = socket.gethostbyname()

# port = 444

# clientsocket.connect("172.21.127.246", port)

# message =clientsocket.recv(1024)

# clientsocket.close()

# print(message.decode('ascii'))

target_host = "www.google.com"
host = socket.gethostname()
target_port = 80

#create a socket object
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#connect to the client
clientsocket.connect((target_host, target_port))

#send some data to the client
clientsocket.send("GET / HTTP/1.1\r\nHost: target_host\r\n\r\n")

#receive some data 
response = clientsocket.recv(4096)
print(response)

