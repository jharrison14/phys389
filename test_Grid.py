import pytest
import numpy as np
import Grid as g
import Fluid as f
import numpy as np

def test_gridCreate():
    dx = g.positionInfo(f.Fluid(),100)
    dt = g.timeInfo(f.Fluid(),100)
    np.testing.assert_array_equal(g.gridCreate(dx,dt),(np.arange(0,10.1,0.1,dtype = float),np.arange(0,10.1,0.1,dtype = float)))
