import pytest
import InitialConditions as ic
import numpy as np

def test_positive_line():
    assert ic.positive_line(2) == 8

def test_negative_line():
    assert ic.negative_line(1) == 2
    assert ic.negative_line(3) == 0

def test_gaussian():
    assert ic.gaussian(2) == 1

def test_sine():
    np.isclose(ic.sine(0.5), 0)
    np.isclose((2.5),0)
    
