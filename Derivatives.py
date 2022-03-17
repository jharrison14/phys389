import numpy as np

def positionDerivative(u,deltaX):
    derivatives = np.empty((0,),dtype = float)
    
    for index, i in enumerate(u):
        if (index + 1 < np.size(u) and index - 1 >= 0):
            mid = u[index+1]-u[index-1]
            toAppend = np.array([mid/(2*deltaX)],dtype = float)
            derivatives = np.append(derivatives, toAppend,0)
    return derivatives









