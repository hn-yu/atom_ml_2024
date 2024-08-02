from ase.io import read, write

atom = read("CONTCAR")
atoms = atom.repeat([5, 5, 1])
write("model.xyz", atoms)