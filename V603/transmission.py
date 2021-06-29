# transmission.py

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from uncertainties import unumpy, ufloat

tau = 90 * 10**-6 # 90 micro second Totzeit
T = 200

alpha, NAl = np.genfromtxt('daten/ComptonAl.txt', unpack=True, comments='#')
alpha, NOhne = np.genfromtxt('daten/ComptonOhne.txt', unpack=True, comments='#')

NAl = np.divide(NAl, (1 - tau * NAl))
NOhne = np.divide(NOhne, (1 - tau * NOhne))

NAl = T * NAl
NOhne = T * NOhne
trans_numpy = np.divide(NAl, NOhne)

NAl = unumpy.uarray(NAl, np.sqrt(NAl))
NOhne = unumpy.uarray(NOhne, np.sqrt(NOhne))

trans = NAl / NOhne

# curve fit
def f(x, a, b):
    return a*x + b

popt, pcov = curve_fit(f, alpha, trans_numpy)
a, b = popt
x = np.linspace(7, 10)
plt.plot(x, f(x, a, b),
        label='Ausgleichsgerade')


#plt.scatter(alpha, NAl,
#        marker='+',
#        label='Messdaten mit Al-Absorber')
#
#plt.scatter(alpha, NOhne,
#        marker='+',
#        label='Messdaten ohne Absorber')

print(trans.shape)
plt.scatter(alpha, unumpy.nominal_values(trans), marker='+',
        label='Transmissionskoeffizient')
plt.errorbar(alpha, unumpy.nominal_values(trans),
        yerr=unumpy.std_devs(trans),
        marker='+',
        linestyle='',
        label='Transmissionskoeffizient')

# visuals
plt.xlabel(r'$\alpha$')
plt.ylabel(r'$N / (\text{Imp} / \text{s})$')
#plt.yscale('log')
plt.legend()
plt.tight_layout()

plt.savefig('build/transmission.pdf')
print('Figure saved in build/transmission.pdf')

