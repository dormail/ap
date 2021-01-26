# untergrundrate.py

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from uncertainties import unumpy, ufloat

def get_untergrund():
    # daten input
    df = pd.read_csv('daten/untergrundrate.csv')
    N = df['N_U']
    
    # daten sind poisson verteilt, daher abweichung DN = sqrt(N)
    DN = np.sqrt(N)
    N = unumpy.uarray(N, DN)
    
    #
    N_U = sum(N) / len(N)
    return N_U

N_U = get_untergrund()
print(f'Die Untergrundrate betraegt {N_U}')
