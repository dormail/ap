# luft.py

import numpy as np
import matplotlib.pyplot as plt

data = [2371, 2365, 2367, 2383, 2364, 2361, 2371, 2375]
data = np.array(data)

d = 0.005 # distanz die der Motor bewegt hat
d = d / 5.046 # ∆d für den Spiegel
print(f'd = {d}')

from uncertainties import ufloat
from uncertainties.umath import *

z = ufloat(data.mean(), data.std())
print(f'z = {z}')
λ = d * 2 / z
λ_real = 635 * 10**-9
print(f'λ = {λ}')
print(f'λ_real = {λ_real}')
print(f'Relativer Fehler: {(λ - λ_real) / λ_real}')

