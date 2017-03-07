
# Imperial Creativity
# ImplotControler 1.0


# Point class and functions

from math import *
from time import *

# Constants

# Extremum
Xmax,Ymax=100,100

#Point Class : Classic mathematical modelisation of a point in 2D space 

class Point(object):
	#Initial X,Y
        X,Y=0,0
	#Creating a Point class dosent need arguments . Every Point get X=0 Y=0 at the creation
	def __init__(self):
        	self.X=0
        	self.Y=0
	#Setting values
    	def setXY(self,x,y):
        	self.X=x
        	self.Y=y
    	def AVX(self,value):
        	self.X+=value
	def tupl(self,a):
        	self.X=P[0]
        	self.Y=P[1]
    	def AVY(self,value):
        	self.Y+=value
    	def clonePoint(self,Point):
        	self.X=Point.X
        	self.Y=Point.Y
	#Returning Values
    	def returnXY(self):
        	return self.X,self.Y
    	def X(self):
        	return self.X
    	def Y(self):
        	return self.Y
        
#The abstract modelisation of an infinit number of points between 2 non-same points
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

	
Len=lambda A,B : sqrt( (A.X-B.X)**2 + (A.Y-B.Y)**2)
def GeometriqueDistance(A,B):
	return Len(A,B)

def generate_points_table(Xmax,Ymax,step):
	P=Point()
	tableL=[]
	finaltable=[]
	for i in range(0,Xmax+step,step):
		for j in range(0,Ymax+step,step):
			P.setXY(i,j)
			tableL+=[P]
		finaltable+=[tableL]
		tableL=0
	return finaltable


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
    
