import pytest
import Fluid as f
import Grid as g
import Derivatives as d
import FiniteDifference as fd
import numpy as np

   
grid = (np.array([1,2,3,4],dtype=float),np.array([1],dtype=float))

def quadratic(x):
    return x**2

u = quadratic


def test_InitialSpeeds():
   np.testing.assert_array_equal(fd.initialSpeeds(u,grid),np.array([1,4,9,16],dtype=float))

dx = 1
dt = 1

initialSpeed = [1,4,9,16]

def test_FiniteDifference():
    np.testing.assert_array_equal(fd.finiteDifference(dx,dt,initialSpeed),np.array([1,-12,-45,0],dtype=float))







    