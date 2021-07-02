# 2.py

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from uncertainties import unumpy as unp

alpha = [30, 35, 40, 50, 55, 60, 70]
alpha = unp.uarray(alpha, np.ones_like(alpha))
alpha = alpha * 2 * np.pi / 360

beta = [19, 24, 26, 31, 34, 36, 39.5]
beta = np.array(beta)
beta = unp.uarray(beta, np.ones_like(beta))
beta = beta * 2 * np.pi / 360

sina = unp.sin(alpha)
sinb = unp.sin(beta)

relsin = sina / sinb
print(f'relsin\n{relsin}\n')

mean = relsin.mean()
print(f'n = {mean}')
std = mean.s
mean = mean.n

# export fuer das protokoll
conv = 360 / (2 * np.pi) # konstante fuer rad -> deg
alpha_deg = alpha * conv
beta_deg = beta * conv
d = {'alpha': alpha_deg,
        'beta': beta_deg,
        'sina': sina,
        'sinb': sinb,
        'relsin': relsin}
data = pd.DataFrame(data=d)
data.to_csv('build/2.tex',
        sep='&',
        #header=False,
        index=False,
        line_terminator='\t\\\\\n',
        float_format='%.3f')

# plotting
plt.errorbar(unp.nominal_values(alpha), unp.nominal_values(relsin),
        yerr=unp.std_devs(relsin),
        xerr=unp.std_devs(alpha),
        fmt='none',
        label=r'Messdaten')

alpha_nom = unp.nominal_values(alpha)
plt.axline((alpha_nom.min(), mean), (alpha_nom.max(), mean),
        c='r',
        label='Mittelwert')

plt.axline((alpha_nom.min(), 1.49), (alpha_nom.max(), 1.49),
        c='g',
        label=r'Theoriewert $n=1,49$')

xplot = np.linspace(alpha_nom.min(), alpha_nom.max())
plt.fill_between(xplot, mean - std, mean + std,
        color='r',
        linestyle=':',
        alpha=0.3,
        label='Standartabweichung')

plt.xlabel(r'$\alpha / \deg$')
plt.ylabel(r'$\sin(\alpha) / \sin(\beta)$')
plt.legend()

plt.savefig('build/2.pdf')

# part 3: Strahlversatz
d = 0.0585
alpha = [30, 35, 40, 50, 55, 60, 70]
alpha = np.array(alpha)
alpha = alpha * 2 * np.pi / 360

beta = [19, 24, 26, 31, 34, 36, 39.5]
beta = np.array(beta)
beta = beta * 2 * np.pi / 360

sina = np.sin(alpha)
sinb = np.sin(beta)

s = d * np.divide(np.sin(np.subtract(alpha, beta)), sinb)
s = np.round(s, 3)
print(f'Strahlversatz s = {s}')

