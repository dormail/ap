import matplotlib.pyplot as plt
import numpy as np
import uncertainties.unumpy as unp
#import sympy
from scipy.optimize import curve_fit
from uncertainties import ufloat

t, T1, p1, T2, p2, N = np.genfromtxt('Daten.dat', unpack=True)
plt.clf()
#a
#plt.plot(t, T1,'o', label='Temperatur T1')
#plt.plot(t, T2,'o', label='Temperatur T2')
plt.errorbar(t, T1, xerr=0, yerr=.1, fmt='.', label = r'Messwerte T1')
plt.errorbar(t, T2, xerr=0, yerr=.1, fmt='.', label = r'Messwerte T2')
plt.xlabel(r'$t [min]$')
plt.ylabel(r'$T [\si{\celsius}]$')
plt.legend(loc='best')
plt.grid()
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/plot.pdf')

#b
def fit(x,A,B,C): 
    return A*x**2 + B*x + C

params1, covariance_matrix1 = curve_fit(fit,t, T1)
errors1 = np.sqrt(np.diag(covariance_matrix1))
params2, covariance_matrix2 = curve_fit(fit,t, T2)
errors2 = np.sqrt(np.diag(covariance_matrix2))
   
for name, value, error in zip('ABC', params1, errors1):
        print(f'{name} = {value:.6f} ± {error:.6f}')

for name, value, error in zip('XYZ', params2, errors2):
        print(f'{name} = {value:.6f} ± {error:.6f}')



plt.plot(
    t,fit(t, *params1), "-",label='Approximationskurve zu T1',
    #linewidth=3,
    )
plt.plot(
    t,fit(t, *params2), "-",label='Approximationskurve zu T2',)
plt.legend(loc='best')
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/plot1.pdf')
