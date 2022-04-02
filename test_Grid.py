import pytest
import numpy as np
import Fluid as f
import Grid as g

def test_gridCreate():
    testFluid = f.Fluid("Test",10,10,100,100)
    
    dx = testFluid.positionInfo()
    dt = testFluid.timeInfo()

    np.testing.assert_array_equal(g.gridCreate(dx,dt),(np.arange(0,10.1,0.1,dtype = float),np.arange(0,10.1,0.1,dtype = float)))
