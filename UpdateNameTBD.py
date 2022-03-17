import InviscidUpdate as iv 
import numpy as np 
import pandas as pd 
import Grid as g
import Fluid as f 
import InitialConditions as ic

lineFluid = f.Fluid("Line",0,10,5)

positions = g.positionInfo(lineFluid,100)
times = g.timeInfo(lineFluid,10000)
grid = g.gridCreate(positions,times)

currentSpeed = iv.initialSpeeds(ic.line,grid)





for index, i in enumerate(grid[1]):
    if index == 0:
        print(currentSpeed)
    elif i % 1 == 0:
        currentSpeed = iv.finiteDifference(grid,currentSpeed)
        print("t=%s"%(i))
        print(currentSpeed)
    else:
        currentSpeed = iv.finiteDifference(grid,currentSpeed)
        


