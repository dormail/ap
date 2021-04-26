# probe.py

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.optimize import curve_fit
from uncertainties import ufloat
from uncertainties.umath import *

# messspule
F = 86.6e-6 # m^2
U_Sp = 900

# probe 1 Dy2O3
# Spannungen in milivolt
print('Dy2O3')
U_Br_0 = 12.5
R_3_0 = 998 + 633 * 0.005

L = 0.073
M = 0.0151
dense = 7.24e3 
Q = M / (L * dense)
print(F)
print(Q)

U_Br = np.array([60, 66, 66])
U_Br = ufloat(U_Br.mean(), U_Br.std())
R_3 = 998 + np.array([309, 302, 310]) * 0.005
print(R_3)
print(R_3 - R_3_0)
R_3 = ufloat(R_3.mean(), R_3.std())

dR = R_3_0 - R_3
print(f'𝛥R = {dR}')
susz1 = 4 * F * U_Br / Q / U_Sp
susz2 = 2 * dR/R_3_0 * F / Q
print(f'U_Br = {U_Br}')
print(f'Spannungsmethode 𝜒 = {susz1}')
print(f'Widerstandsmethode 𝜒 = {susz2}')


# probe 3 Gd2O3
L = 0.076
M = 0.01408
dense = 7.4e3 
Q = M / (L * dense)
