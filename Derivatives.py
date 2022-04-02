import numpy as np

def positionDerivative(u,deltaX):
    """
    Calcualtes the derivative for a set of y values for a function at each x value for where that y value was derived

    Parameters:
        u (array with dtype: float): the y values calculated from a list of x values for a given function
        deltaX (float): the position interval calculated from the positionInfo method from the fluid class

    Returns:
        derivates (array with dtype: float): the derivatives at each x value specified in the u array except for the ones at the end 
    """
    derivatives = np.empty((0,),dtype = float) #defines empty list for which the derivatives will be appended to
    
    for index, i in enumerate(u): #iterates through every y value and assigns an index
        if (index + 1 < np.size(u) and index - 1 >= 0): #makes sure the function does not break when trying to call a value outside of the bound
            mid = u[index+1]-u[index-1] #numerator of centre space derivative approximation in finite difference method
            toAppend = np.array([mid/(2*deltaX)],dtype = float) # numerator devided by denominator of centre space derivative apprximation
            derivatives = np.append(derivatives, toAppend,0) #appends the calculated derivative to the empy list
    return derivatives # returns list of derivatives at same y positions as u except for the first and last one (set by boundary conditions)









