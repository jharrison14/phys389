import pytest
import numpy as np
import Grid as g
import Fluid as f
import numpy as np
import Grid as g 
def test_gridCreate():
    np.testing.assert_array_equal(g.gridCreate(f.Fluid(),10),(np.arange(0,10.1,0.1,dtype = float),np.arange(0,10.1,0.1,dtype = float)))
