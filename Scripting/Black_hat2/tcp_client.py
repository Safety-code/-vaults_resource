import socket


target_host = "www.google.com"
target_port = 80

# create socket object
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#connect the client
tcp_socket.connect((target_host, target_port))

#Send some data to the server
tcp_socket.send(b"GET HTTP/1.1\r\nHost: google.com\r\n\r\n")

#response object to receive some data 
response = tcp_socket.recv(4096)

print(response.decode())
tcp_socket.close()