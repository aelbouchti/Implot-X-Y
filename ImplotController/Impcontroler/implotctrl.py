


# Imperial Creativity
# ImplotControler 1.0
# M-A Hilaly


# ImplotControler is the 2D-implot main driver

#

from math import *
from time import *
from GPIO import *


# Constants


MotorX,MotorY
StepX,StepY
Xmax,Ymax=20,40

Grid
Data

# Classes

class Motor(object):
    Pin=[]
class Point(object):
    X,Y=0,0
class Path(object):
    PTH=[]
    


# Functions

def _init_():
    
def MoveX(Numberofsteps,sens):

def MoveY(Numberofsteps,sens):

def MoveStepX(sens):

def MoveStepY(sens):

def DrawPath():

def Bresenham(Form,Precision):
    
def MTP(Point):
    #Move to point


def GoHome():
    #go to initial point

def printAlpha(alphabet):
    #Print alphabet

def printText(text):

def estimtime():
    
def main():
    
