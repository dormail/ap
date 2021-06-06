# phase.py

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.optimize import curve_fit

df = pd.read_csv('daten/phase.csv', comment='#')
phi = df['phi']
U = df['U']
phi = phi * 2 * np.pi / 360

# curve fit
def f(x, a , b, c, d):
    return a * np.sin(b * x + c) + d

popt, pcov = curve_fit(f, phi, U)
err = np.sqrt(np.diag(pcov))
a, b, c, d = popt[:]
a_err, b_err, c_err, d_err = err[:]

print(f'a = {a} \pm {a_err}')
print(f'b = {b} \pm {b_err}')
print(f'c = {c} \pm {c_err}')
print(f'd = {d} \pm {d_err}')



plt.scatter(phi, U,
        marker='+',
        label='Messdaten')
x = np.linspace(-1, 6.3)
plt.plot(x, f(x, a, b, c, d),
        color='k',
        label='Curve Fit')

plt.legend()
plt.xlabel(r'$\phi$')
plt.ylabel(r'$U / \si{V}$')

plt.xticks([0, np.pi/3, 2*np.pi/3, np.pi, 4 * np.pi / 3, 5 * np.pi/3, 2 * np.pi],
        [r"$0$", r"$\frac{\pi}{3}$", r"$\frac{2\pi}{3}$", r"$\pi$", r"$\frac{4\pi}{3}",
        r"$\frac{5\pi}{3}$", r"$2\pi$"])

plt.tight_layout()
plt.savefig('build/phase.pdf')

