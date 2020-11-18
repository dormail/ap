import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy
import scipy.optimize as opt

### bestimmung der Dichten ###
# alles in SI einheiten
m1 = 0.394 
m2 = 0.3811
l1 = 0.601
l2 = 0.5515
r = 0.005

# volumen der Staebe
V1 = l1 * r**2 * np.pi
V2 = l2 * r**2 * np.pi

# Dichte der Staebe
dichte1 = m1 / V1
dichte2 = m2 / V2

print(f'Dicht von Stab 1:\t{dichte1} kg/m^3')
print(f'Dicht von Stab 2:\t{dichte2} kg/m^3')


### die funktion was die auslenkung definiert ###
def D(x, E):
    r = 0.005 # radius der staebe in meter
    m = 0.949 # masse des gewichtes in Kg
    
    F = m * 9.81 # Kraft durch die Masse m
    
    I = np.pi * r**4 / 4 # flaechentraegheistmoment
    L = 0.53 # hebelarm in metern
    return F / (2 * E * I) * (L * x**2 - x**3 / 3)

# allgemeine Daten
r = 0.005 # radius der staebe in meter
m = 0.949 # masse des gewichtes in Kg

F = m * 9.81 # Kraft durch die Masse m

I = np.pi * r**4 / 4 # flaechentraegheistmoment

# messung 1
# stab der an beiden enden aufliegt
L = 28.5 # aufhaengepunkt in cm

df1 = pd.read_csv('daten/daten1_1.csv')
df2 = pd.read_csv('daten/daten1_2.csv')
x1 = df1['stellung der messuhr in cm']
x2 = df2['stellung der messuhr in cm']

D1 = df1['biegung in micrometer']
D2 = df2['biegung in micrometer']

lx1 = np.abs(x1 - L)
lx2 = np.abs(x2 - L)

plt.scatter(lx1, D1, c='b', marker='+')
plt.scatter(lx2, D2, c='g', marker='+')
plt.savefig('build/plot1.pdf')

plt.close()

# messung 2
# stab1 mit einem freien ende
L = 0.53 # aufhaengepunkt in m
df1 = pd.read_csv('daten/daten2_1.csv')
df2 = pd.read_csv('daten/daten2_2.csv')
x1 = df1['stellung der messuhr in cm'] * 0.01
x2 = df2['stellung der messuhr in cm'] * 0.01

D1 = df1['biegung in micrometer'] / 1000000 # nun in metern
D2 = df2['biegung in micrometer'] / 1000000 # nun in metern

lx1 = np.abs(L - x1)
lx2 = np.abs(L - x2)

plt.scatter(x1, D1, c='b', marker='+', 
    label='Messuhr 1')
plt.scatter(x2, D2, c='g', marker='+',
        label='Messuhr 2')
plt.title('Stab 1, einseitig eingespannt')

# curve fit
x_all = np.append(x1, x2)
D_all = np.append(D1, D2)
popt, pcov = opt.curve_fit(D, x_all, D_all)
E = popt[0]
print(f'Elastizitätsmodul für Stab 1: \t {E}')

# plot der Theoriekurve
x = np.linspace(0,L)
plt.plot(x, D(x,E), 'r', 
        label=rf'Theoriekurve für $E={{{E:.4}}}$')
        #label=rf'Theoriekurve für $E={{{E:.4}}} \, \frac{{N}}{{m^2}}$')

plt.xlabel(r'$\frac{x}{cm}$')
plt.legend()

plt.savefig('build/plot2.pdf')
plt.close()

# messung 3
# stab2 mit einem freien ende
L = 53 # aufhaengepunkt in cm
df1 = pd.read_csv('daten/daten3_1.csv')
df2 = pd.read_csv('daten/daten3_2.csv')
x1 = df1['stellung der messuhr in cm']
x2 = df2['stellung der messuhr in cm']

D1 = df1['biegung in micrometer']
D2 = df2['biegung in micrometer']

lx1 = np.abs(L - x1)
lx2 = np.abs(L - x2)

plt.scatter(x1, D1, c='b', marker='+', 
    label='Messuhr 1')
plt.scatter(x2, D2, c='g', marker='+',
        label='Messuhr 2')
plt.title('Stab 2, einseitig eingespannt')
plt.xlabel(r'$\frac{x}{cm}$')
plt.legend()

plt.savefig('build/plot3.pdf')
plt.close()
# 
# # messung 3
# # stab2 mit einem freien ende
# d3 = df3['stellung der messuhr in cm']
# x3 = df3['biegung in micrometer']
# 
# plt.scatter(d3,x3, c='k', marker='+')
# plt.savefig('build/plot3.pdf')
# 
# 
# #plt.show()
# 
# # in matplotlibrc leider (noch) nicht möglich
# # plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
