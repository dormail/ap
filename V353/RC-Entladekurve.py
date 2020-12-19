### RC-Entladekurve.py ###
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

# daten input
df = pd.read_csv('daten/RC-Entladekurve.csv')
t = df['t'] # ist halt jetzt nicht SI :(
U = df['U']

# frequenz der Quelle
f = 999

# funktion die entlade vorgang beschreibt
# U0 Spannung zu t=0
# T Zeitkonstante des RC-Glieds
def UC(t, U0, T):
    return U0 * np.exp(-1 * t / T)

# curve fit
p0 = [2.2, 100]
popt, pcov = curve_fit(UC, t, U, p0=p0)
U0 = popt[0]
T = popt[1]
U0_err = np.sqrt(np.diag(pcov)[0])
T_err = np.sqrt(np.diag(pcov)[1])
error = [U0_err, T_err]

# teste die pcov
print(pcov)

# ausgabe auf terminal
print(f'Ergebnisse vom curve_fit:')
print(f'U0 = {U0} ± {error[0]:.2}')
print(f'T = {T:.4} ± {error[1]:.2}')

# plot
t_plt = np.linspace(0, 180)
#t_plt = np.linspace(0, 0.00018)
plt.scatter(t,U, marker='+', label='Messdaten')
plt.plot(t_plt, UC(t_plt, U0, T), color='r', label=rf'curve fit für $RC={{{T:.5}}}\mu s$')
plt.legend()

plt.title('Entladung eines RC-Kreises')
plt.xlabel(r'$t/(\mu \si{s})$')
plt.ylabel(r'$U_C / \si{V}$')

plt.savefig('build/4a.pdf')
