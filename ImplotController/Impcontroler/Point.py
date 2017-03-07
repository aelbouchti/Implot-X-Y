


# Imperial Creativity
# ImplotControler 1.0
# M-A Hilaly


# Point class and functions



from math import *
from time import *



# Constants


#MotorX,MotorY
#StepX,StepY
Xmax,Ymax=20,40

#Grid
#Data


class P(object):
    dim=0
    
    def __init__(self,X,Y):
        self.X=X
        self.Y=Y
        
    def setXY(self,a,b):
        self.X=a
        self.Y=b
    
    def setX(self,value):
        self.X=self.X+value
        
    def setY(self,value):
        self.Y+=value
        
    def setPoint(self,Point):
        self.X=Point.X
        self.Y=Point.Y
        
    def returnXY(self):
        return self.X,self.Y
        

class Line():
    pass
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
    
