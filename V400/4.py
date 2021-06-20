# 4.py

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

n = 1.55 # Brechungsindex von Cronglas

alpha1 = [30, 35, 40, 45, 50]
alpha1 = np.array(alpha1)
alpha1 = alpha1 * 2 * np.pi / 360

alpha2red = [77, 65, 57, 51, 45]
alpha2red = np.array(alpha2red)
alpha2red = alpha2red * 2 * np.pi / 360

alpha2green = [78, 66, 58, 52, 45.5]
alpha2green = np.array(alpha2green)
alpha2green = alpha2green * 2 * np.pi / 360

# Berechnung der beta
beta1 = np.arcsin(np.sin(alpha1) / n)
beta2red = np.arcsin(np.sin(alpha2red) / n)
beta2green = np.arcsin(np.sin(alpha2green) / n)

# berechnung von delta
delta_red = (alpha1 + alpha2red) - beta1 - beta2red
delta_green = (alpha1 + alpha2green) - beta1 - beta2green

# Rückkonvertierung nach Grad
conv = 360 / (2 * np.pi) # conversion rad -> deg
alpha1 = alpha1 * conv
alpha2red = alpha2red * conv
alpha2green = alpha2green * conv
beta1 = beta1 * conv
beta2red = beta2red * conv
beta2green = beta2green * conv
delta_red = delta_red * conv
delta_green = delta_green * conv

# plotting
plt.scatter(alpha1, delta_red,
        c='r',
        marker='+',
        label='Roter Laser')

plt.scatter(alpha1, delta_green,
        c='g',
        marker='+',
        label='Grüner Laser')

plt.xlabel(r'Einfallwinkel $\alpha_1 / \text{deg}$')
plt.ylabel(r'Ablenkung $\delta / \text{deg}$')
plt.legend()
plt.tight_layout()

plt.savefig('build/4.pdf')
print('Figure saved at build/4.pdf')

# export fuer das protokoll
d = {'alpha1': alpha1,
        'alpha2red': alpha2red,
        'alpha2green': alpha2green,
        'beta1': beta1,
        'beta2red': beta2red,
        'beta2green': beta2green,
        'delta_red': delta_red,
        'delta_green': delta_green}
data = pd.DataFrame(data=d)
data.to_csv('build/4.tex',
        sep='&',
        #header=False,
        index=False,
        line_terminator='\t\\\\\n',
        float_format='%.3f')
print('Data saved at build/4.tex')

