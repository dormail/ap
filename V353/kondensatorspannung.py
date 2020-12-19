### generatorspannung.py ###
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

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

# plot
plt.scatter(f,A)


plt.savefig('spannungsverhaeltnis.pdf')
