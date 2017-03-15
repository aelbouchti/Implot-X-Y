
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
        self.release()

    def infopls(self):
        return 'Motor at ', self.PINS, self.steps

    def abord(self, type, value, tb):
        GPIO.cleanup(self.PINS)

    def movesteps(self, value):
        steps = value - self.steps
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

    def movestep(self, state):
        #HIGH OR LOW
        self.stat = state
        GPIO.output(self.PINS, state)
		


        
class COMMANDER(Motor):
    
    def __init__(self,name):
        self.name=name
        self.HOME=False
        self.SENSORPIN=0
        self.POS=0
		self.STEP=0
        
        
    def setPins(self,pins):
        self.Motor.pins=pins
    
    def SSP(self,s):
        self.SENSORPIN=s
        
    def setHOME(self):
        #
        #
        self.HOME=True
    def definstep(self,step):
		self.Motor.movesteps(step)
		self.STEP=step
	
    def MoveOneStep(self,a): # -1 for backward
        self.Motor.movesteps(self.STEP*a)
		self.POS+=a
        
    

class CURSOR(Object):
    
    def __init__(self):
		
        self.XCommand=COMMANDER('X')
        self.YCommand=COMMANDER('Y')
        self.Position=Point(0,0)
        self.PullPin=15
        self.Home=False
        self.HomeKnown=False
        self.CodeExec=Code()
        self.Grid=[]
        self.GRIDinfo=[0,0,0,0]
        
    def setPins(self,p1,p2):
        self.XCommand.setPins(p1)
        self.YCommand.setPins(p2)
    
    def SensorPins(self,s1,s2):
        self.XCommand.SSP(s1)
        self.YCommand.SSP(s2)
        
    def CheckHome(self):
        return self.Home
    
    def HomeCursor(self):
        self.XCommand.setHOME()
        self.YCommand.setHOME()
        self.Position=Point(0,0)
        self.Home=True
	
    def GetCodeData(self,Code):
        self.CodeExec.decodeDATA(DATA)
    	
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
		self.PathExec.bresenhampath(self.Position,point)
		self.optimise()
		while self.Position!=point:
			for i in self.PathExec.pathpoints:
				m,n=derivateC(self.Position,i)
				if m==0 : 
					self.YCommand.MoveOneStep(n)
					self.Position.AVY(n)
				else:
					self.XCommand.MoveOneStep(m)
					self.Position.AVX(m)
				self.Grid.insert(self.Position)
				
        self.Home=False
        
    def Click(self,operation=True):
        if operation==True:
            #
        else:
            #
    
    
