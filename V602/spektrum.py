import matplotlib.pyplot as plt
import numpy as np
import uncertainties as unc
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.optimize import curve_fit
import scipy.constants as const
from scipy.signal import find_peaks, peak_widths

th , n = np.genfromtxt('daten/Emissionsspektrum.dat', unpack=True)

N_MAX=np.amax(n)
print("N_MAX2=",N_MAX)

peaks, _ = find_peaks(n, height=1000)
assert len(peaks) == 2

Vpeaks = th[peaks]
results_half = peak_widths(n, peaks, rel_height=0.5)
w_h, l, r = results_half[1:]
l = (l/10 + 8) 
r = (r/10 + 8) 

#print(f"Halbwertsbreiten: {(r-l):.3f}°")


plt.plot(th,n,"--", label='Messdaten')
#plt.plot(th[0:120],n[0:120],'r--',label = 'Bremsberg')
plt.hlines(w_h, l, r, color='r', label='Halbwertsbreiten')
plt.axvline(x=20.2 ,linestyle= "--",color='k', label = r'$K_{\beta}$')
plt.axvline(x=22.5 ,linestyle="--", color='y', label = r'$K_{\alpha}$')
#plt.axvline(x=1)
plt.xlabel(r'$\theta \:/\: \si{°}$')
plt.ylabel(r'$N \:/\: \si{\frac{Imp}{s}}$')
plt.legend(loc='best')
plt.tight_layout()
plt.savefig('build/spektrum.pdf')