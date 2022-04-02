import numpy as np


def gridCreate(dx,dt):
    """
    Represents all possible positions and times for a defined fluid

    Parameters:
        dx (tuple with dtype: float): Tuple returned from positionInfo method of the Fluid class
        dt (tuple with dtype: float): Tuple returned from timeInfo method of the Fluid class

    Returns
        positions, times (tuple with dtype: array with dtype: float): Tuple containing arrays for all positions and all times for
        which the speed is measured.
    """
    positions = np.arange(0,dx[0]+dx[1],dx[1]) #array of positions from zero to the pipe length with a calculated position increment
    times = np.arange(0,dt[0]+dt[1],dt[1]) # array of times from zero to the maximum time with a calculated time increment

    return positions, times

