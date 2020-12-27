### phasenverschiebung.py ###
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

# daten input, anpassung auf SI-Größen
df = pd.read_csv('daten/4c-1.csv')
f1 = df['f']
a1 = df['a']
b1 = df['b']
df = pd.read_csv('daten/4c-2.csv')
f2 = df['f'] * 1000
a2 = df['a']
b2 = df['b']

# Spannung der Quelle
U0 = 4.2

# merge arrays
f = np.append(f1, f2)
a = np.append(a1,a2)
b = np.append(b1, b2)
phi = a/b * 2 * np.pi

# neues dataframe fuer ausgabe
d = {'f': f, 'a': a, 'b':b, 'phi':phi}
df_new = pd.DataFrame(d)
print(df_new)

# curve fit
def phi_fit(f, T):
    omega = 2 * np.pi * f
    return np.arctan(-1 * omega * T)

p0 = [0.00089]
T, pcov = curve_fit(phi_fit, f, phi, p0=p0)
err = np.sqrt(np.diag(pcov))[0]
T = T[0]

# output
print(f'RC = ({-1*T * 10**6:.4f} ± {err * 10*6:.4f}) micro-seconds')

# plot
phi_plt = np.linspace(30, 10**5, 10**4)
plt.plot(phi_plt, phi_fit(phi_plt, T), color='r', label=rf'Curve Fit für $RC = {-1*T * 10**6:.2f}\mu\si{{s}}$')
plt.scatter(f,phi, marker='+', label='Messdaten')

plt.title(r'Phasenverschiebung zwischen $U_C$ und $U_G$')
plt.xlabel(r'$f \cdot \si{s}$')
plt.ylabel(r'$\varphi$')
plt.legend()
#plt.xlim(0,10000)
plt.xscale('log')

plt.savefig('build/4c.pdf')
