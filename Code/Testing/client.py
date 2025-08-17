import socket
import sys

sys.path.append('/home/malo/Documents/Gesture_Controlled_Car/Code/Utils')
from network import HOST_IP, SERVER_IP

def connect_to_server(HOST, PORT):
    
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


if __name__ == "__main__":
    connect_to_server(HOST_IP, 65432)
