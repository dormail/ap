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
d1 = pd.read_csv('daten/IMessBr.csv')
L_2 = d1['L2/mH']
R_2 = d1['R2'] 
R_3 = d1['R3']
R_4=1000-R_3
p=unp.uarray(R_3/R_4,0.005*R_3/R_4)
p1=unp.uarray(R_4/R_3,0.005*R_4/R_3)
R2=unp.uarray(R_2,0.03*R_2)
R_x=R2*p
L_x=L_2*p
mL_x=np.mean(noms(L_x))
mR_x=np.mean(noms(R_x))
print(L_x)
#print(noms(R_x))
#print(stds(R_x))
sdl=np.std(noms(L_x), ddof=1)
sdml=sdl/(3**(1/2))

sdr=np.std(noms(R_x), ddof=1)
sdmr=sdr/(3**(1/2))
#print(f'Standardabweichung: \t {sd:.4}')
#print(f'FehlerMittelwert: \t {sdm:.4}')
#print(f'Mittelwert: \t {mR_x:.4}')
c=ufloat(mL_x,np.mean(stds(L_x))+sdml)
u=ufloat(mR_x,np.mean(stds(R_x))+sdmr)
print(f'Wert_19_L_x[mH]= \t {c:.5}')
print(f'Wert_19_R_x= \t {u:.5}')



