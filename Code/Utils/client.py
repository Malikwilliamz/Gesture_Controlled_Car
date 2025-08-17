import socket

HOST ="192.168.68.67"
PORT = 65432

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
client.connect((HOST, PORT))

client.send('Hello From Client'.encode())
print(client.recv(1024).decode())