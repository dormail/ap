# std.py

import numpy as np
from uncertainties import ufloat

data = [5.015, 6.005]
data = np.array(data)

mean = np.mean(data)
std = np.std(data)

E = ufloat(mean, std)
print(f'U = {E}')

h = 4.135e-15 # planck constant for eV
c = 3e8
l = h*c / E
print(f'l = {l}')

