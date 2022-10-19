import socket

target_host = "127.0.0.1"
target_port = 9997

# create socket object
udp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# send some data
udp_client.sendto(b"AAABBBCC", (target_host, target_port))

#receive some data
data, addr = udp_client.recv(4096)

print(data.decode())
udp_client.close()