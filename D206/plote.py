#e
import matplotlib.pyplot as plt
import numpy as np
import uncertainties.unumpy as unp
from scipy.optimize import curve_fit
from uncertainties import ufloat
t, T1, p1, T2, p2, N = np.genfromtxt('Daten.dat', unpack=True)
p1+=1
p2+=1
T2+=273.15
#plt.plot(T2,p2, 'o', label='T2-p2-Kurve')

   

params, covariance_matrix = np.polyfit(1/T2, np.log(p2), deg=1, cov=True)

errors = np.sqrt(np.diag(covariance_matrix))

print('a = {:.3f} ± {:.4f}'.format(params[0], errors[0]))
print('b = {:.3f} ± {:.4f}'.format(params[1], errors[1]))

def gerade (x, m, b):
    return m*x+b

z = np.linspace(np.min(1/T2), np.max(1/T2))

plt.plot(1/T2, np.log(p2), 'rx', label='T2-p2-Messdaten')
plt.plot(z, gerade (z, *params), 'b-', label='Ausgleichsgerade')
plt.xlabel(r'$1/T_2 \:[K]$')
plt.ylabel(r'$ln(p_2[bar])$')
plt.legend(loc='best')

plt.tight_layout()
plt.savefig('build/plot2.pdf')
