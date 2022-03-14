import InviscidUpdate as iv 
import numpy as np 
import pandas as pd 
import Grid as g
import Fluid as f 
import InitialConditions as ic

tophatFluid = f.Fluid("Top-Hat",0,10,10)

positions = g.positionInfo(tophatFluid,100)
times = g.timeInfo(tophatFluid,1000)
grid = g.gridCreate(positions,times)


d = {}
df = pd.DataFrame(data=d)
currentSpeeds = iv.initialSpeeds(ic.two_top_hat,grid).tolist()
for i in grid[1]:
    if i == 0:
        toUpdate = {"%s"%(i):currentSpeeds}
        d.update(toUpdate)
    else:
        print("Nope")

print(df)
