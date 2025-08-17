import socket

HOST = ""
PORT = 65432

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

server.listen()

while True:
    client, addr = server.accept()
    print(client.recv(1024).decode())
    #client.send('Hello from server'.encode())
    client.send('a'.encode())


