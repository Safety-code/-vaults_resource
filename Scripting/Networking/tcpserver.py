#!/bin/python3
#TCP server
import socket
import threading
from xmlrpc import client
#from urllib import request

#IP address and port the server will listen
bind_ip = "127.0.0.1"
bind_port = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((bind_ip,bind_port))

#Server listening here
server.listen(5)

print ("[*] Listening on %s:%d {%} {(bind_ip, bind_port)}")
print("[*] Listening on %s:%d" % (bind_ip,bind_port))

#this is our client-handling thread
def handle_client(client_socket):

    #print out what the client sends
    request= client_socket.recv(1024)

    print("[*] Received: %s" % request)

    #send back a packet to
    client_socket.send("ACK!")

    client_socket.close()
while True:
    client, addr = server.accept()

    print("[*] Accepted connection from: %s:%d" % (addr[0],addr[1]))

    #spin up our client thread to handle incoming data
    client_handler = threading.Thread(target=handle_client,args=(client,))
    client_handler.start()