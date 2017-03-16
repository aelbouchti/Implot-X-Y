
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
        #GPIO.setmode(GPIO.BCM)
        #GPIO.setup(self.PINS, GPIO.OUT)
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

    def movesteps(self, a):
        #steps = value - self.steps
        self.move(a)

    def move(self, steps):

        
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
        #GPIO.output(self.PINS, state)
		


        
class COMMANDER():
    
    def __init__(self,name,pins):
        self.Motor=Motor(pins)
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
        self.HOME=True
    def definstep(self,step):
        self.Motor.movesteps(step)
        self.STEP=step
    def MoveOneStep(self,a): # -1 for backward
        self.Motor.movesteps(self.STEP*a)
        self.POS+=a
        
    

class CURSOR():
    
    def __init__(self,pins1,pins2):
		
        self.XCommand=COMMANDER('X',pins1)
        self.YCommand=COMMANDER('Y',pins2)
        self.Position=Point(0,0)
        self.PullPin=15
        self.Home=False
        self.HomeKnown=False
        self.CodeExec=Code()
        self.Paths=[]
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
        self.HomeKnow=True
	
    def GetCodeData(self,DATA):
        self.CodeExec.decodeDATA(DATA)

    def GeneratePaths(self):
        self.Paths=[]
        for i in range(0,len(self.CodeExec.checkpoints)-1):
            P=Path()
            P.setConfig(self.CodeExec.checkpoints[i],self.CodeExec.checkpoints[i+1],self.CodeExec.operativepaths[i])
            self.Paths+=[P]
        
    	
    def ExecuteData(self):
        
        
        for i in self.Paths:
            if i.Operation:
                i.bresenhampath()
                i.optimise()
                print('optimised')
                #self.Click()
                for j in i.PAT:
                    print('moving to',j.X,j.Y)
                    self.MoveCursorTo(j)
                    
            else:
                self.Click(False)
                print('OneAxeTransition')
                self.MoveCursorTo(Point(i.start.X,i.end.Y))
                self.MoveCursorTo(Point(i.end.X,i.end.Y))
                    
                
                
            
        
    def MoveCursorTo(self,point):
        if equal(self.Position,point):
            self.Home=True
            print('equal')
        else:
            a,b,c,d=derivate(Point(self.Position.X,self.Position.Y),point)
            print("abcd",a,b,c,d)
            if a==0:
                while (self.Position.Y == point.Y )== False:
                    print('Y+1')
                    self.YCommand.MoveOneStep(d)
                    self.Position.AVY(d)
            if b==0:
                while (self.Position.X == point.X )== False:
                    print('X+1')
                    self.XCommand.MoveOneStep(c)
                    self.Position.AVX(c)
				
        self.Home=False

        
    def Click(self,operation=True):
        if operation==True:
            pass
        else:
            pass
    
    
