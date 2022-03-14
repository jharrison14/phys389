import numpy as np 



class Fluid:
    def __init__(
        self,
        name = 'Water',
        viscosity = 1.0,
        pipeLength = 10.0,
        maxTime = 10.0
    ):
        self.name = name
        self.viscosity = viscosity
        self.pipeLength = pipeLength
        self.maxTime = maxTime


    def __str__(self):
        return "Fluid: {0}, Viscosity: {1:.3e}, Time {2}, Pipe Length {3}".format(
        self.name, self.viscosity, self.maxTime, self.pipeLength)

    


