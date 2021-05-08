# filterkurve.py

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.optimize import curve_fit
from uncertainties import ufloat
from uncertainties.umath import *

f, U = np.genfromtxt('Daten/filterkurve.txt', unpack=True)

data = {'f': f, 'U': U}
df = pd.DataFrame(data)
df = df.sort_values('f')
df.to_csv('build/filterkurve.tex', 
        sep='&', 
        header=False,
        index=False,
        line_terminator='\t\\\\\n')


# fitten eine Gaussglocke drüber
def gaus(x, m, a, n):
    return n * np.exp(-1 * a * (x - m)**2)

popt, pcov = curve_fit(gaus, f, U, p0=[35, 0.1, 2])
errors = np.sqrt(np.diag(pcov))
m = ufloat(popt[0], errors[0])
a = ufloat(popt[1], errors[1])
n = ufloat(popt[2], errors[2])
print(f'm = {m} \na = {a} \nn = {n}')

Q = m / sqrt(2 * np.log(2) / a)
m = m.n
a = a.n
n = n.n

print(f'Fitparameter:')
print(f'gaus(m)/ sqrt(2) = {gaus(m, m, a, n) / np.sqrt(2)}')
print(f'gaus(m-5) = {gaus(m-5, m, a, n)}')

print(f'Güte Q = {Q}')
print(f'{sqrt(2 * np.log(2) / a)}')

Q_opt = 50
m_opt = 35
a_opt = Q_opt / m_opt * 2 * np.log(2)
x = np.linspace(20, 50, 200)
plt.scatter(f,U, color='k', marker='+',
        label='Messdaten')
plt.plot(x, gaus(x,m,a,n), color='r',
        label='Curve Fit')
plt.plot(x, gaus(x,m_opt,a_opt,n * 1.2), color='b', ls='--',
        label='Ideale Filterkurve')

plt.xlabel(r'$f$ / kHz')
plt.ylabel(r'$U$ / V')
plt.legend()

plt.savefig('build/filterkurve.pdf')

