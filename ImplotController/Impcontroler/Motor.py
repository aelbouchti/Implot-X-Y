
# Imperial Creativity
# ImplotControler 1.0



import sys
from time import *
from math import *
from time import *
try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO . Try sudo commands")

from Implotcontroler import Point


class Motor(object):
    
    DELAY = 0.02
    def __init__(self, pins, delay=DELAY):
        self.PINS = pins
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.PINS, GPIO.OUT)
        self.DELAY = delay
        self.stat = []
        self.LL = [
            (1, 1, 0, 0),
            (1, 0, 1, 0),
            (0, 1, 1, 0),
            (0, 1, 0, 1),
            (0, 0, 1, 1),
            (1, 0, 0, 1)]
        self.zero = [0,0,0,0]
        self.steps = 0
        self.movestep(self.LL[0])
        self.release()

    def infopls(self):
        return 'Motor at ', self.PINS, self.steps, self.actual_state

    def abord(self, type, value, tb):
        GPIO.cleanup(self.PINS)

    def movesteps(self, value):
        steps = value - self._steps
        self.move(steps)

    def move(self, steps):
        
        if steps == 0:
            return '-0-'
        
        rotation = steps//abs(steps)
        for i in range(0, steps, rotation):
            index = (self.steps + rotation)%len(self.LL)
            self.movestep(self.LL[index])
            sleep(self.DELAY)
            self.steps= rotation

    def release(self):
        self.movestep(self.zero)
        self.stat = self.zero

    def reset(self):
        self.steps = 0

    def _set_step(self, state):
        #HIGH OR LOW
        self.stat = state
        GPIO.output(self.PINS, state)


        
class COMMANDER(Motor,Path):
    
    def __init__(self,name):
        super(COMMANDER, self).__init__()
        self.name=name
        self.HOME=False
        self.SENSORPIN=0
        self.POS=0
        
        
    def setPins(self,pins):
        self.Motor.pins=pins
    
    def SSP(self,s):
        self.SENSORPIN=s
        
    def setHOME(self):
        #
        #
        self.HOME=True
    
    def MoveToPos(self,pos):
        
        
    

class CURSOR(Object):
    
    def __init__(self):
        self.XCommand=COMMANDER('X')
        self.YCommand=COMMANDER('Y')
        self.Position=Point(0,0)
        self.PullPin=15
        self.Home=False
        self.HomeKnown=False
        self.PathExec=Path()
        self.GRID=[]
        self.GRIDinfo=[0,0,0,0]
        
    def setPins(self,p1,p2):
        self.XCommand.setPins(p1)
        self.YCommand.setPins(p2)
    
    def SensorPins(self,s1,s2):
        self.XCommand.SSP(s1)
        self.YCommand.SSP(s2)
        
    def setGRID(self,xmax=100,ymax=100,stepx=1,stepy=1):
    
	    P=Point(0,0)
	    tableL=[]
	    finaltable=[]
	    for i in range(0,Xmax+stepx,stepx):
		    for j in range(0,Ymax+stepy,stepy):
			    P=P.setXY(i,j)
			    tableL+=[P]
		    finaltable+=[tableL]
		    tableL=0
	    #return table and number of points on X and Y axe
	    self.GRID,self.GRIDinfo=finaltable,[xmax,ymax,stepx,stepy]
        
    def CheckHome(self):
        return self.Home
    
    def HomeCursor(self):
        self.XCommand.setHOME()
        self.YCommand.setHOME()
        self.Position=Point(0,0)
        self.Home=True
    
    def GetPathData(self,DATA):
        self.PathExec.decodeDATA(DATA)
        
    def ExecuteData(self):
        self.MoveCursorTo(self.PathExec.pathpoints[0])
        OL=self.PathExec.operativelines
        PP=self.PathExec.pathpoints
        
        for i in self.PathExec.L:
            if OL[i]==T:
                self.Click()
                self.MoveCursorTo(PP[i])
            else:
                self.Click(False)
                self.MoveCursorTo(PP[i])
                
            
        
    def MoveCursorTo(self,point):
        if self.HomeKnown=False:
            self.HomeCursor()
        
        self.Home=False
        
    def Click(self,operation=True):
        if operation==True:
            #
        else:
            #
    
    
