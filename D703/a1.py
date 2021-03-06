import matplotlib.pyplot as plt
import numpy as np
import scipy
import scipy.constants as const
import scipy.optimize as opt
from uncertainties import ufloat
import uncertainties.unumpy as unp
from uncertainties.unumpy import (nominal_values as noms,
                                  std_devs as stds)



### data import ###

U, N = np.genfromtxt('Daten/Kennlinie.dat', unpack=True)
Up = U[5:-11]
Np = N[5:-11]

params, covariance_matrix = np.polyfit(Up, Np, deg =1 , cov = True)
errors = np.sqrt(np.diag(covariance_matrix))
x = np.linspace(Up[0], Up[-1])

print(f'a = {params[0]} +- {errors[0]}')
print(f'b = {params[1]} +- {errors[1]}') 
#print(Np) 
y=params[0] * 370 + params[1]
z=params[0] * 470 + params[1]
print(((z-y))/y)
plt.clf()
dN=np.sqrt(N)
plt.errorbar(U, N,  yerr=dN, fmt='.', label = r'Messwerte mit Fehler')
plt.plot(x, params[0] * x + params[1], label = 'Plateau-Gerade')

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

#c
N1 = 96041 / 120
N2 = 76518 / 120
N12 = 158479 / 120

n1 =  ufloat(N1, np.sqrt(N1))
n2 =  ufloat(N2, np.sqrt(N2))
n12 = ufloat(N12, np.sqrt(N12))

T = (n1 + n2 - n12) / (2 * n1 * n2)
print(f'Totzeit = {T:.6f}')

#d
U, I ,N0= np.genfromtxt('Daten/Zaehlrohrstrom.dat', unpack=True)
I=I/1000000
I0 = unp.uarray(I, 0.05/1000000)
Z = I0 / ((const.epsilon_0*N0))
print(Z)
Z=Z/(1.602*10**(-19))
print(Z)
Zn = unp.nominal_values(Z)
Zf  = unp.std_devs(Z)
plt.figure()
plt.errorbar(U, Zn, yerr = Zf, fmt = '.')
plt.xlabel('U[V]') 
plt.ylabel('Z[1*e]')
plt.tight_layout()
plt.savefig('build/plotd.pdf')