# a.py
# Auswertung fuer Teil a)

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from uncertainties import ufloat

# data input
df = pd.read_csv('daten/zeitabhaengigkeit.csv',
        comment='#')

f = 348.8
L = ufloat(3.5, 0.01) * 10**-3 # gegebener Wert fuer die Induktivitaet

U = np.array(df['U'].values)
#U = U / 1000
t = np.linspace(13.6, 13.6 * U.shape[0], U.shape[0])
#t = t / 10**6

# curve fit
def e_fun(x, k, x0):
    return x0 * np.exp(-1 * k * x)

popt, pcov = curve_fit(e_fun, t, U, p0=[0.01,400])
k, x0 = popt[0], popt[1]
k_err, x0_err = np.sqrt(np.diag(pcov))
# fuer SI: k -> k * 10**6


x = np.linspace(t[0] - 5, t[-1] + 20)
plt.scatter(t, U,
        marker='+',
        label='Messdaten')
plt.plot(x, e_fun(x, k, x0),
        c='r',
        label='Curve Fit')

plt.legend()
#plt.yscale('log')
plt.xlabel(r'$t / \si{\micro \second}$')
plt.ylabel(r'$U / \si{\milli \volt}$')

plt.savefig('build/5a.pdf')

# Fehler rechnung in SI
k = ufloat(k, k_err)
x0 = ufloat(x0, x0_err)
print(f'x0 = {x0} +/- {x0_err}')
print(f'k = {k} +/- {k_err}')
k = k * 1e6
x0 = x0 * 1e6
print(f'SI: k = {k} +/- {k_err}')

T_ex = 1 / k
R = 2 * L / T_ex
print(f'T_ex = {T_ex}')
print(f'R = {R}')

