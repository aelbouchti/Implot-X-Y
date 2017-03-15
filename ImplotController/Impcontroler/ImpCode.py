
"""
General Functions
Calling Intern Cursor Class
Generating Paths and Executing Data

"""



from Impcontroler import Point
from Impcontroler import Motor
from time import *
from math import *

M1pins=[]
M2pins=[]
S1P,S2P=0,0
Xmax,Ymax=0,0


def StartX():
    CURSOR=CURSOR()
    CURSOR.setPins(M1pins,M2pins)
    CURSOR.sensorPins(S1P,S2P)
    CURSOR.HomeCursor()



def Data(CODE):
    CURSOR.GetCodeData(CODE)

    
def WriteData():
    CURSOR.GeneratePaths()
    CURSOR.ExecuteData()
    
if __name__=="__main__":
    StartX()
    WriteData()
