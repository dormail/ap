### RC-Entladekurve.py ###
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('daten/RC-Entladekurve.csv')
t = df['t']
U = df['U']

# frequenz der Quelle
f = 999

plt.scatter(t,U)
plt.savefig('RC.pdf')
