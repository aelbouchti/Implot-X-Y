


# Imperial Creativity
# ImplotControler 1.0
# M-A Hilaly


# ImplotControler is the 2D-implot main driver

#

from math import *
from time import *
#from GPIO import *


# Constants


#MotorX,MotorY
#StepX,StepY
Xmax,Ymax=20,40

#Grid
#Data

# Classes

class Point(object):
    X,Y=0,0
    
    def __init__(self):
        self.X=0
        self.Y=0
    
    def addX(self,value):
        self.X=self.X+value
    def addY(self,value):
        self.Y+=value


# Functions


    
def MoveX():
    print("x moving")

#def MoveY():

#def MoveStepX():

#def MoveStepY():

#def DrawPath():

#def Bresenham():
    
#def MTP():
    #Move to point


#def GoHome():
    #go to initial point

#def printAlpha():
    #Print alphabet

#def printText():

#def estimtime():
    
#def main():
    
