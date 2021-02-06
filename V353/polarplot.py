""" polarplot.py start """
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

# phasenverschiebung.py
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

f_c = f
phi_c = phi

# curve fit
def phi_fit(f, T):
    omega = 2 * np.pi * f
    return np.arctan(-1 * omega * T)

p0 = [0.00089]
Tc, pcov = curve_fit(phi_fit, f, phi, p0=p0)
err = np.sqrt(np.diag(pcov))[0]
Tc = -1 * Tc[0] # RC nach berechnung von 4c

# output
T = Tc
print('Fit-Ergebnisse für Phasenverschiebung:')
print(f'RC = ({T * 10**6:.4f} ± {err * 10*6:.4f}) micro-seconds')

# amplitudenverhaeltnis
# daten input, anpassung auf SI-Größen
df = pd.read_csv('daten/kondensatorspannung1.csv')
f1 = df['f']
A1 = df['A']
df = pd.read_csv('daten/kondensatorspannung2.csv')
f2 = df['f'] * 1000
A2 = df['A'] / 1000

# Spannung der Quelle
U0 = 4.2

# merge arrays
f = np.append(f1, f2)
A = np.append(A1, A2)

# anpassung auf spannungsverhaeltnis
A = A / 4.2

# curve fit
def AC(f, T):
    #U0 = 4.2
    U0 = 1 # damit das Verhaeltnis dargestellt wird
    w = 2 * np.pi * f
    return U0 / (np.sqrt(1 + w**2 * T**2))

p0 = [0.0008]
om = 2 * np.pi * f
popt, pcov = curve_fit(AC, f, A, p0=p0)
U0 = 4.2
Tb = popt[0]
err = np.sqrt(np.diag(pcov))[0]

# output
T = Tb
print('Fit-Ergebnisse für Amplitudenverhaeltnis:')
print(f'RC = {10**6*T:.1f} ± {10**6*err:.2} micro-seconds')

# plotting
fig = plt.figure()
ax = fig.add_subplot(111, polar=True)

RC = Tc
# plot von messwerten
ax.scatter(phi_c, AC(f_c, RC), marker='+', 
        linewidth=1, label='Messwerte zur Phasenverschiebung')
ax.scatter(phi_fit(-1 * f[0:7], RC), A[0:7], marker='x', color='k',
        linewidth=0.8, label='Messwerte zum Amplitudenverhältnis')

f = np.linspace(10**-2, 10**4, 10**5)
# plot fuer wert laut phase
plt.polar(phi_fit(-1 * f, RC), AC(f, RC), label=rf'Theoriekurve für $RC = {10**6 * RC:.2f}$',
        linewidth=0.5, color='r')

ax.set_thetamin(120)
ax.set_thetamax(-10)
ax.set_rlabel_position(0)

ax.grid(True)

plt.title('Polarplot der Messergebnisse')
plt.xticks([0, np.pi/8, np.pi/4,  3*np.pi/8, np.pi/2],
        [r"$0$", r"$\frac{\pi}{8}$", r"$\frac{\pi}{4}$",  r"$\frac{3\pi}{8}$", r"$\frac{\pi}{2}$"])
plt.legend()
plt.tight_layout()
plt.savefig('build/polarplot.pdf')

""" polarplot.py end """
