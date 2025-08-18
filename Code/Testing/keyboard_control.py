import socket
import sys
from keyboard import keyboard
import piplates.MOTORplate as MOTOR

sys.path.append('/home/malik/Documents/Gesture_Controlled_Car/Gesture_Controlled_Car/Config')

from hardware_config import move_forward, move_backward, move_forward_when_pressed, move_backward_when_pressed,stop_all

"""
def press(key):
    if key == 'w':
        move_forward_when_pressed()
        print("Moving Forward")
    
    elif key == 's':
        move_backward_when_pressed()
        print("Moving Backward")
        
def release(key):
    stop_all()
    
listen_keyboard(
    on_press=press,
    on_release = release)
        
"""

"""def move_forward_when_pressed():
    # Motor plate configuration
    MOTOR.dcCONFIG(0, 1, 'ccw', 100.0, 0)
    MOTOR.dcCONFIG(0, 2, 'ccw', 100.0, 0)
    MOTOR.dcCONFIG(0, 3, 'cw', 100.0, 0)
    MOTOR.dcCONFIG(0, 4, 'cw', 100.0, 0)

    MOTOR.dcSTART(0, 1)
    MOTOR.dcSTART(0, 2)
    MOTOR.dcSTART(0, 3)
    MOTOR.dcSTART(0, 4)
    

def stop_all():
    MOTOR.dcSTOP(0, 1)
    MOTOR.dcSTOP(0, 2)
    MOTOR.dcSTOP(0, 3)
    MOTOR.dcSTOP(0, 4)"""

while True:
	if keyboard.is_pressed('w'):
		move_forward_when_pressed()
		print("Moving forward")
	elif keyboard.is_pressed('q'):
		stop_all()
		print("Stopped")
	else:
		stop_all()
		
