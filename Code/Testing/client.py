import socket

HOST ="192.168.68.69"
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((HOST, PORT))

    while True:
        command = input("Enter command (FORWARD, BACKWARD, LEFT, RIGHT) or 'exit' to quit: ")
        client.sendall(command.encode())

        if command.lower() == 'exit':
            print("Exiting client.")
            break

        response = client.recv(1024).decode()
        print(f"Server response: {response}")