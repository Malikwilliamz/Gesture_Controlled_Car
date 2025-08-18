import socket
import sys, tty, termios, time
import keyboard
from sshkeyboard import listen_keyboard

sys.path.append('/home/malik/Documents/Gesture_Controlled_Car/Gesture_Controlled_Car/Code/Utils')
sys.path.append('/home/malik/Documents/Gesture_Controlled_Car/Gesture_Controlled_Car/Config')

from network import HOST_IP
from hardware_config import move_forward, move_backward, move_forward_when_pressed, move_backward_when_pressed,stop_all

def press(key):
    if key == 'w':
        move_forward_when_pressed()
        print("Moving Forward")
    
    elif key == 's':
        move_backward_when_pressed()
        print("Moving Backward")
        
def release(key):
    stop_all()
        


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
                    move_backward()

                elif data == "LEFT":
                    print("Turning left")

                elif data == "RIGHT":
                    print("Turning right")

                else:
                    stop_all()
                    print("Unknown command")

                conn.sendall(b'Command executed')




if __name__ == "__main__":
    connect_to_client(65432)
    listen_keyboard(
    on_press=press,
    on_release = release)
