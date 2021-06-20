# 1.py

import numpy as np
import matplotlib.pyplot as plt

data = [19.5, 25.5, 29.5, 35.5, 41, 46, 51]
data = np.array(data)

x = [20, 25, 29, 35, 40, 45, 50]
x = np.array(x)

rel = data / x
print(rel)
mean = np.mean(rel)
std = np.std(rel)
print(f'rel = {mean} pm {std}')

plt.scatter(x, rel,
        marker='+',
        label=r'Messdaten')

plt.axline((x.min(), mean), (x.max(), mean),
        c='r',
        label='Mittelwert')

plt.axline((x.min(), 1), (x.max(), 1),
        c='g',
        label='Theoriewert')

xplot = np.linspace(x.min(), x.max())
plt.fill_between(xplot, mean - std, mean + std,
        color='r',
        linestyle=':',
        alpha=0.3,
        label='Standartabweichung')

plt.ylabel(r'$\alpha_1 / \alpha_2$')
plt.xlabel(r'$\alpha_1$')
plt.legend()

plt.savefig('build/1.pdf')

