import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy
import scipy.optimize as opt


### data import ###
d1 = pd.read_csv('daten/WienRobinson.csv')
f = d1['f'] 
U_Br = d1['2U_Br']/2

plt.plot(f, U_Br, label='Kurve')
plt.xlabel(r'$f \:/\: \si{\hertz}$')
plt.ylabel(r'$U_{Br} \:/\: \si{\volt}$')
plt.legend(loc='best')

#plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
plt.savefig('build/WRplot.pdf')
