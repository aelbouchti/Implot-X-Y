
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
	
	def __init__(self,start,end):
		""" Path class : Points Cursor should follow
			Using Point class and Bresenham / Andrew algorithms
		"""
		#pathpoints at the start : having the one and only points a in general(0,0)
		self.pathpoints=[a]
		self.start=Point()
		self.end=Point()
		self.Operation=False #Boolean decision weither to write or not
		#Lenth of pathpoints
		self.L=len(self.pathpoints) 
		self.code='' # The way we encode a bunch of points to simplify orders
		self.PATH=[] #Final table of the pathpoints
		
		#example pathpoints=[(0,5),(1,3),(5,6),(10,0)] 
		#pathdirections take the value of A in the simple equation AX+B=Y
		#pathdirections=['-1/2','-4/3','5/6'] as strings not fractions
		#PATH.0.0.F.0.-2.T.
		
	def setConfig(self,S,E,W):
		self.start=S
		self.end=E
		self.Operation=W

	def reLength(self):
		self.L= len(self.operationpoints)

	def ChangeOperation(self):
		self.Operation= not Self.Operation
		#Boolean manip
		
	def ACP(self,x,i):
		#addcheckpoint : insert Point value in index i
		#if i is out of index
		if i>self.L:
			i=self.L
		#if i i a list of points ( add automaticly att last index)
		if type(i)==list():
		     self.pathpoints+=i
		# Insert functions and case where i dosent satisfy anycondition
		if i<self.L : self.pathpoints.insert(i,x)
		else : self.pathpoints+=[x]
		
	def bresenhampath(self,start=self.start,end=self.end):
		""" Bresenham's Algorithm for Line
			Start and End are Point() classes
			Ouput: Modifying the pathpoints to bresenhams points
		"""
		x1,y1=start.X,start.Y
		x2,y2=end.X,end.Y
		#Calculating differentials dx,dy
		dx=x2-x1
		dy=y2-y1
		#defining if Line passing threw start and end is steep or not
		is_steep=abs(dy)>abs(dx)
		if is_steep:
			x1,y1=y1,x1
			x2,y2=y2,x2
		#swapping points if its necessary 
		swapped=False
		if x1>x2:
			x1,x2=x2,x1
			y1,y2=y2,y1
			swapped=True
		#recalculating dx,dy
		dx=x2-x1
		dy=y2-y1
		#Calculating Error
		error=int(dx/2.0)
		#ystep is -1 or +1
		ystep=1 if y1<y2 else -1
		y=y1
		points=[]
		for x in range(x1,x2+1):
			coord = Point(y, x) if is_steep else Point(x, y)
			points.append(coord)
			error-=abs(dy)
			if error<0:
				y+=ystep
				error+=dx
			if swapped:
				points.reverse()
		self.pathpoints=points
		self.L=len(points)
			
	def optimise(self):
		a,b,m,n=Point(),Point(),0,0
		k=self.pathpoints[0]
		ln=[self.pathpoints[0]]
		j=self.pathpoints[self.L-1]
		for i in range(0,self.L-1):
			a=self.pathpoints[i]
			b=self.pathpoints[i+1]
			if isnextto(a,b):
				ln+=[self.pathpoints[i+1]]
				continue
			else:
				possibleA,possibleB=Point(a.X,a.Y),Point(a.X,a.Y)
				m,n=wichsens(b,a)
				possibleA.AVX(m)
				possibleB.AVY(n)
				if disT(k,j,possibleA)>disT(k,j,possibleB):
					ln+[possibleB]
				ln+=[possibleA]
			ln+=[self.pathpoints[i+1]]
		self.path=ln

		def printpathpoints(self):
			for i in self.pathpoints:
				print(i.X,i.Y)
				
		def printoptimised(self):
			for in self.PATH:
				print(i.X,i.Y)
				
				
				

	def resetLists(self):
		self.pathpoints=[]
		#self.pathdirections=[]
		self.Operation=False
		self.PATH=[]
		
	def STARTX(self):
		self.bresenhampath()
		self.optimise()
		

			
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
		
class Code():
	def __init__(self):
		self.Code=''
		self.startx=Point()
		self.checkpoints=[]
		self.operativepaths[]

	def Code(self):
		code=''
		for i in range(0,self.L):
			a,b=self.checkpoints[i].returnXY()
			code+='.'+str(self.operativepaths[i])
		     	code+='.'+str(a)+'.'+str(b)
		self.Code=code
		
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

		self.checkpoints=pp
		self.operatiepaths=ol

	def setCode(self,Code):
		self.Code=Code

	def setLists(self,M,N):
		self.checkpoints=M
		self.operativepaths=N
				
			
		
	

	
def givefunction(A,B):
	dx=A.X-B.X
	dy=A.Y-B.Y
	return dy , -dx , dx*A.Y -dy*A.X

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

def isnextto(a,b):
	dx=abs(a.X-b.X)
	dy=abs(a.Y-b.Y)
	if dx+dy==1:
		return True
	return False


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


def Bresenhamline(start, end):
    """Bresenham's Line Algorithm
    Produces a list of tuples from start and end
    """
    # Setup initial conditions
    x1, y1 = start
    x2, y2 = end
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
    for x in range(x1, x2 + 1):
        coord = (y, x) if is_steep else (x, y)
        points.append(coord)
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
	
def angletodistance(angle,Dpignon):
	
def distancetoangle(distance,Dpignon):
	

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
    
