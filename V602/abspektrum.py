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


E_K_z=9.60
E_K_ga=10.32
E_K_br=13.43
E_K_r=15.12
E_K_s=15.99
Z = np.array ([30,31,35,37,38])
E_K=np.array([E_K_z,E_K_ga,E_K_br,E_K_r,E_K_s])

params, covariance_matrix = np.polyfit(Z, np.sqrt(E_K), deg=1, cov=True)

x_plot = np.linspace(30, 40)
plt.plot(
    x_plot,
    params[0] * x_plot + params[1],
    ls='-', label='Ausgleichsgerade',  
)
plt.plot(Z, np.sqrt(E_K),".", label="Messdaten")
plt.legend(loc="best")
plt.ylabel(r'$\sqrt{E_K} \:/\: \sqrt{\si{\kilo\electronvolt}}$')
plt.xlabel(f"Ordnungszahl Z")
plt.tight_layout()
plt.savefig('build/mosely.pdf')
plt.close()
#rconst=(params[0]**2)*e/(h*c)

print(f"gerade={params[0]}x {params[1]}")
#ry_m=(params[0]**2)/h
#rconstabs=10973731.56816-((params[0]**2)*e/(h*c))
#rconstrel=(10973731.56816-(params[0]**2)*e/(h*c))/10973731.56816


#print(f"rydberg energie = {params[0]**2} rydberg const {rconst} ryconst abs{rconstabs} ryconst rel {rconstrel}")