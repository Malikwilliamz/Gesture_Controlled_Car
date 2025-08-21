import socket
import sys
from keyboard import keyboard
import piplates.MOTORplate as MOTOR
sys.path.append('/home/malik/Documents/Gesture_Controlled_Car/Gesture_Controlled_Car/Config')

from hardware_config import move_forward, move_backward, turn_left, turn_right,stop_all




while True:
	if keyboard.is_pressed('w'):
		move_forward()
		print("Moving forward")
        
        elif keyboard.is_pressed('s'):
                move_backward()
                print("Moving backward")

        elif keyboard.is_pressed('a'):
                turn_left()
                print("Turning Left")


        elif keyboard.is_pressed('d'):
                turn_right()
                print("Turning Right")


	elif keyboard.is_pressed('q'):
		stop_all()
		print("Stopped")
	else:
		stop_all()
		
