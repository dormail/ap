# Diode.py
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.optimize import curve_fit

d, U = np.genfromtxt('daten/Diode.txt', unpack=True)

# curve fit
def f(d, a, b):
    return a / d**1 + b
def g(d, a, b):
    return a / d**2 + b

popt, pcov = curve_fit(f, d, U)
a, b = popt[:]
error = np.diag(np.sqrt(np.abs(pcov)))
print('Ergebnisse 1/x fit')
print(f'a = {a} \pm {error[0]}')
print(f'b = {b} \pm {error[1]}')

# alternative curve_fit
popt_alt, pcov_alt = curve_fit(g, d, U)
a_alt, b_alt = popt_alt[:]
error = np.diag(np.sqrt(np.abs(pcov_alt)))
print('Ergebnisse 1/x^2 fit')
print(f'a = {a_alt} \pm {error[0]}')
print(f'b = {b_alt} \pm {error[1]}')


plt.scatter(d,U,
        marker='+',
        label='Messdaten')
x = np.linspace(np.min(d)-1, 36)
plt.plot(x, f(x, a, b),
        color='k',
        label='Curve Fit mit $1/x$ Form')
plt.plot(x, g(x, a_alt, b_alt),
        color='r',
        ls='--',
        label=r'Curve Fit mit $1/x^2$ Form')

plt.legend()
plt.xlabel('Distanz / cm')
plt.ylabel(r'$U$ / V')
plt.tight_layout()

plt.savefig('build/diode.pdf')

