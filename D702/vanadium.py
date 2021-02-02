# vanadium.py

from untergrundrate import get_untergrund
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import polyfit
from uncertainties import unumpy, ufloat

N_U = get_untergrund()

df = pd.read_csv('daten/vanadium.csv')
df['DN'] = round(np.sqrt(df['N[Impulse]']))
df['N Korrigiert'] = round(df['N[Impulse]'] - N_U.n / 10)

#print(df)

t = df['t']
Dt = 30
N = df['N[Impulse]']
DN = np.sqrt(N)

# konvertiere in uarray und ziehe untergrund ab
uN = unumpy.uarray(N, DN)
uN = uN - N_U / 10

N = unumpy.nominal_values(uN)
DN = unumpy.std_devs(uN)

# polynom fit ersten grades
coef, cov = np.polyfit(t, np.log(unumpy.nominal_values(uN)), 1, cov=True)
err = np.sqrt(np.diag(cov))

lmd = ufloat(-1 * coef[0], err[0])
T = np.log(2) / lmd
lit = 3.743 * 60
error = (T - lit) / lit
print(f'Steigung der Ausgleichsgerade: {lmd}')
print(f'Halbwertszeit fuer vanadium: {T}')
print(f'Abweichung vom Literaturwert: {error:.4f}')

lmd = -1 * coef[0]
lmd_err = err[0]
N_0 = np.exp(coef[1]) / (1 - np.exp(-1 * lmd * Dt))
print(N_0)

# plot
plt.errorbar(t, N, yerr=DN, ls='', marker='+',
        label='Messdaten')
plt.fill_between(t, 10**2 * 2 * np.exp(-1 * (lmd-lmd_err) * t),
         10**2 * 2 * np.exp(-1 * (lmd+lmd_err) * t),
         alpha=0.3, color='r')
plt.plot(t, 10**2 * 2 * np.exp(-1 * lmd * t),
        color='r',
        label=f'Fit für $T=({T.n:.0f}\pm{T.s:.0f})$ s')

plt.title(r'Messdaten und Fit zum Zerfall von Vanadium-52')
plt.legend()
plt.xlabel(r'$t/$s')
plt.ylabel(r'Zerfälle / $30$s')
plt.yscale('log')
plt.savefig('build/vanadium.pdf')
