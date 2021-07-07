# mfp.py
# Skript zur Berechnung der mittleren freien Weglänge 
import numpy as np

def mfp(T):
    # T in K
    # p in mbar
    p = 5.5e7 * np.exp(-6876 / T)
    w = 0.0029 / p
    return w

KC = 273
T = np.array([25, 148, 168, 197.5])
T = T + KC

print('Berechnung mittlere freie Weglänge')
for t in T:
    print(f'mfp({t - KC} K) = {mfp(t):.4e} cm')
    print(f'n({t - KC} K) = {1 / mfp(t):.4e} / cm')

