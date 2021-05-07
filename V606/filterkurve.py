# filterkurve.py

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.optimize import curve_fit
from uncertainties import ufloat
from uncertainties.umath import *

f, U = np.genfromtxt('Daten/filterkurve.txt', unpack=True)

data = {'f': f, 'U': U, 'U_norm': U / np.max(U)}
df = pd.DataFrame(data)
df = df.sort_values('f')
df.to_csv('build/filterkurve.tex', 
        sep='&', 
        header=False,
        index=False,
        line_terminator='\t\\\\\n',
        float_format='%.3f')

U = U / np.max(U)

# fitten eine Gaussglocke drüber
def gaus(x, m, a):
    n = 1
    return n * np.exp(-1 * a * (x - m)**2)

popt, pcov = curve_fit(gaus, f, U, p0=[35, 1.98])
errors = np.sqrt(np.diag(pcov))
m = ufloat(popt[0], errors[0])
a = ufloat(popt[1], errors[1])
#n = ufloat(popt[2], errors[2])
print(f'm = {m} \na = {a}')# \nn = {n}')

nu_plus = m + sqrt(1/(2*a) * np.log(2))
nu_minus = m - sqrt(1/(2*a) * np.log(2))
print(f'𝜈_+ = {nu_plus}')
print(f'𝜈_- = {nu_minus}')
print(f'd𝜈 = {nu_plus - nu_minus}')

Q = m / sqrt(2 * np.log(2) / a)
m = m.n
a = a.n
#n = n.n

print(f'Fitparameter:')
print(f'gaus(m)/ sqrt(2) = {gaus(m, m, a) / np.sqrt(2)}')
print(f'gaus(m-5) = {gaus(m-5, m, a)}')

print(f'Güte Q = {Q}')

Q_opt = 50
m_opt = 35
a_opt = Q_opt / m_opt * 2 * np.log(2)
x = np.linspace(20, 50, 200)
plt.scatter(f,U, color='k', marker='+',
        label='Messdaten')
plt.plot(x, gaus(x,m,a), color='r',
        label='Curve Fit')
plt.plot(x, gaus(x,m_opt,a_opt), color='b', ls='--',
        label='Ideale Filterkurve')
#plt.axline((20,1/np.sqrt(2)), (40,1/np.sqrt(2)))

plt.xlabel(r'$f$ / kHz')
plt.ylabel(r'$U_A / U_E$')
plt.legend()

plt.savefig('build/filterkurve.pdf')

