import numpy as np
from Fluid import Fluid

def gridCreate(fluid,maxTime):
    t = fluid.time
    deltaT = (maxTime-t)/100
    times = np.arange(t,maxTime+deltaT,deltaT)

    x = fluid.pipeLength
    deltaX = x/100
    positions = np.arange(0,x+deltaX,deltaX)

    return "Times: %s, Positions: %s" %(times,positions) 


default = Fluid()

print(gridCreate(default,10))