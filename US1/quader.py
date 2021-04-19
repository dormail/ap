import matplotlib.pyplot as plt
import numpy as np
import scipy
import scipy.constants as const
import scipy.optimize as opt
from uncertainties import ufloat
import uncertainties.unumpy as unp
from uncertainties.unumpy import (nominal_values as noms,
                                  std_devs as stds)

s, t = np.genfromtxt('content/quaderdaten.txt', unpack=True)
print(s)
print(t)
S=np.sort(s)
T=np.sort(t)
print(S)
params, covariance_matrix = np.polyfit(T, S, deg =1 , cov = True)
errors = np.sqrt(np.diag(covariance_matrix))
print(f'a = {params[0]} +- {errors[0]}')
print(f'b = {params[1]} +- {errors[1]}') 
plt.errorbar(T, S, fmt='.', label = 'Messwerte')
plt.plot(T, params[0] * T + params[1], label = 'Ausgleichs-Gerade')
plt.xlabel(r'$t [\si{\micro \second}]$')
plt.ylabel(r'$s [\si{\milli \meter}]$')
plt.legend(loc='best')
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/plot.pdf')

#daempfung
a1, a2, d = np.genfromtxt('content/daempfung.txt', unpack=True)
