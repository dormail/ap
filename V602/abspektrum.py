import matplotlib.pyplot as plt
import numpy as np
import uncertainties as unc
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.optimize import curve_fit
import scipy.constants as const

#Brom
thb , nb = np.genfromtxt('daten/Brom.dat', unpack=True)

plt.plot(thb,nb,".", label='Messdaten')
plt.xlabel(r'$\theta \:/\: °$')
plt.ylabel(r'$N \:/\: \frac{Imp}{s}$')
plt.legend(loc='best')
plt.tight_layout()
plt.savefig('build/Brom.pdf')
plt.figure()
#gallium
thga , nga = np.genfromtxt('daten/Gallium.dat', unpack=True)

plt.plot(thga,nga,".", label='Messdaten')
plt.xlabel(r'$\theta \:/\: °$')
plt.ylabel(r'$N \:/\: \frac{Imp}{s}$')
plt.legend(loc='best')
plt.tight_layout()
plt.savefig('build/Gallium.pdf')
plt.figure()
#Rubidium
thr , nr = np.genfromtxt('daten/Rubidium.dat', unpack=True)

plt.plot(thr,nr,".", label='Messdaten')
plt.xlabel(r'$\theta \:/\: °$')
plt.ylabel(r'$N \:/\: \frac{Imp}{s}$')
plt.legend(loc='best')
plt.tight_layout()
plt.savefig('build/Rubidium.pdf')
plt.figure()
#Strontium
ths , ns = np.genfromtxt('daten/Strontium.dat', unpack=True)

plt.plot(ths,ns,".", label='Messdaten')
plt.xlabel(r'$\theta \:/\: °$')
plt.ylabel(r'$N \:/\: \frac{Imp}{s}$')
plt.legend(loc='best')
plt.tight_layout()
plt.savefig('build/Strontium.pdf')
plt.figure()
#Zink
thz , nz = np.genfromtxt('daten/Zink.dat', unpack=True)

plt.plot(thz,nz,".", label='Messdaten')
plt.xlabel(r'$\theta \:/\: °$')
plt.ylabel(r'$N \:/\: \frac{Imp}{s}$')
plt.legend(loc='best')
plt.tight_layout()
plt.savefig('build/Zink.pdf')
plt.figure()