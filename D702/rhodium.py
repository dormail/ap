# rhodium.py

from untergrundrate import get_untergrund
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import polyfit
from uncertainties import unumpy, ufloat

N_U = get_untergrund()

df = pd.read_csv('daten/rhodium.csv')
df['DN'] = round(np.sqrt(df['N']))
df['N Korrigiert'] = round(df['N'] - N_U.n / 20)

print(df)

t = df['t']
Dt = 15
N = df['N Korrigiert']
DN = np.sqrt(N)

# Ausgleichsrechnung fuer langsamen Zerfall
N_slow = N[19:-1]
t_slow = t[19:-1]

print(f'Langsamer Zerfall startet bei {t[19]}s')
coef, cov = np.polyfit(t_slow, np.log(N_slow), 1, cov=True)
err = np.sqrt(np.diag(cov))
lmd = ufloat(-1 *  coef[0], err[0])
T_slow = np.log(2) / lmd
lit = 260.4
error = (T_slow - lit) / lit
print(f'Steigung der Ausgleichsgerade: {lmd}')
print(f'Halbwertszeit fuer langsames Rhodium: {T_slow}')
print(f'Abweichung vom Literaturwert: {error:.4f}')

x = np.linspace(300, 660)
plt.plot(x, 90 * np.exp(x * -1 * lmd.n),
        color='k',
        label=f'Langsamer Zerfall (T = {T_slow.n:.0f} s)')

# Kurzlegebiger Zerfall ###
N_fast = N[0:8]
t_fast = t[0:8]
print(f'Schneller Zerfall geht bis {t_fast[len(t_fast) - 1]}s')

N_korr = 667 * (1 - np.exp(-1 * lmd.n * Dt)) * np.exp(-1 * lmd.n * t_fast)

coef, cov = np.polyfit(t_fast, np.log(N_fast - N_korr), 1, cov=True)
err = np.sqrt(np.diag(cov))
lmd = ufloat(-1 *  coef[0], err[0])
T_fast = np.log(2) / lmd
lit = 42.3
error = (T_fast - lit) / lit
print(f'Steigung der Ausgleichsgerade: {lmd}')
print(f'Halbwertszeit fuer schnelles Rhodium: {T_fast}')
print(f'Abweichung vom Literaturwert: {error:.4f}')

x = np.linspace(0, 150)
plt.plot(x, 800 * np.exp(x * -1 * lmd.n),
        color='r',
        label=f'Schneller Zerfall (T = {T_fast.n:.0f} s)')

# plots
plt.errorbar(t,N, yerr=DN,
        ls='', marker='+',
        label='Messdaten')


plt.legend()
plt.xlabel(r'$t/$s')
plt.ylabel(r'Zerfälle / $15$s')
plt.yscale('log')
plt.savefig('build/rhodium.pdf')
