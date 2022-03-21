import InviscidUpdate as iv 
import numpy as np 
import pandas as pd 
import Grid as g
import Fluid as f 
import InitialConditions as ic
from os import path 
import copy as c 


lineFluid = f.Fluid("Line",0,10,0.9)

positions = g.positionInfo(lineFluid,1000)
times = g.timeInfo(lineFluid,10000)
grid = g.gridCreate(positions,times)

currentSpeed = iv.initialSpeeds(ic.gaussian,grid)

Data = []

for index, i in enumerate(grid[1]):
    if index == 0:
        """
        entry = []
        for j in currentSpeed:
            entry.append(c.deepcopy(j))
            Data.append(entry)
        """
        print("Yes")
    elif 9000 <= index <= 10000 and index % 100 == 0:
        currentSpeed = iv.finiteDifference(grid,currentSpeed)
        entry = []
        for k in currentSpeed:
            entry.append(c.deepcopy(k))
            Data.append(entry)
        print("t=%s"%(i))
    else:
        currentSpeed = iv.finiteDifference(grid,currentSpeed)
    
np.save("InviscidData",Data,allow_pickle=True)
if path.exists("InviscidData.npy"):
    print("Done")

    

