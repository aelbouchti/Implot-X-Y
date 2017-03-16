
"""
General Functions
Calling Intern Cursor Class
Generating Paths and Executing Data

"""



from Impcontroler import Point
from Impcontroler import Motor
from time import sleep
from math import sleep

M1pins=[]
M2pins=[]
S1P,S2P=0, 0
Xmax,Ymax=0, 0


def StartX():
    Point.CURSOR=CURSOR()
    Point.CURSOR.setPins(M1pins, M2pins)
    Point.CURSOR.sensorPins(S1P, S2P)
    Point.CURSOR.HomeCursor()



def Data(CODE):
    Point.CURSOR.GetCodeData(CODE)

    
def WriteData():
    Point.CURSOR.GeneratePaths()
    Point.CURSOR.ExecuteData()
    
if __name__=="__main__":
    StartX()
    WriteData()
