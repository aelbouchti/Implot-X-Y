
# Imperial Creativity
# ImplotControler 1.0


# Point class and functions

from math import *
from time import *

# Constants



# Extremum
Xmax,Ymax=100,100


#Point Class : Classic mathematical modelisation of a point in 2D space dd
class Point(Object):
	#Initial X,Y
	def __init__(self,a=0,b=0):
		self.X=a
		self.Y=b
	#Setting values
	def setXY(self,a,b):
		self.X=a
		self.Y=b
	def setX(self,x):
		self.X=x
	def setY(self,y):
		self.Y=y
	def AVX(self,value):
		self.X+=value
	def AVY(self,value):
		self.Y+=value
	def returnXY(self):
		return self.X,self.Y
	def X(self): return self.X
	def Y(self): return self.Y
	
	
#The abstract modelisation of an infinit number of points between 2 non-same points
class Line():
	def __init__(self,a,b):
		self.A=Point(a.X,a.Y)	
		self.B=Point(b.X,b.Y)
	def GeoLen(self):
		return sqrt( (self.A.X-self.B.X)**2 + (self.A.Y-self.B.Y)**2)
	def PixLen(self):
		return abs(self.A.X-self.B.X) + abs(self.A.Y-self.B.Y)
	def setA(self,a):
		self.A=a
	def setB(self,b):
		self.B=b
		
		
class Path():
	
	def __init__(self,a=Point(0,0)):
		self.pathpoints=[a]
		self.operativelines['.PATH']
		self.L=len(pathpoints)
		self.code=''
		#pathpoints and pathdirections are 2 distinct sets with n and n - 1 elements
		#example pathpoints=[(0,5),(1,3),(5,6),(10,0)] 
		#pathdirections take the value of A in the simple equation AX+B=Y
		#pathdirections=['-1/2','-4/3','5/6'] as strings not fractions
		'PATH.0.0.F.0.-2.T.
		
	def ACP(self,x,i=self.L):
		#addcheckpoint : insert Point value in index i
		     
		if type(i)=='list'
		     self.pathpoints+=i
		if i!=self.L : self.pathpoints.insert(i,x)
		elif i==self.L : self.pathpoints+=[x]

	
	def bresenhampath(self,start,end):
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
    			self.pathpoints=points
			
	def optimise(self):
		A=0
		a,b,m,n=0,0,0,0
		k=self.pathpoints[0]
		j=self.pathpoints[L]
		possibleA,possibleB=Point(),Point()
		for i in L-1:
			a=self.pathpoints[i]
			b=self.pathpoints[i+1]
			if Len==1:
				continue
			else:
				m,n=wichsens(a,b)
				possibleA=a.AVX(m)
				possibleB=a.AVY(n)
				if disT(k,j,possibleA)>disT(k,j,possibleB):
					self.pathpoints.insert(i+1,possibleB)
				self.pathpoints.insert(i+1,possibleA)
				
				

	def resetLists(self):
		self.pathpoints=[]
		self.pathdirections=[]
		self.operativelines[]
		     
			
	
	def AOL(self,OLTab): #ADD OPERATIVE LINES
		self.operativelines=OLTab
		     

	def codeDATA(self):
		code=''
		for i in range(0,self.L):
			a,b=self.pathpoints[i].returnXY()
			code+='.'+str(self.operativelines[i])
		     	code+='.'+str(a)+'.'+str(b)
		self.code=code

			
	def decodeDATA(self,code=self.code):
		# 'PATH.0.0.T.2.0.F.0.0.T.0.2.F.0.0.T.0.-2.F.0.0.T.-2.0.F.0.0'
		pp=[]
		ol=[]
		a=Point()
		recode=code.split(".")
		counter=0
		for i in range(0,len(recode),3)
		     	a.setXY(recode[i],recode[i+1])
		     	pp+=[a]
		     	ol+=[recode[i+2]]

		self.pathpoints=pp
		self.operativelines=ol
		
	def config(self):
		self.optimise()
		self.L=len(pathpoints)
		
		
		
				
			
		
	

	
def givefunction(A,B):
	dx=A.x-B.x
	dy=A.y-B.y
	return dy , -dx , dx*A.y -dy*A.x

def disT(A,B,C):
	a,b,c=givefunction(A,B)
	return abs(C.x*a+C.y*b+c)//(sqrt(a*a+b*b))

def derivate(p,q):
	a=p.X-q.X
	b=p.Y-q.Y
	return a,b,a>0,b>0

def wichsens(p,q):
	a,b,c,d=derivate(p,q)
	if c==d:
		if a>0:
			return 1,1
		if a<0:
			return -1,-1
	else:
		if a>0:
			return 1,-1
		if a<0:
			return -1,1
		

def derivate2(p,q):
	return abs(p.X-q.X),abs(p.Y-q.Y)

def derivateC(q,p):
	return (p.X-q.X),(p.Y-q.Y)


# Euclide Algorithme for biggest commun divisor
def pgcd(a,b) :  
   	while a%b != 0 : 
      	a, b = b, a%b 
   	return b

def fractorise(a,b):
	if pgcd(a,b)==1:
		return a,b
	return factorise(a/pgcd(a,b),b/pgcd(a,b))
	
		
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


decision = lambda a : a>0
def decision(a) : return a>0
	
def decodedirections(code):
	a=code.split('/')
	return int(a[0]),int(a[1])
	
def angletodistance():
	
def distancetoangle():
	

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
    
