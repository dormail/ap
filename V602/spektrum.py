import matplotlib.pyplot as plt
import numpy as np
import uncertainties as unc
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.optimize import curve_fit
import scipy.constants as const

th , n = np.genfromtxt('daten/Emissionsspektrum.dat', unpack=True)

N_MAX=np.amax(n)
print("N_MAX2=",N_MAX)


plt.plot(th,n,".", label='Messdaten')
plt.plot(th[0:120],n[0:120],'r--',label = 'Bremsberg')
plt.plot(th[127:143],n[127:143],'r--')
plt.plot(th[150:180],n[150:180],'r--')
#plt.axvline(theta_peak_cu[0],  ls = '--', label = r'$K_{\mathrm{\beta}}$')
#plt.axvline(theta_peak_cu[1], color='g', ls = '--', label = r'$K_{\mathrm{\alpha}}$')
plt.xlabel(r'$\theta \:/\: °$')
plt.ylabel(r'$N \:/\: \frac{Imp}{s}$')
plt.legend(loc='best')
plt.tight_layout()
plt.savefig('build/spektrum.pdf')