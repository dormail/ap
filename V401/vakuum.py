# vakuum.py

import numpy as np
import matplotlib.pyplot as plt

data = [22, 28, 22, 30, 21, 22, 18, 32, 31, 33, 31, 49, 42, 52, 38]
data = [32, 31, 33, 31, 49, 42, 52, 38]
data = np.array(data)

b = 0.05
p = (1 - 0.799932) * 10**5 # in pascal
p0 = 1013.2 * 10**5 # außendruck
λ = 635 * 10**-9

from uncertainties import ufloat
from uncertainties.umath import *

z = ufloat(data.mean(), data.std())
n = z * λ / (2*b)
print(f'z = {z}')
print(f'∆n = {n}')

