from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer
from math import *

class MyMotor():
    def __init__(self, port):
        self.motor = Motor(port)

    def rotate_to(self, angle, direction=0, speed=30):
        angle = (angle + 360) % 360 

        if direction == 1:
            dd = 'clockwise'
        elif direction == -1:
            dd = 'counterclockwise'
        elif direction == 0:
            dd = 'shortest path'
        else:
            assert False
        self.motor.run_to_position(angle, dd, speed)
        self.motor.run_to_position(angle, speed=speed)

    def rotate(self, speed):
        self.motor.start(speed)

class Timer():
    def wait_for_seconds(self, secs):
        wait_for_seconds(secs)
