
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
  Name=''
  Type=''
  Nbr_steps=0
  PINS=[]
  
  def __init__(self,Name,Type,Nbr_steps,PINS):
    self.Name=Name
    self.Type=Type
    self.Nbr_steps=Nbr_steps
    self.PINS=PINS
    
  def setPINS(self,PINS):
    self.PINS=PINS
    
  def StartMotor():
    for i in PINS:
      GPIO.setup(i,GPIO.IN)
    
    
  
          
