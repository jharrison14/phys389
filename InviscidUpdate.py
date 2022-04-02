import FiniteDifference as fd 
import numpy as np  
import Grid as g
import Fluid as f 
import InitialConditions as ic
from os import path 
import copy as c 

#first part of the fluids investigated
"""
positiveLineFluid = f.Fluid("Positive Line",0,5,1)
positions = positiveLineFluid.positionInfo()
times = positiveLineFluid.timeInfo()

positiveLineFluid = f.Fluid("Positive Line",0,5,0.1)
positions = positiveLineFluid.positionInfo()
times = positiveLineFluid.timeInfo()
"""

negativeLineFluid = f.Fluid("Negative Line",0,5,0.5) #definition of the fluid for a particlar run
positions = negativeLineFluid.positionInfo() #determining pipe length and position increment
times = negativeLineFluid.timeInfo() #determining maximum time and time increment

#second part of the fluids investigated
"""
gaussianFluid = f.Fluid("Gaussian",0,5,0.82436063535)
positions = gaussianFluid.positionInfo()
times = gaussianFluid.timeInfo()

gaussianFluid = f.Fluid("Gaussian",0,5,0.82436063535)
positions = gaussianFluid.positionInfo()
times = gaussianFluid.timeInfo()

sineFluid = f.Fluid("Sinusoidal",0,5,1/np.pi)
positions = sineFluid.positionInfo()
times = guassianFluid.timeInfo()
"""
grid = g.gridCreate(positions,times) #creates all possible positions and times 


#first part of initial conditions ran
"""
currentSpeed = fd.initialSpeeds(ic.positive_line,grid) 
"""

currentSpeed = fd.initialSpeeds(ic.negative_line,grid) # defines u(x,0) based on a partiular initial condition

#second part of initial conditions ran
"""
currentSpeed = fd.initialSpeeds(ic.gaussian_line,grid)

currentSpeed = fd.initialSpeeds(ic.sine,grid)
"""

Data = [] #created dataset to be exported into a NumPy file

for index, i in enumerate(grid[1]): #iterates through list of time and assigns an index
    if index == 0: #adds entry for initial time with profile based on initial conditions
        entry = []#created list of speeds at time t=0 to be appended to data set to be exported
        for j in currentSpeed: #iterates through current speeds
            entry.append(c.deepcopy(j)) #creates a deep copy of the speed at a given position
            Data.append(entry) #appends deep copies to data output list
        print(currentSpeed)
    elif index % 6000 == 0: #also appends deep copies if the time index is 6000 (divides max time by five)
        currentSpeed = fd.finiteDifference(grid,currentSpeed) #applies finite difference method to evolve current speed in time
        #same process as in the conditional statement above except the time evolved state is put into the data output list
        entry = []
        for k in currentSpeed:
            entry.append(c.deepcopy(k))
            Data.append(entry)
        print("t=%s"%(i)) #prints the time value of the datasets, acts as way to check if it is update correctly as well as indicator of progress
    else:
        currentSpeed = fd.finiteDifference(positions[1],times[1],currentSpeed) #evolves current speed through time without appending to any data-set
    
np.save("InviscidData",Data,allow_pickle=True) #exports data-set
if path.exists("InviscidData.npy"):
    print("Done") #indicates when data-set has been exported



    

