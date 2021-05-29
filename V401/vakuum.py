# vakuum.py

import numpy as np
import matplotlib.pyplot as plt

data = [22, 28, 22, 30, 21, 22, 18, 32, 31, 33, 31, 49, 42, 52, 38]
data = [32, 31, 33, 31, 49, 42, 52, 38]
data = np.array(data)

b = 0.05
λ = 635 * 10**-9

from uncertainties import ufloat
from uncertainties.umath import *

z = ufloat(data.mean(), data.std())
n = z * λ / (2*b)
print(f'z = {z}')

print(f'Näherung')
print(f'∆n = {n}')
dn_lit = .00027316
print(f'relativer Felhger = {(n - dn_lit) / dn_lit}')

# hier eine exaktere Berechnung
T_0 = 273.15
dp = 600 * .00133322 # druck diff in torr
dp = dp * 10000 # torr -> pascal
p_0 = 1013.2 * 10 # pascal
p = p_0
T = T_0 + 20

n = 1 + ((z * λ * T * p_0)/(2 * b * T_0 * dp))

print('Etwas exakter')
print(f"Brechungsindex: {n}")
n_lit = 1.00027316
print(f'Relativer Fehler: {(n-n_lit)/n}')

