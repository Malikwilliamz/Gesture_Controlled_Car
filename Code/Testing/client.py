import socket
import sys

sys.path.append('/home/malo/Documents/Gesture_Controlled_Car/Code/Utils')
sys.path.append('/home/malo/Documents/Gesture_Controlled_Car/Code/Client_Code/hand-gesture-recognition-mediapipe-main')

from network import HOST_IP, SERVER_IP
from app import command_to_server

def connect_to_server(HOST, PORT):
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect((HOST, PORT))
        while True:
            command = command_to_server
            client.sendall(command.encode())
            print(f"Sent command: {command}")
            if command.lower() == 'exit':
                print("Exiting client.")
                break

            response = client.recv(1024).decode()
            print(f"Server response: {response}")


if __name__ == "__main__":
    
    connect_to_server(SERVER_IP, 65432)
