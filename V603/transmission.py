# transmission.py

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from uncertainties import unumpy, ufloat

tau = 90 * 10**-6 # 90 micro second Totzeit
T = 200
d_LiF = 201.4
d_LiF *= 10**(-12)

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
a_err, b_err = np.sqrt(np.diag(pcov))
x = np.linspace(7, 10)

# ausgabe der fit ergebnisse
a_uf = ufloat(a, a_err)
b_uf = ufloat(b, b_err)
print(f'a = {a_uf}')
print(f'b = {b_uf}')

# plotting
fig, ax1 = plt.subplots()

ax1.plot(x, f(x, a, b),
        label='Ausgleichsgerade')

ax1.scatter(alpha, unumpy.nominal_values(trans), marker='+',
        label='Transmissionskoeffizient')
ax1.errorbar(alpha, unumpy.nominal_values(trans),
        yerr=unumpy.std_devs(trans),
        marker='+',
        linestyle='',
        label='Transmissionskoeffizient')

# visuals
ax1.set_xlabel(r'$\alpha$')
ax1.set_ylabel(r'$N / (\text{Imp} / \text{s})$')
#plt.yscale('log')
ax1.legend()

# second x scale
# define functions which convert alpha to lambda
def lam(x):
    return 2 * d_LiF * np.sin(x * np.pi / 180)

def inv_lam(lam):
    return 180 / np.pi * np.arcsin(lam / (2*d_LiF))

ax2 = ax1.secondary_xaxis('top', functions=(lam, inv_lam))
ax2.set_xlabel(r'$\lambda /$m')


fig.tight_layout()

fig.savefig('build/transmission.pdf')
print('Figure saved in build/transmission.pdf')

# part 3.3
d = 201.4e-12

T1 = 0.432
T2 = 0.375

alpha1 = (T1 - b_uf) / a_uf
alpha2 = (T2 - b_uf) / a_uf

lam1 = 2 * d * unumpy.sin(alpha1)
lam2 = 2 * d * unumpy.sin(alpha2)
print(f'lambda1 = {lam1}')
print(f'lambda2 = {lam2}')
dLambda = -1 * lam1 + lam2
print(f'dLambda = {-1 * lam1 + lam2}')

# abweichung
lambda_C_lit = 2.43e-12
Err = (dLambda - lambda_C_lit) / lambda_C_lit
print(f'Error = {Err}')
