# untergrundrate.py

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from uncertainties import unumpy, ufloat

def get_untergrund():
    # daten input
    t = 300
    df = pd.read_csv('daten/untergrundrate.csv')
    N = df['N_U']
    
    # daten sind poisson verteilt, daher abweichung DN = sqrt(N)
    DN = np.sqrt(N)
    N = unumpy.uarray(N, DN)
    #print(N)
    
    #
    N_U = sum(N) / len(N)
    #N_U = N_U / t # falls man es auf 1 sekunde normieren moechte
    return N_U

N_U = get_untergrund()
#print(f'Die Untergrundrate betraegt {N_U}')
