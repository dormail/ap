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
d1 = pd.read_csv('daten/CWert9.csv')
C_2 = d1['C2/nF']
R_2 = d1['R2'] 
R_3 = d1['R3']
R_4=1000-R_3
p=unp.uarray(R_3/R_4,0.005*R_3/R_4)
p1=unp.uarray(R_4/R_3,0.005*R_4/R_3)
R2=unp.uarray(R_2,0.03*R_2)
R_x=R2*p
C_x=C_2*p1
mC_x=np.mean(noms(C_x))
mR_x=np.mean(noms(R_x))
#print(C_x)
#print(noms(R_x))
#print(stds(R_x))
sdc=np.std(noms(C_x), ddof=1)
sdmc=sdc/(2**(1/2))

sdr=np.std(noms(R_x), ddof=1)
sdmr=sdr/(2**(1/2))
#print(f'Standardabweichung: \t {sd:.4}')
#print(f'FehlerMittelwert: \t {sdm:.4}')
#print(f'Mittelwert: \t {mR_x:.4}')
c=ufloat(mC_x,np.mean(stds(C_x))+sdmc)
u=ufloat(mR_x,np.mean(stds(R_x))+sdmr)
print(f'Wert_9_C_x[nF]= \t {c:.5}')
print(f'Wert_9_R_x= \t {u:.5}')

