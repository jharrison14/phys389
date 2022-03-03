import Grid as g
import Fluid as f
import numpy as np

def positionDerivative(u,grid,deltaX):
    derivatives = np.empty((0,),dtype = float)
    x = grid[1]
    
    for index, i in enumerate(x):
        if (index + 1 < np.size(x) and index - 1 >= 0):
            mid = u(x[index+1])-u(x[index-1])
            toAppend = np.array([mid/(2*deltaX)],dtype = float)
            derivatives = np.append(derivatives, toAppend,0)
    return derivatives

def timeDerivative(u,grid,deltaT):
    derivatives = np.empty((0,),dtype = float)
    t = grid[0]
    
    for index, i in enumerate(t):
        if (index + 1 < np.size(t) and index - 1 >= 0):
            difference = u(t[index+1])-u(i)
            toAppend = np.array([difference/deltaT],dtype = float)
            derivatives = np.append(derivatives, toAppend,0)
    return derivatives


