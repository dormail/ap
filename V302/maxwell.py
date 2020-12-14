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
d1 = pd.read_csv('daten/Maxwell.csv')
C_4 = d1['C4/nF']
C_4/=1000000 #jetzt in mF
R_2 = d1['R2'] 
R_3 = d1['R3']
R_4 = d1['R4']
R3=unp.uarray(R_3,0.03*R_3)
R4=unp.uarray(R_4,0.03*R_4)
R_x=R_2*R3/R4
L_x=R_2*R3*C_4
mL_x=np.mean(noms(L_x))
mR_x=np.mean(noms(R_x))
#print(C_x)
#print(noms(R_x))
#print(stds(R_x))
sdl=np.std(noms(L_x), ddof=1)
sdml=sdl/(2**(1/2))

sdr=np.std(noms(R_x), ddof=1)
sdmr=sdr/(2**(1/2))
#print(f'Standardabweichung: \t {sd:.4}')
#print(f'FehlerMittelwert: \t {sdm:.4}')
#print(f'Mittelwert: \t {mR_x:.4}')
c=ufloat(mL_x,np.mean(stds(L_x))+sdml)
u=ufloat(mR_x,np.mean(stds(R_x))+sdmr)
print(f'MW_Wert_19_L_x[mH]= \t {c:.5}')
print(f'MW_Wert_19_R_x= \t {u:.5}')



