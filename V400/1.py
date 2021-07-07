# 1.py

import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat, unumpy

data = [19.5, 25.5, 29.5, 35.5, 41, 46, 51]
data = np.array(data)
unc = np.ones_like(data)
data_unc = unumpy.uarray(data, unc)

x = [20, 25, 29, 35, 40, 45, 50]
x = np.array(x)
x_err = np.ones_like(x)
x_unc = unumpy.uarray(x, x_err)

rel = data / x
rel_unc = data_unc / x_unc
print(rel_unc)
mean = np.mean(rel)
std = np.std(rel)
mean_unc = rel_unc.mean()

print(f'mean = {mean} pm {std}')
print(f'mean_unc = {mean_unc}')

plt.errorbar(x, unumpy.nominal_values(rel_unc),
        yerr=unumpy.std_devs(rel_unc),
        xerr=x_err,
        fmt='none',
        label=r'Messdaten')


mean = mean_unc.n
std = mean_unc.s
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
plt.xlabel(r'$\alpha_1 / \text{deg}$')
plt.legend()
plt.tight_layout()

plt.savefig('build/1.pdf')

