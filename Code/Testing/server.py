import socket
import sys

sys.path.append('/home/malik/Documents/Gesture_Controlled_Car/Gesture_Controlled_Car/Code/Utils')
sys.path.append('/home/malik/Documents/Gesture_Controlled_Car/Gesture_Controlled_Car/Config')

from network import HOST_IP
from hardware_config import move_forward,stop_all



def connect_to_client(PORT):
    HOST = ""
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

                if (data == "FORWARD"):
                    print("Moving forward")
                    move_forward()
 
                elif data == "BACKWARD":
                    print("Moving backward")

                elif data == "LEFT":
                    print("Turning left")

                elif data == "RIGHT":
                    print("Turning right")

                elif data == "Stop":
                    print("Stopping")
                    stop_all()

                elif (data == "Open") or (data == "Pointer") or (data == "OK"):
                    print("Nothing")



                else:
                    stop_all()
                    print("Unknown command")





if __name__ == "__main__":
    connect_to_client(65432)
    
