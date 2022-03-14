import numpy as np 



testArray = np.empty((0,))

for i in range (4,7):
    testArray = np.append(testArray,[i],0)

print(testArray)