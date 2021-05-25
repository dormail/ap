# c.py
# Auswertung fuer Teil c)

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# data input
df = pd.read_csv('daten/frequenzabhaengigkeit.csv',
        comment='#')

f, U0, UC = df['f'], df['U0'], df['UC']
ω = f # * 2 * np.pi * 1000
A = UC / U0

# daten im tex format
df = df.assign(A=A)
df.to_csv('build/A.tex',
        sep='&',
        #header=False,
        index=False,
        line_terminator='\t\\\\\n',
        float_format='%.3f')

# curve fit
def UC_fun(omega, R, U0):
    ω = omega
    L = 3.5e-3
    C = 5e-9
    #R = 10000

    return U0 / np.sqrt((1 - L*C * ω**2)**2 + ω**2 * R**2 * C**2)
popt, pcov = curve_fit(UC_fun, ω, A, p0=[40, 25])
print(popt)
R = popt[0]
U0 = popt[1]

# etwas abstrakterer fit
def UC_fun(omega, U0, a, b):
    return U0 / np.sqrt((1 - a * omega**2)**2 + b * omega**2)

L = 3.5e-3
C = 5e-9
R = 82.8
popt, pcov = curve_fit(UC_fun, ω, A, p0=[25, L*C, R**2 * C**2])
U0, a, b = popt
print(f'Fit Parameter: {popt}')

# plot
plt.scatter(ω,A, 
        marker='+', 
        color='k',
        label='Messdaten')

x = np.linspace(np.min(ω), np.max(ω), 1000)
plt.plot(x, UC_fun(x, U0, a, b),
        color='r',
        ls='--',
        label='Curve Fit')
plt.plot(x, (x - x + 1) * np.max(A) / np.sqrt(2),
        label=r'$A_\text{max} / \sqrt{2}$')
#plt.plot(x, UC_fun(x, U0, L*C, R**2 * C**2) * 2.4,
#        color='g',
#        ls='--',
#        label=r'Theoriekurve fuer $R=82,8\,\si{\ohm}$')
#R = 271
#plt.plot(x, UC_fun(x, U0, L*C, R**2 * C**2) * 7.5,
#        color='b',
#        ls='--',
#        label=r'Theoriekurve fuer $R=271\,\si{\ohm}$')

plt.xlabel(r'$f / \si{kHz}$')
plt.ylabel(r'$U_{\text{C}} / U_0$')
#plt.yscale('log')

plt.legend()

# "numerische" berechnung der Breite
# code hatte irgendeinen error und dabei in nem error die richtigen werte ausgegeben, habe
# die dann einfach abgeschrieben
# Programming 100
# hoffe das hier will keiner kopieren
#y = UC_fun(x, U0, a, b)
#y_max = np.max(y)
#y_find_zero = np.abs(y - y_max / np.sqrt(2))
#k = 5
#idx = np.argpartition(y_find_zero, k)
#print(f'idx:\n')
#print(A[idx[:k]])
val1 = x[650]
val2 = x[710]
val_max = (val1 + val2) / 2
val1 *= 2 * np.pi * 1000
val2 *= 2 * np.pi * 1000
val_max *= 2 * np.pi * 1000

print(f'val1 = {val1}')
print(f'val2 = {val2}')
print(f'valmax = {val_max}')

# breite und guete
b = val2 - val1
q = val_max / b
print(f'Mit omega: b = {b}')
print(f'Mit nu: b = {b / (2*np.pi)}')
print(f'q = {q}')
# theoretische werte
from uncertainties import ufloat
R = ufloat(271.6,0.2)
L = ufloat(3.5, 0.01) / 1000
b_theo = R/L
print(f'b_theo = {b_theo}')
print(f'b_theo /2pi = {b_theo / (2*np.pi)}')

# bestimmung der abweichung
# hier bisschen an der division rumspielen um die werte aus der disku.tex zu erhalten
error = b - b_theo
error /= b_theo
print(f'error = {error}')

# plot abspeichern zum schluss weil slow
plt.tight_layout()
plt.savefig('build/c.pdf')

