import InviscidUpdate as u 
import numpy as np
from os import path
from matplotlib import pyplot as plt



if path.exists("InviscidData.npy"):
    print("The file InviscidData.npy has been created.") #indicates whether data-set has been successfuly imported
else:
    raise ValueError("The file InviscidData.npy cannot be found or is in the wrong directory")

#confirms that Data is loaded back in
print("testing reading it back in")
DataIn = np.load("InviscidData.npy", allow_pickle=True)

x = u.grid[0] #defines x values of plot

for index, i in enumerate(DataIn): #iterates through dataset
    plt.plot(x,i)#plots each curve in dataset


plt.xlabel('Position (m))') #defines label of x values
plt.ylabel('Speed (m/s)') #defines label for y values
plt.show() #displays plot

