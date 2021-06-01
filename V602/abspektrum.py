import matplotlib.pyplot as plt
import numpy as np
import uncertainties as unc
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.optimize import curve_fit
import scipy.constants as const





#Brom
thb , nb = np.genfromtxt('daten/Brom.dat', unpack=True)
br1=13 
br2=13.5
sig_br_lit= 3.848
Z_br= 35
br_middle = (br1 + br2)/2

plt.figure()
plt.axvline(br_middle, linestyle='-', color='red', label='Mitte der Absorptionskante')    
plt.axvspan(br1, br2, alpha=0.2,label='Absorptionskante')
plt.grid()
plt.plot(thb,nb,".", label='Messdaten')
plt.xlabel(r'$\theta \:/\: \si{°}$')
plt.ylabel(r'$N \:/\: \si{\frac{Imp}{s}}$')
plt.legend(loc='best')
plt.tight_layout()
plt.savefig('build/Brom.pdf')
plt.figure()
#gallium
thga , nga = np.genfromtxt('daten/Gallium.dat', unpack=True)
g1=17.1 
g2=17.6
sig_g_lit= 3.677
Z_g= 31
g_middle = (g1 + g2)/2

plt.figure()
plt.axvline(g_middle, linestyle='-', color='red', label='Mitte der Absorptionskante')    
plt.axvspan(g1, g2, alpha=0.2,label='Absorptionskante')
plt.grid()
plt.plot(thga,nga,".", label='Messdaten')
plt.xlabel(r'$\theta \:/\: \si{°}$')
plt.ylabel(r'$N \:/\: \si{\frac{Imp}{s}}$')
plt.legend(loc='best')
plt.tight_layout()
plt.savefig('build/Gallium.pdf')
plt.figure()
#Rubidium
thr , nr = np.genfromtxt('daten/Rubidium.dat', unpack=True)
r1=11.4 
r2=12.1
sig_r_lit= 3.944
Z_r= 37
r_middle = (r1 + r2)/2

plt.figure()
plt.axvline(r_middle, linestyle='-', color='red', label='Mitte der Absorptionskante')    
plt.axvspan(r1, r2, alpha=0.2,label='Absorptionskante')
plt.grid()
plt.plot(thr,nr,".", label='Messdaten')
plt.xlabel(r'$\theta \:/\: \si{°}$')
plt.ylabel(r'$N \:/\: \si{\frac{Imp}{s}}$')
plt.legend(loc='best')
plt.tight_layout()
plt.savefig('build/Rubidium.pdf')
plt.figure()
#Strontium
ths , ns = np.genfromtxt('daten/Strontium.dat', unpack=True)
s1=10.8
s2=11.4
sig_s_lit= 3.999
Z_s= 38
s_middle = (s1 + s2)/2

plt.figure()
plt.axvline(s_middle, linestyle='-', color='red', label='Mitte der Absorptionskante')    
plt.axvspan(s1, s2, alpha=0.2,label='Absorptionskante')
plt.grid()
plt.plot(ths,ns,".", label='Messdaten')
plt.xlabel(r'$\theta \:/\: \si{°}$')
plt.ylabel(r'$N \:/\: \si{\frac{Imp}{s}}$')
plt.legend(loc='best')
plt.tight_layout()
plt.savefig('build/Strontium.pdf')
plt.figure()
#Zink
thz , nz = np.genfromtxt('daten/Zink.dat', unpack=True)
z1=18.5 
z2=18.9
sig_z_lit=3.566
Z_z=30
z_middle = (z1 + z2)/2

plt.figure()
plt.axvline(z_middle, linestyle='-', color='red', label='Mitte der Absorptionskante')    
plt.axvspan(z1, z2, alpha=0.2,label='Absorptionskante')
plt.grid()
plt.plot(thz,nz,".", label='Messdaten')
plt.xlabel(r'$\theta \:/\: \si{°}$')
plt.ylabel(r'$N \:/\: \si{\frac{Imp}{s}}$')
plt.legend(loc='best')
plt.tight_layout()
plt.savefig('build/Zink.pdf')
plt.figure()
