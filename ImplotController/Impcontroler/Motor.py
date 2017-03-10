
# Imperial Creativity
# ImplotControler 1.0


# Motors class
import sys
from math import *
from time import *
try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO . Try sudo commands")


import RPi.GPIO as GPIO
from Implotcontroler import Point
from time import *

class Motor(object):
    
    DELAY = 0.02
    def __init__(self, pins, delay=DELAY):
        self.PINS = pins
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.PINS, GPIO.OUT)
        self.DELAY = delay
        self.stat = []
        self.LL = [
            (1, 1, 0, 0),
            (1, 0, 1, 0),
            (0, 1, 1, 0),
            (0, 1, 0, 1),
            (0, 0, 1, 1),
            (1, 0, 0, 1)]
        self.zero = [0,0,0,0]
        self.steps = 0
        self.movestep(self.LL[0])
        self.release()

    def infopls(self):
        return 'Motor at ', self.PINS, self.steps, self.actual_state

    def abord(self, type, value, tb):
        GPIO.cleanup(self.PINS)

    def movesteps(self, value):
        steps = value - self._steps
        self.move(steps)

    def move(self, steps):
        
        if steps == 0:
            return '-0-'
        
        rotation = steps//abs(steps)
        for i in range(0, steps, rotation):
            index = (self.steps + rotation)%len(self.LL)
            self.movestep(self.LL[index])
            sleep(self.DELAY)
            self.steps= rotation

    def release(self):
        self.movestep(self.zero)
        self.stat = self.zero

    def reset(self):
        self.steps = 0

    def _set_step(self, state):
        #HIGH OR LOW
        self.stat = state
        GPIO.output(self.PINS, state)


        
class COMMANDER(Motor,Point):
    
    def __init__():
        super(COMMANDER, self).__init__()
    
