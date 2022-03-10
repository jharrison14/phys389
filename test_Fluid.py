import Fluid as f 
import numpy as np 

def test_string():
    default = f.Fluid()
    assert default == "Fluid: {0}, Viscosity: {1:.3e}, Velocity {2}, Time {3}, Pipe Length {4}".format(
        "Water", 1.0, np.array([1,0,0],dtype = float), 0, 10.0)

print(f.Fluid())