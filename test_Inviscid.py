import pytest
import InviscidUpdate as iv 
import Derivatives as d 
import InitialConditions as ic 
import Grid as g 
import Fluid as f
"""
def test_iniitalSpeeds():
    np.isclose(iv.initialSpeeds(testu,g.gridCreate(g.positionInfo(f.Fluid(),100),g.timeInfo(f.Fluid(),100))),np.arange(4,24,0.2))
"""

testu = ic.line

dx = g.positionInfo(f.Fluid(),100)
dt = g.timeInfo(f.Fluid(),100)
grid = g.gridCreate(dx,dt)

print(iv.finiteDifference(grid,testu))