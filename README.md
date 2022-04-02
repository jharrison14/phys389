==============================CORE-FILE====================================
Fluid.py - Python class which defines properties of a fluid in a
one-dimensional pipe as well its methods to determine position and time 
intervals

======================FUNCTIONS USED IN UPDATING===========================

Grid.py - Determines arrays of positions and times used in updating speed

InitialConditions.py - Stores initial conditions for speed profiles 
dependent on postiion

FiniteDifference.py - Stores function for evolving speed through time using
the finite difference method

========================UPDATE AND DISPLAY FILES===========================

InviscidUpdate - Updates the speed profile through all time values and 
exports specific times in a NumPy file

InviscidPlot - Plots the exported profiles for the specific times through
MatPlotLib

==============================TEST FILES===================================

test_Fluid - Test methods in Fluid slass
test_Grid - Tests function in Grid
test_Derivates - Tests function in Derivatives
test_InitialConditions - Tests functions in InitialConditions
test_FiniteDifferency - Tests functions in FiniteDifference

============================PACKAGES USED==================================

NumPy
MatPlotLib (PyPlot)
Copy
OS

