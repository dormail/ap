import matplotlib.pyplot as plt
import numpy as np
import uncertainties as unc
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.optimize import curve_fit
import scipy.constants as const

th , n = np.genfromtxt('daten/Bragg.dat', unpack=True)

N_MAX=np.amax(n)
print("N_MAX=",N_MAX)

#plt.plot(x,x*pa_gl[0]+pa_gl[1], label='Ausgleichsgerade')
plt.plot(th,n,".", label='Messdaten')
plt.plot(28.2,N_MAX,'r.',label = 'Maximum')
plt.xlabel(r'$\theta \:/\: °$')
plt.ylabel(r'$N \:/\: \frac{Imp}{s}$')
plt.legend(loc='best')
plt.tight_layout()
plt.savefig('build/bragg.pdf')