import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy
import scipy.optimize as opt


### data import ###
d1 = pd.read_csv('daten/Wheatstone.csv')
R_2 = d1['R_2'] 
R_3 = d1['R_3']
R_4=1000-R_3
R_x=R_2*R_3/R_4
PotFehler=0.005*R_2
#mR_x=numpy.mean(R_x)
print(R_x)
sd=np.std(R_x, ddof=1)
sdm=sd/1.732
print(f'Standardabweichung: \t {sd:.4}')
print(f'FehlerMittelwert: \t {sdm:.4}')
print(f'Mittelwert: \t {np.mean(R_x):.7}')
print(f'Mittelwert der Fehler: \t {np.mean(PotFehler):.7}')
