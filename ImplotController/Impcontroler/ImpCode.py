
"""
General Functions
Calling Intern Cursor Class
Generating Paths and Executing Data

"""



#from Impcontroler import Point
from Impcontroler import Motor
#from time import sleep
#from math import sleep

M1pins=[]
M2pins=[]
S1P,S2P=0, 0
Xmax,Ymax=0, 0


def StartX():
    Motor.CURSOR=CURSOR()
    Motor.CURSOR.setPins(M1pins, M2pins)
    Motor.CURSOR.sensorPins(S1P, S2P)
    Motor.CURSOR.HomeCursor()



def Data(CODE):
    Motor.CURSOR.GetCodeData(CODE)

    
def WriteData():
    Motor.CURSOR.GeneratePaths()
    Motor.CURSOR.ExecuteData()
    
if __name__=="__main__":
    StartX()
    WriteData()
