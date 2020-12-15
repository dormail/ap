import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy
import scipy.optimize as opt
from uncertainties import ufloat
import uncertainties.unumpy as unp
from uncertainties.unumpy import (nominal_values as noms,
                                  std_devs as stds)


### data import ###
d1 = pd.read_csv('daten/Wheatstone.csv')
R_2 = d1['R_2'] 
R_3 = d1['R_3']
R_4=1000-R_3
y=unp.uarray(R_3/R_4,0.005*R_3/R_4)
R_x=R_2*y

mR_x=np.mean(noms(R_x))
#print(R_x)
#print(noms(R_x))
#print(stds(R_x))
sd=np.std(noms(R_x), ddof=1)
sdm=sd/1.732
#print(f'Standardabweichung: \t {sd:.4}')
#print(f'FehlerMittelwert: \t {sdm:.4}')
#print(f'Mittelwert: \t {mR_x:.4}')
u=ufloat(mR_x,np.mean(stds(R_x))+sdm)
print(f'Wert_11_R_x= \t {u:.4}')