"""
This module contains the hardware configuration for the gesture-controlled car.
"""
import time
import piplates.MOTORplate as MOTOR



def run_motor1():
    MOTOR.dcSTART(0, 1)
    time.sleep(5.0)
    MOTOR.dcSPEED(0, 1, 100.0)
    time.sleep(10.0)
    MOTOR.dcSTOP(0, 1)

    print("Motor 1 run complete.")

def move_forward():
    MOTOR.dcCONFIG(0, 1, 'ccw', 50.0, 0)
    MOTOR.dcCONFIG(0, 2, 'ccw', 50.0, 0)
    MOTOR.dcCONFIG(0, 3, 'cw', 50.0, 0)
    MOTOR.dcCONFIG(0, 4, 'cw', 50.0, 0)

    MOTOR.dcSTART(0, 1)
    MOTOR.dcSTART(0, 2)
    MOTOR.dcSTART(0, 3)
    MOTOR.dcSTART(0, 4)
    
def stop_all():
    MOTOR.dcSTOP(0, 1)
    MOTOR.dcSTOP(0, 2)
    MOTOR.dcSTOP(0, 3)
    MOTOR.dcSTOP(0, 4)

def move_backward():
    MOTOR.dcCONFIG(0, 1, 'cw', 50.0, 0)
    MOTOR.dcCONFIG(0, 2, 'cw', 50.0, 0)
    MOTOR.dcCONFIG(0, 3, 'ccw', 50.0, 0)
    MOTOR.dcCONFIG(0, 4, 'ccw', 50.0, 0)

    MOTOR.dcSTART(0, 1)
    MOTOR.dcSTART(0, 2)
    MOTOR.dcSTART(0, 3)
    MOTOR.dcSTART(0, 4)

def turn_left():
    MOTOR.dcCONFIG(0, 1, 'cw', 50.0, 0)
    MOTOR.dcCONFIG(0, 2, 'cw', 50.0, 0)
    MOTOR.dcCONFIG(0, 3, 'cw', 50.0, 0)
    MOTOR.dcCONFIG(0, 4, 'cw', 50.0, 0)

    MOTOR.dcSTART(0, 1)
    MOTOR.dcSTART(0, 2)
    MOTOR.dcSTART(0, 3)
    MOTOR.dcSTART(0, 4)

def turn_right():
    MOTOR.dcCONFIG(0, 1, 'ccw', 50.0, 0)
    MOTOR.dcCONFIG(0, 2, 'ccw', 50.0, 0)
    MOTOR.dcCONFIG(0, 3, 'ccw', 50.0, 0)
    MOTOR.dcCONFIG(0, 4, 'ccw', 50.0, 0)

    MOTOR.dcSTART(0, 1)
    MOTOR.dcSTART(0, 2)
    MOTOR.dcSTART(0, 3)
    MOTOR.dcSTART(0, 4)


