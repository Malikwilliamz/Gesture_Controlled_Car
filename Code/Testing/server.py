import socket
import sys

sys.path.append('/home/malo/Documents/Gesture_Controlled_Car/Code/Utils')

from network import HOST_IP

def connect_to_client(PORT):
    HOST = HOST_IP
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind((HOST, PORT))
        server.listen()
        print(f"Server listening on {HOST}:{PORT}")

        conn, addr = server.accept()

        with conn:
            print(f"Connected by {addr}")

            while True:
                data = conn.recv(1024).decode()
                if not data:
                    break

                print(f"Received: {data}")

                if data == "FORWARD":
                    print("Moving forward")
                elif data == "BACKWARD":
                    print("Moving backward")
                elif data == "LEFT":
                    print("Turning left")
                elif data == "RIGHT":
                    print("Turning right")
                else:
                    print("Unknown command")

                conn.sendall(b'Command executed')




if __name__ == "__main__":
    connect_to_client(65432)