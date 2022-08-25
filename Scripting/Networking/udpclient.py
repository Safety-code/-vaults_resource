#!/bin/python3

from http import client
import socket

target_host= "127.0.0.1"
target_port=80

#create a socket object
udpsock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#send some data to the socket
client.sendto("What is your SSL certificate", (target_host, target_port))

#receive some data from the socket
data, addr = client.recvfrom(4096)

print(data)
