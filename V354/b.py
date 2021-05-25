# b.py
# Rechnung fuer 5b

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from uncertainties import ufloat
from uncertainties.umath import sqrt

# theorie wert
L = ufloat(3.5, 0.01) * 1e-3
C = ufloat(5, 0.02) * 1e-9

R_ap = sqrt(L/C) * 2
print(f'Theoriewert: R_ap = {R_ap}')

# messwert
n = 2.53
R_ap_ex = 2.53 * 5000 / 10
print(f'Messwert: R_ap = {R_ap_ex}')

# fehlerrechnung
err_rel = (R_ap - R_ap_ex) / R_ap
print(f'Relativer Fehler: {err_rel}')

