
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
	def __init__(self,a,b):
        	self.X=a
        	self.Y=b
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
		
class Path(Line):
	def __init__(self,a,b):
		a=Line.__init__(0,0)


		
Len=lambda A,B : sqrt( (A.X-B.X)**2 + (A.Y-B.Y)**2)
def GeometriqueDistance(A,B):
	return Len(A,B)


def generate_points_table(Xmax,Ymax,step):
	P=Point(0,0)
	tableL=[]
	finaltable=[]
	
	for i in range(0,Xmax+step,step):
		for j in range(0,Ymax+step,step):
			P.setXY(i,j)
			tableL+=[P]
		finaltable+=[tableL]
		tableL=0
	#return table and number of points on X and Y axe
	return finaltable,len(finaltable[0],len(finaltable))


def bresenham_line(start, end):
    	# Setup initial conditions
	x1, y1 = start.returnXY()
	x2, y2 = end.returnXY()
	dx = x2 - x1
	dy = y2 - y1
    	# Determine how steep the line is
	
    	is_steep = abs(dy) > abs(dx)
	
    	# Rotate line
    	if is_steep:
        	x1, y1 = y1, x1
        	x2, y2 = y2, x2
		
	# Swap start and end points if necessary and store swap state
        swapped = False
    	if x1 > x2:
        	x1, x2 = x2, x1
        	y1, y2 = y2, y1
        	swapped = True

    	# Recalculate differentials
    	dx = x2 - x1
    	dy = y2 - y1
	
    	# Calculate error
    	error = int(dx / 2.0)
    	ystep = 1 if y1 < y2 else -1
	
    	# Iterate over bounding box generating points between start and end
    	y = y1
    	points = []
	cord=Point(0,0)
    	for x in range(x1, x2 + 1):
        	coord = (y, x) if is_steep else (x, y)
		cord.X=coord[0]
		cord.Y=coord[1]
        	points.append(cord)
        	error -= abs(dy)
        	if error < 0:
            		y += ystep
            		error += dx
    	# Reverse the list if the coordinates were swapped
    	if swapped:
        	points.reverse()
    		return points


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
    
