import Grid as g
import Fluid as f 
import numpy as np 
import Derivatives as d

def test_positionDerivatives():
    def quadratic(x):
        return x**2

    grid = g.gridCreate(f.Fluid(),10)
    deltaX = 0.1

    derivatives = d.positionDerivative(quadratic,grid,deltaX)
    np.isclose(derivatives,np.arange(0.2,20,0.2,dtype = float))

def test_timesDerivatives():
    def quadratic(t):
        return t**2

    grid = g.gridCreate(f.Fluid(),10)
    deltaT = 0.1

    derivatives = d.positionDerivative(quadratic,grid,deltaT)
    np.isclose(derivatives,np.arange(0.2,20,0.2,dtype = float))