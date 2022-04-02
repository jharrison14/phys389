import numpy as np

def positive_line(x):
    """
    Defines a line with slope 2 and intercept 4

    Parameters:
        x (float): independent variable of the line
    
    Returns:
        The y value for y=2*x+4
    """
    return 2*x + 4 #y value for y=2*x+4

def negative_line(x):
    """
    Defines a line with slope -2 and intercept 4 between zero and two

    Parameters:
        x (float): independent variable of the line

    Returns:
        the y value for y=-2*x+4
    """
    if x >= 2:
        return 0 # sets condition so it returns the line only for between 0 and 2
    else:
        return -2*x +4 #y value for y=-2*x=4



def gaussian(x):
    """
    Returns Gaussian function with mean 2 and standard deviation 1


    Parameters:
        x (float): independent variable of the curve
    
    Returns:
        the y value for y = np.exp(-2*(x-2)**2)
    """
    return np.exp(-2*(x-2)**2) #y value for y = np.exp(-2*(x-2)**2)

def sine(x):
    """
    Returns sin function of period 2 and amplitude 1 from 0 to 2


    Parameters:
        x (float): independent variable of the curve
    
    Returns:
        the y value for y = np.sin(np.pi * x)
    """
    if 0 <= x <= 2: #determines condition for which the function is only drawn between 0 and 2
        return np.sin(np.pi * x) #y value for y = np.sin(np.pi * x)
    else:
        return 0