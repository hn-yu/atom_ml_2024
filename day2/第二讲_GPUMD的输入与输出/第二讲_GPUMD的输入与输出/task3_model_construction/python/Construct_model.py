from pylab import *
from ase import Atoms
from ase.io import write


a = 3.88  
h = 0.46
b = a / 2
Si_uc = Atoms('Si2',
            positions=[[0, a*np.sqrt(3)/3, 10 + h/2], [a/2, a*np.sqrt(3)/6, 10 - h/2]],
            cell=[(a, 0, 0), (-a/2, a*np.sqrt(3)/2, 0), (0, 0, 20)],
            pbc=[True, True, False])

Si = Si_uc.repeat([10, 10, 1])
write("model_uc.xyz", Si_uc)
write("model.xyz", Si)