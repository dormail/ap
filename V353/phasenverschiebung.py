### phasenverschiebung.py ###
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

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

# plot
plt.scatter(f,phi)


plt.savefig('phasenverschiebung.pdf')

