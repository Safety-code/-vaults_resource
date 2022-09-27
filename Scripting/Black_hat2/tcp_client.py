import socket


target_host = "www.google.com"
target_port = 80

# create socket object
utp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#connect the client
utp_client.connect((target_host, target_port))

#Send some data to the server
utp_client.send(b"GET HTTP/1.1\r\nHost: google.com\r\n\r\n")

#receive some data 
response = utp_client.recv(4096)

print(response.decode())
utp_client.close()