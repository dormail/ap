import matplotlib.pyplot as plt
import numpy as np
import uncertainties as unc
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.optimize import curve_fit
import scipy.constants as const
import sympy

t,p,t2=np.genfromtxt('daten/bis1bar.txt', unpack=True)

t+=273 #Kelvin
t2+=273
p/=1e3

params, _fehler = np.polyfit(1/t2,np.log(p), deg=1, cov=True)
L1=-1*params[0]*const.gas_constant
fehler = np.sqrt(np.diag(_fehler))
print("\nParams=",params)
print("fehler=", fehler)
print(f"L1={L1:.8f} \n")

uparams=unp.uarray(params,fehler)
uL1=-1*uparams[0]*const.gas_constant
La=const.gas_constant * 373
uLa=unc.ufloat(La,0)
uLi=uL1-uLa
uLimol=uLi/(const.Avogadro*const.elementary_charge)
print(f'\n \n L1= {uL1:.4f} J/mol \n La={uLa:.4f} J/mol \n Li= {uLi:.4f} J/mol\n Li pro Molekül in eV: {uLimol:.4f} eV\n')

x=np.linspace(1/t2[-1],1/t2[0],1000)
plt.figure()
plt.plot(x, params[0]*x + params[1], label='Ausgleichsgerade')
plt.plot(1/t2,np.log(p),'.', label='Messwerte')
plt.xlabel(r'$\frac{1}{T} \:/\: \frac{1}{\si{\kelvin}}$')
plt.ylabel(r'$ln(\frac{p}{p_0}) $')
plt.legend(loc='best')

# in matplotlibrc leider (noch) nicht möglich
plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/plot1.pdf')
################################

P,T=np.genfromtxt('daten/bis15bar.txt', unpack=True)

T+=273
params2, _f = np.polyfit(T,P, deg=3, cov=True)
err = np.sqrt(np.diag(_f))
uparam=unp.uarray(params2,err)
print('\n\n15 bar')
print("\nPolynomwerte /T^3, /T^2, /T und :\n", uparam,'\n')


plt.figure()
plt.plot(T,P,'.',label="Messwerte")
plt.plot(T, params2[0]*T**3 + params2[1]*T**2+params2[2]*T+params2[3], label="Ausgleichskurve")
plt.xlabel("T [K]")
plt.ylabel("p [bar]")
plt.tight_layout()
plt.legend()
plt.savefig('build/plot2.pdf')



R=const.gas_constant
C=0.9
def L(x,a,b,c,d):
    return (((R*x/2)+np.sqrt((R*x/2)**2-0.9*(a*x**3 + b*x**2+c*x+d)))*((3*a*x**3+2*b*x**2+c*x)/(a*x**3+b*x**2+c*x+d)))

x= np.linspace(T[-1],T[0],1000)


plt.figure()
plt.plot(x, L(x, *params2), label='Genäherte Funktion für L')
plt.xlabel("T [K]")
plt.ylabel("L [J/mol]")
plt.savefig('build/plot3.pdf')