import numpy as np 
import Grid as g 
import Derivatives as d
import InitialConditions as ic 


class Fluid:
    def __init__(
        self,
        velocity = np.array([1, 0, 0], dtype = float),
        name = 'Water',
        viscosity = 1.0,
        pipeLength = 10.0,
        maxTime = 0
    ):
        self.velocity = velocity.copy().astype(np.float)
        self.name = name
        self.viscosity = viscosity
        self.pipeLength = pipeLength
        self.maxTime = maxTime


    def __str__(self):
        return "Fluid: {0}, Viscosity: {1:.3e}, Velocity {2}, Time {3}, Pipe Length {4}".format(
        self.name, self.viscosity, self.velocity, self.maxTime, self.pipeLength)

    def finiteDifference(self,grid,dt,ic):
        timeAdvancedValues = np.empty((0,np.size(grid)), dtype = float)
        
        positions = grid[0]
        times = grid[1]

        dx = positions[1]-positions[0]
        dt = times[1]-times[0]

        r = (-dt)/(2*dx)
        for i in positions:
            print(i)
            #function is being furtther developed



