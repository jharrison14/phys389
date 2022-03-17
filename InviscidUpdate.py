import numpy as np
import Fluid as f 
import Derivatives as d 
import InitialConditions as ic 
import Grid as g 


def initialSpeeds(u,grid):
    positions = grid[0]
    speeds = np.empty((0,),dtype=float)

    for i in positions:
        speedsAppend = np.array([u(i)],dtype =float)
        speeds = np.append(speeds,speedsAppend,0)
    return speeds


def finiteDifference(grid,u):
        
        timeAdvancedValues = np.empty((0,), dtype = float)

        positions = grid[0]
        times = grid[1] 
        
        dx = positions[1]-positions[0]
        dt = times[1]-times[0]
        
        derivatives = d.positionDerivative(u,dx)

        
        for index, i in enumerate(u):
            if index == 0:
                timeAdvancedValues = np.append(timeAdvancedValues,np.array([i],dtype=float),0)
            elif index == np.size(u)-1:
                timeAdvancedValues = np.append(timeAdvancedValues,np.array([timeAdvancedValues[-1]],dtype=float),0)
            else:
                timeJump = i-(i*dt*derivatives[index-1])
                toAppend = np.array([timeJump],dtype=float)
                timeAdvancedValues = np.append(timeAdvancedValues,toAppend,0)  

        return timeAdvancedValues

"""
lineFluid = f.Fluid("Line",0,10,10)

positions = g.positionInfo(lineFluid,100)
times = g.timeInfo(lineFluid,1000)
grid = g.gridCreate(positions,times)

currentSpeed = initialSpeeds(ic.line,grid)

timeAdvancedOnce = finiteDifference(grid,)
"""



