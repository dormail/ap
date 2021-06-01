# glanzwinkel-theo.py
import numpy as np

h = 6.626e-34
c = 2.99e8
d = 201.4e-12

def theta_glanz(E):
    return np.arcsin(h*c / (E *2 *d)) * 360 / (2 * np.pi)

# K_α
E = 8.06e3 * 1.602e-19
theta = theta_glanz(E)
print(f'K_α: 𝜃 = {theta}')

# K_β
E = 8.92e3 * 1.602e-19
theta = theta_glanz(E)
print(f'K_β: 𝜃 = {theta}')
