import numpy as np 
import Derivatives as d

def initialSpeeds(u,grid):
    """
    Determines u(x,0) for every position value in the grid based on the initial condition

    Parameters:
        u (function): the initial condition
        grid (tuple with dtype: array with dtype: float): the arrays of position and time determined from the info from the fluid class
    Returns:
        the calcualted values of u(x,0) for each position on the grid
    """
    positions = grid[0] #calls array of positions from grid
    speeds = np.empty((0,),dtype=float) #creates empty list for which speeds will go into

    for i in positions: #iterates through every position value
        speedsAppend = np.array([u(i)],dtype =float) #finds speed at the iterated value
        speeds = np.append(speeds,speedsAppend,0) #appends speed to empty list
    return speeds #returns calculated values of u(x,0)


def finiteDifference(dx,dt,u):
    """
    Evolves a set of speeds by one time interval

    Parameters:
        dx (float): position interval calcualted from fluid class
        dt (float): time interval calculated from fluid class
    Returns:
        timeAdvancedValues (array with dtype: float): the speeds at the set positions after evolving from time 't' to 't+dt'  
    """    
    timeAdvancedValues = np.empty((0,), dtype = float) #creates empty set for time-evolved speeds

    derivatives = d.positionDerivative(u,dx) #determines list of position derivatives for given initial speeds


    for index, i in enumerate(u): #iterates through each speed and assigns an index
        if index == 0:
            timeAdvancedValues = np.append(timeAdvancedValues,np.array([i],dtype=float),0) #bounday condition for u(0,0)
        elif index == np.size(u)-1:
            timeAdvancedValues = np.append(timeAdvancedValues,np.array([0.],dtype=float),0) #boundary condition for u(L,0) where L is the pipe length
            #timeAdvancedValues = np.append(timeAdvancedValues,np.array([timeAdvancedVales[-1]],dtype-float)0) #this line is used for the positive linear inital condition
        else:
            timeJump = i-(i*dt*derivatives[index-1])# calculates finite difference function for the iterated speed
            toAppend = np.array([timeJump],dtype=float) #creates an array for the above calculation to be appended
            timeAdvancedValues = np.append(timeAdvancedValues,toAppend,0) #appends the time evolved speed into the empty array 

    return timeAdvancedValues #returns array of time evolved speeds






