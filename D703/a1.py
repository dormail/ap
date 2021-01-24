import matplotlib.pyplot as plt
import numpy as np
import scipy
import scipy.optimize as opt
from uncertainties import ufloat
import uncertainties.unumpy as unp
from uncertainties.unumpy import (nominal_values as noms,
                                  std_devs as stds)



### data import ###

U, N = np.genfromtxt('Daten/Kennlinie.dat', unpack=True)
#print(U) 
#print(N) 
plt.clf()
dN=np.sqrt(N)
plt.errorbar(U, N,  yerr=dN, fmt='.', label = r'Messwerte mit Fehler')
plt.xlabel(r'$U [\si{\volt}]$')
plt.ylabel(r'$N [ Imp / 60 s]$')
plt.legend(loc='best')
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/plot1.pdf')





