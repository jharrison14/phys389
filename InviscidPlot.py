import UpdateNameTBD as u 
import numpy as np
from os import path
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


if path.exists("InviscidData.npy"):
    print("The file InviscidData.npy has been created.")
else:
    raise ValueError("The file InviscidData.npy cannot be found or is in the wrong directory")

#confirms that Data is loaded back in
print("testing reading it back in")
DataIn = np.load("InviscidData.npy", allow_pickle=True)

x = u.grid[0]

for index, i in enumerate(DataIn):
    plt.plot(x,i)

plt.xlabel('Time (s)')
plt.ylabel('Speed (m/s)')
plt.legend()
plt.show()