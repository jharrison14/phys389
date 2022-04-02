import Fluid as f 
import pytest 

def test_positionInfo():
    default = f.Fluid()
    assert default.positionInfo() == (10.0, 0.01)

def test_timeInfo():
    default = f.Fluid()
    assert default.timeInfo() == (10.0, 10.0/30000)

