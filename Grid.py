import numpy as np
import Fluid as f


def positionInfo(fluid,steps):
    x = fluid.pipeLength
    deltaX = x/steps
    return x, deltaX

def timeInfo(fluid, steps):
    t = fluid.maxTime
    deltaT = t/steps
    return t, deltaT
def gridCreate(dx,dt):
    
    positions = np.arange(0,dx[0]+dx[1],dx[1])
    times = np.arange(0,dt[0]+dt[1],dt[1])

    return positions, times

