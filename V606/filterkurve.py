# filterkurve.py

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

f, U = np.genfromtxt('Daten/filterkurve.txt', unpack=True)


# fitten eine Gaussglocke drüber
def gaus(x, m, s, n):
    return n * np.exp(-1 * (x - m)**2 / (2 * s**2))

popt, pcov = curve_fit(gaus, f, U, p0=[35, 5, 2])
m = popt[0]
s = popt[1]
n = popt[2]

print(f'Fitparameter:')
print(f'm = {m} \ns = {s} \nn = {n}')
print(f'gaus(m)/ sqrt(2) = {gaus(m, m, s, n) / np.sqrt(2)}')
print(f'gaus(m-5) = {gaus(m-5, m, s, n)}')

print(f'Güte Q = {35 / 10}')

x = np.linspace(20, 50, 200)
plt.scatter(f,U, color='k', marker='+',
        label='Messdaten')
plt.plot(x, gaus(x,m,s,n), color='r',
        label='Curve Fit')

plt.xlabel(r'$f$ / kHz')
plt.ylabel(r'$U$ / V')
plt.legend()

plt.savefig('build/filterkurve.pdf')

