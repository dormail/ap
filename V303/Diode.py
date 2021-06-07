# Diode.py
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.optimize import curve_fit

d, U = np.genfromtxt('daten/Diode.txt', unpack=True)

# curve fit
def f(d, a, b):
    return a / d**1 + b

popt, pcov = curve_fit(f, d, U)
a, b = popt[:]
error = np.diag(np.sqrt(np.abs(pcov)))
print(f'a = {a} \pm {error[0]}')
print(f'b = {b} \pm {error[1]}')

plt.scatter(d,U,
        marker='+',
        label='Messdaten')
x = np.linspace(np.min(d)-1, 36)
plt.plot(x, f(x, a, b),
        color='k',
        label='Curve Fit')

plt.legend()
plt.xlabel('Distanz / cm')
plt.ylabel(r'$U$ / V')
plt.tight_layout()

plt.savefig('build/diode.pdf')

