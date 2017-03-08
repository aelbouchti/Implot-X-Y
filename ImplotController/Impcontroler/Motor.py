
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

    

GPIO.setmode(GPIO.BCM)

class Motor(Object):
    def __init__(self,Name,Nbr_steps,PINS):
            self.Name=Name
            self.Nbr_steps=Nbr_steps
            self.PINS=PINS
    
    def setPINS(self,PINS):
            self.PINS=PINS
    
    def StartMotor():
            for pin in PINS:
                    print "Setup pins"
                    GPIO.setup(pin,GPIO.OUT)
                    GPIO.output(pin, False)
    
    

