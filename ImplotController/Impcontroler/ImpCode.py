
"""
General Functions
Calling Intern Cursor Class
Generating Paths and Executing Data

"""


from Impcontroler import Point
from Impcontroler import Motor
#from time import sleep
#from math import sleep

M1pins = []
M2pins = []
Code='0.0.T.1.1.F'
TargetPoint=Point.Point()
S1P, S2P = 0, 0
Xmax, Ymax = 0, 0

def StartX():
    Motor = Motor.CURSOR()
    Motor.Motor.setPins(M1pins, M2pins)
    Motor.Motor.sensorPins(S1P, S2P)
    Motor.Motor.HomeCursor()

def Data(CODE=code):
    Motor.Motor.GetCodeData(CODE)

def WriteData():
    Motor.Motor.GeneratePaths()
    Motor.Motor.ExecuteData()

if __name__ == "__main__":
    StartX()
    Data(code)
    WriteData()
