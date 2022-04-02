import pytest
import Fluid as f
import Derivatives as d
import Grid as g
import numpy as np


testFluid = f.Fluid("Test",10,10,100,100)    
grid = g.gridCreate(testFluid.positionInfo(),testFluid.timeInfo())


def quadratic(x):
    return x**2

quadraticValues = np.empty((0,),dtype=float)
for i in grid[0]:
    quadraticValues = np.append(quadraticValues,np.array([quadratic(i)],dtype=float),0)

    
def test_Derivatives():
    quadraticDerivative = d.positionDerivative(quadraticValues,testFluid.positionInfo()[1])
    np.isclose(quadraticDerivative,np.arange(0.2,20.,0.2,dtype=float))

