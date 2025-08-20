"""
This File tests motor functionalities based o.
"""

import sys 
import time

sys.path.append('/home/malik/Documents/Gesture_Controlled_Car/Gesture_Controlled_Car/Config')

from hardware_config import move_forward, move_backward, turn_left, stop_all

def test_all_motors():
    move_forward()
    time.sleep(5)
    move_backward()
    time.sleep(5)
    stop_all()

def test_left_turn():
    turn_left()
    stop_all()

def main():
    while True:    
       select_test = input("Select test to run (1: All Motors, 2: Turn Left 9: Exit): ")
       print(f"Selected test: {select_test}")
       if select_test == "1":
          test_all_motors()

       elif select_test == "2":
          test_left_turn()
       
       elif select_test == "9":
          break
       else:
          print("Invalid selection.")


if __name__ == "__main__":
    main()
