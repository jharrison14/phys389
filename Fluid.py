import numpy as np 

class Fluid:
    def __init__(
        self,
        velocity = np.array([1, 0, 0], dtype = float),
        time = 0,
        name = 'Water',
        viscosity = 1.0,
        pipeLength = 10.0
    ):
        self.velocity = velocity.copy().astype(np.float)
        self.time = time
        self.name = name
        self.viscosity = viscosity
        self.pipeLength = pipeLength


    def __str__(self):
        return "Fluid: {0}, Viscosity: {1:.3e}, Velocity {2}, Time {3}, Pipe Length {4}".format(
        self.name, self.viscosity, self.velocity, self.time, self.pipeLength)

    
    