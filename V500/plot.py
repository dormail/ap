import matplotlib.pyplot as plt
import numpy as np
import uncertainties as unc
import uncertainties.unumpy as unp
from uncertainties import ufloat
from scipy.optimize import curve_fit
import scipy.constants as const

U_gl , I_gl = np.genfromtxt('daten/gelb.txt', unpack=True)
U_gl*=-1
#I_gl *=1e-9

print(U_gl)
print(I_gl)

pa_gl , cov_gl = np.polyfit(U_gl[2:8],np.sqrt(I_gl[2:8]), deg =1, cov = True)
errors_gl = np.sqrt(np.diag(cov_gl))
a_gl = ufloat(pa_gl[0], errors_gl[0])
print("a_gl", a_gl)
b_gl = ufloat(pa_gl[1], errors_gl[1])
print("b_gl", b_gl)
Ug_gl = (-b_gl/a_gl)
print("gelbeNullstelle", Ug_gl)
#print(pa_gl,errors_gl)
x=np.linspace(-5,Ug_gl.nominal_value)
plt.plot(x,x*pa_gl[0]+pa_gl[1], label='Ausgleichsgerade')
plt.plot(U_gl,np.sqrt(I_gl),".", label='Messdaten')
plt.xlabel(r'$U \:/\: \si{\volt}$')
plt.ylabel(r'$\sqrt{I} \:/\: \sqrt{\si{\nano\ampere}}$')
plt.legend(loc='best')
plt.savefig('build/gelb.pdf')


U_gr , I_gr = np.genfromtxt('daten/gruen.txt', unpack=True)
#I_gr *=1e-9
U_gr*=-1
pa_gr , cov_gr = np.polyfit(U_gr[0:6],np.sqrt(I_gr[0:6]), deg =1, cov = True)
errors_gr = np.sqrt(np.diag(cov_gr))
a_gr = ufloat(pa_gr[0], errors_gr[0])
print("a_gr", a_gr)
b_gr = ufloat(pa_gr[1], errors_gr[1])
print("b_gr", b_gr)
Ug_gr = (-b_gr/a_gr)
print("grueneNullstelle", Ug_gr)
#print(pa_gl,errors_gl)
plt.figure()
x=np.linspace(-5,Ug_gr.nominal_value)
plt.plot(x,x*pa_gr[0]+pa_gr[1], label='Ausgleichsgerade')
plt.plot(U_gr,np.sqrt(I_gr),".", label='Messdaten')
plt.xlabel(r'$U \:/\: \si{\volt}$')
plt.ylabel(r'$\sqrt{I} \:/\: \sqrt{\si{\nano\ampere}}$')
plt.legend(loc='best')
plt.savefig('build/gruen.pdf')

U_v1 , I_v1 = np.genfromtxt('daten/violett1.txt', unpack=True)
U_v1*=-1
#I_gr *=1e-9
pa_v1 , cov_v1 = np.polyfit(U_v1[1:8],np.sqrt(I_v1[1:8]), deg =1, cov = True)
errors_v1 = np.sqrt(np.diag(cov_v1))
a_v1 = ufloat(pa_v1[0], errors_v1[0])
print("a_v1", a_v1)
b_v1 = ufloat(pa_v1[1], errors_v1[1])
print("b_v1", b_v1)
Ug_v1 = (-b_v1/a_v1)
print("v1Nullstelle", Ug_v1)
#print(pa_gl,errors_gl)
plt.figure()
x=np.linspace(-5,Ug_v1.nominal_value)
plt.plot(x,x*pa_v1[0]+pa_v1[1], label='Ausgleichsgerade')
plt.plot(U_v1,np.sqrt(I_v1),".", label='Messdaten')
plt.xlabel(r'$U \:/\: \si{\volt}$')
plt.ylabel(r'$\sqrt{I} \:/\: \sqrt{\si{\nano\ampere}}$')
plt.legend(loc='best')
plt.savefig('build/v1.pdf')

U_v2 , I_v2 = np.genfromtxt('daten/violett2.txt', unpack=True)
U_v2*=-1
#I_gr *=1e-9
pa_v2 , cov_v2 = np.polyfit(U_v2[0:6],np.sqrt(I_v2[0:6]), deg =1, cov = True)
errors_v2 = np.sqrt(np.diag(cov_v2))
a_v2 = ufloat(pa_v2[0], errors_v2[0])
print("a_v2", a_v2)
b_v2 = ufloat(pa_v2[1], errors_v2[1])
print("b_v2", b_v2)
Ug_v2 = (-b_v2/a_v2)
print("v2Nullstelle", Ug_v2)
#print(pa_gl,errors_gl)
plt.figure()
x=np.linspace(-5,Ug_v2.nominal_value)
plt.plot(x,x*pa_v2[0]+pa_v2[1], label='Ausgleichsgerade')
plt.plot(U_v2,np.sqrt(I_v2),".", label='Messdaten')
plt.xlabel(r'$U \:/\: \si{\volt}$')
plt.ylabel(r'$\sqrt{I} \:/\: \sqrt{\si{\nano\ampere}}$')
plt.legend(loc='best')
plt.savefig('build/v2.pdf')
#b)
Ug = np.array([Ug_gl.n,Ug_gr.n,Ug_v1.n,Ug_v2.n])
lam = np.array([578e-9,546e-9,435e-9,405e-9])

e = 1.602176634e-19 
c = 299792458
f=c/lam
pa_Ug , cov_Ug = np.polyfit( f ,Ug ,deg =1, cov = True)
errors_Ug = np.sqrt(np.diag(cov_Ug))
a = ufloat(pa_Ug[0], errors_Ug[0])#=h/e
Ak = ufloat(pa_Ug[1], errors_Ug[1])
print("a=", a)
print("Ak=", Ak)
plt.figure()
x=np.linspace(0,800000000000000)
plt.plot(x,x*pa_Ug[0]+pa_Ug[1], label='Ausgleichsgerade')
plt.plot(f,Ug,".", label='Daten')
plt.ylabel(r'$U_g \:/\: \si{\volt}$')
plt.xlabel(r'$\nu \:/\: \si{\hertz}$')
plt.legend(loc='best')
plt.savefig('build/ug.pdf')
#c
plt.figure()
plt.plot(U_gl,I_gl,".", label='Messdaten zur gelben Spektrallinie')
plt.xlabel(r'$U \:/\: \si{\volt}$')
plt.ylabel(r'$I \:/\: \si{\nano\ampere}$')
plt.legend(loc='best')
plt.savefig('build/UI.pdf')