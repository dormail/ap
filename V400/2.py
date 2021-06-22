# 2.py

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

alpha = [30, 35, 40, 50, 55, 60, 70]
alpha = np.array(alpha)
alpha = alpha * 2 * np.pi / 360

beta = [19, 24, 26, 31, 34, 36, 39.5]
beta = np.array(beta)
beta = beta * 2 * np.pi / 360

sina = np.sin(alpha)
sinb = np.sin(beta)

relsin = sina / sinb
print(relsin)

mean = np.mean(relsin)
std = np.std(relsin)
print(f'n = {mean} \pm {std}')

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
plt.scatter(alpha, relsin,
        marker='+',
        label=r'Messdaten')

plt.axline((alpha.min(), mean), (alpha.max(), mean),
        c='r',
        label='Mittelwert')

plt.axline((alpha.min(), 1.49), (alpha.max(), 1.49),
        c='g',
        label=r'Theoriewert $n=1,49$')

xplot = np.linspace(alpha.min(), alpha.max())
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

