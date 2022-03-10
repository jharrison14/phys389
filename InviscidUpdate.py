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


def finiteDifference(grid,ic):
        
        timeAdvancedValues = np.empty((0,), dtype = float)

        positions = grid[0]
        times = grid[1] 
        
        dx = positions[1]-positions[0]
        dt = times[1]-times[0]
        
        derivatives = d.positionDerivative(ic,grid,dx)

        for index, i in enumerate(positions):
            if index == 0:
                timeAdvancedValues = np.append(timeAdvancedValues,np.array(0,dtype = float),0)
            elif index == -1:
                timeAdvancedValues = np.append(timeAdvancedValues,timeAdvancedValues[-1],0)
            else:
                toAppend = np.array(ic(i)-(ic(i)*dt*derivatives[index-1]),dtype=float)
                timeAdvancedValues = np.append(timeAdvancedValues,toAppend,0)
        
        return timeAdvancedValues
        

dx = g.positionInfo(f.Fluid(),100)
dt = g.timeInfo(f.Fluid(),100)
grid = g.gridCreate(dx,dt)

print(finiteDifference(grid,ic.line))


