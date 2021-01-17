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
d1 = pd.read_csv('daten/WienRobinson.csv')
f = d1['f'] 
U_Br = d1['2U_Br']/2
f0=160
om=f/f0
U=U_Br/10

f0theo=160.11
omtheo=np.linspace(20,30000,num=10000)/f0theo
Utheo=(1/9*((omtheo**2-1)**2/((1-omtheo**2)**2+9*omtheo**2)))**0.5

plt.plot(om, U,"o", label='Messdaten', linewidth=1.0)
plt.plot(omtheo, Utheo, label='Theorie-Kurve', linewidth=1.0)
plt.xscale('log')
plt.xlabel(r'$f/f_0 \:$')
plt.ylabel(r'$U_{Br}/U_S \:$')
plt.legend(loc='best')

plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/WRplot.pdf')
