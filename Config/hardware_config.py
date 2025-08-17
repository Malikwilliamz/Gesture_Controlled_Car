"""
This module contains the hardware configuration for the gesture-controlled car.
"""
import time
import piplates.MOTORplate as MOTOR

# Motor plate configuration
MOTOR.dcCONFIG(0, 1, 'cw', 50.0, 2.5)

def run_motor1():
    MOTOR.dcSTART(0, 1)
    time.sleep(5.0)
    MOTOR.dcSPEED(0, 1, 100.0)
    time.sleep(10.0)
    MOTOR.dcSTOP(0, 1)

    print("Motor 1 run complete.")