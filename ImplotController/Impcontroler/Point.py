
# Imperial Creativity
# ImplotControler 1.0


# Point class and functions

from math import *
from time import *

# Constants

Xmax,Ymax=100,100


class P(object):
	dim=0
        X,Y=0,0
	def __init__(self):
        	self.X=0
        	self.Y=0
    	def setXY(self,x,y):
        	self.X=x
        	self.Y=y
    	def 2tuple(self,a):
        	self.X=P[0]
        	self.Y=P[1]
    	def AVX(self,value):
        	self.X+=value
    	def AVY(self,value):
        	self.Y+=value
    	def clonePoint(self,Point):
        	self.X=Point.X
        	self.Y=Point.Y
    	def returnXY(self):
        	return self.X,self.Y
    	def X(self):
        	return self.X
    	def Y(self):
        	return self.Y
        
class Line():
	A,B=P(),P()
	def __init__(self,a,b):
		self.A=a
		self.B=b
	def GeoLen(self):
		return sqrt( (self.A.X-self.B.X)**2 + (self.A.Y-self.B.Y)**2)
	def PixLen(self):
		return abs(self.A.X-self.B.X) + abs(self.A.Y-self.B.Y)
	def setA(self,a):
		self.A=a
	def setB(self,b):
		self.B=b


def MoveX():
    	print("x moving")
	
LEN=lambda A,B : sqrt( (A.X-B.X)**2 + (A.Y-B.Y)**2)
def GeometriqueDistance(A,B):
	return LEN(A,B)
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
    
