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


### die funktionen für theoriekurven ###
# einseitig
def D(x, E):
    r = 0.005 # radius der staebe in meter
    m = 0.949 # masse des gewichtes in Kg
    
    F = m * 9.81 # Kraft durch die Masse m
    
    I = np.pi * r**4 / 4 # flaechentraegheistmoment
    L = 0.53 # hebelarm in metern
    return F / (2 * E * I) * (L * x**2 - x**3 / 3)

# beidseitig
def D_mit(x, E):
    r = 0.005 # radius der staebe in meter
    m = 0.949 # masse des gewichtes in Kg
    
    F = m * 9.81 # Kraft durch die Masse m
    
    I = np.pi * r**4 / 4 # flaechentraegheistmoment
    L = 0.53 # hebelarm in metern
    # return F / (48 * E * I) * (4 * x**3 - 12 * L * x**2 + 9 * L**2 * x - L**3)
    return F / (48 * E * I) * (3 * L**2 * x - 4 * x**3)

def D_mit_left(x,E):
    r = 0.005 # radius der staebe in meter
    m = 0.949 # masse des gewichtes in Kg
    
    F = m * 9.81 # Kraft durch die Masse m
    
    I = np.pi * r**4 / 4 # flaechentraegheistmoment
    L = 0.53 # hebelarm in metern
    return F / (48 * E * I) * (4 * x**3 - 12 * L * x**2 + 9 * L**2 * x - L**3)


# allgemeine Daten
r = 0.005 # radius der staebe in meter
m = 0.949 # masse des gewichtes in Kg

F = m * 9.81 # Kraft durch die Masse m

I = np.pi * r**4 / 4 # flaechentraegheistmoment

# messung 1
# stab der an beiden enden aufliegt
L = 0.285 # mitte in cm

df1 = pd.read_csv('daten/daten1_1.csv')
df2 = pd.read_csv('daten/daten1_2.csv')
x1 = df1['stellung der messuhr in cm'] * 0.01
x2 = df2['stellung der messuhr in cm'] * 0.01

x1_messung1 = x1
x2_messung1 = x2

D1 = df1['biegung in micrometer'] / 1000000 # nun in metern
D2 = df2['biegung in micrometer'] / 1000000 # nun in metern

D1_messung1 = D1
D2_messung1 = D2

# fuer den fit muss eine seite auf die andere gebracht werden
pos_right = np.append(x1[x1 < 0.285], x2[x2 < .285])
pos_left = np.append(x1[x1 > 0.285], x2[x2 > .285])
data_right = np.append(D1[x1 < 0.285], D2[x2 < .285])
data_left = np.append(D1[x1 > 0.285], D2[x2 > .285])

print(len(pos_right))
print(len(pos_left))
print(len(data_right))
print(len(data_left))

fitting_data = np.append(data_left, data_right)
pos_mirrored = (.285 - (pos_left - .285))
#print(pos_right_to_left)
fitting_x = np.append(pos_mirrored, pos_right)
#fitting_x = pos_left
#fitting_data = data_left

print(fitting_x)
print(fitting_data)

# plt.close()
# plt.scatter(fitting_x, fitting_data, c='r')
#plt.scatter(pos_mirrored, fitting_data, c='b')
popt, pcov = opt.curve_fit(D_mit, fitting_x, fitting_data)
E = popt[0]

print(f'E-Modul fuer Stab 1 nach Messung 1:\t{E:.4}')
error = np.sqrt(np.diag(pcov))
e = error[0]
print(f'Abweichung: \t{error[0]:.4}')



# plot der Theoriekurve
# linke haelfte
x = np.linspace(0,0.285)
plt.plot(x, D_mit(x,E), 'r',
        label=rf'Theoriekurve für $E=({{{E:.4}}})$Pa')
plt.fill_between(x, D_mit(x,E+e), D_mit(x,E-e), 
        facecolor='red', alpha=0.5, label=rf'$\sigma$-Umgebung')
# rechte haelfte
x = np.linspace(.285,0.57)
plt.plot(x, D_mit_left(x,E), 'r')
plt.fill_between(x, D_mit_left(x,E+e), D_mit_left(x,E-e), 
        facecolor='red', alpha=0.5)

# lx1 = np.abs(x1 - L)
# lx2 = np.abs(x2 - L)

plt.scatter(x1, D1, c='b', marker='+', label='Messuhr 1')
plt.scatter(x2, D2, c='g', marker='+', label='Messuhr 2')
plt.scatter(0.64,130 / 1000000, c='r', marker='+', label='Fehlerhafte Messung')

plt.xlabel(r'$x / \si{m}$')
plt.ylabel(r'$D(x) / \si{m}$')
plt.title(rf'Messdaten und Fit zu Stab 1, beidseitig eingespannt')
plt.legend()

plt.savefig('build/plot1.pdf')

plt.close()

# messung 2
# stab1 mit einem freien ende
L = 0.53 # aufhaengepunkt in m
df1 = pd.read_csv('daten/daten2_1.csv')
df2 = pd.read_csv('daten/daten2_2.csv')
x1 = df1['stellung der messuhr in cm'] * 0.01
x2 = df2['stellung der messuhr in cm'] * 0.01
x1_messung2 = x1
x2_messung2 = x2

D1 = df1['biegung in micrometer'] / 1000000 # nun in metern
D2 = df2['biegung in micrometer'] / 1000000 # nun in metern
D1_messung2 = D1
D2_messung2 = D2

lx1 = np.abs(L - x1)
lx2 = np.abs(L - x2)

plt.scatter(x1, D1, c='b', marker='+', 
    label='Messuhr 1')
plt.scatter(x2, D2, c='g', marker='+',
        label='Messuhr 2')
#plt.title('Stab 1, einseitig eingespannt')
plt.title(rf'Messdaten und Fit zu Stab 1, einseitig eingespannt')

# curve fit
x_all = np.append(x1, x2)
D_all = np.append(D1, D2)
popt, pcov = opt.curve_fit(D, x_all, D_all)
E = popt[0]
print(f'E-Modul für Stab 1 nach Messung 2: \t {E:.4}')
error = np.sqrt(np.diag(pcov))
e = error[0]
print(f'Abweichung: \t{error[0]:.4}')

# plot der Theoriekurve
x = np.linspace(0,L)
plt.plot(x, D(x,E), 'r', 
        label=rf'Theoriekurve für $E={{{E:.4}}}$')
        #label=rf'Theoriekurve für $E={{{E:.4}}} \, \frac{{N}}{{m^2}}$')
# plot der sigma umgebung
plt.fill_between(x, D(x,E+e), D(x,E-e), 
        facecolor='red', alpha=0.5, label=rf'$\sigma$-Umgebung')

c = np.sqrt(E / dichte1)
print(f'Schallgeschwindigkeit in Stab 1:\t{c}')

#plt.xlabel(r'$\frac{x}{cm}$')
plt.legend()
plt.xlabel(r'$x / \si{m}$')
plt.ylabel(r'$D(x) / \si{m}$')

plt.savefig('build/plot2.pdf')
plt.close()

# messung 3
# stab2 mit einem freien ende
L = 0.53 # aufhaengepunkt in cm
df1 = pd.read_csv('daten/daten3_1.csv')
df2 = pd.read_csv('daten/daten3_2.csv')
x1 = df1['stellung der messuhr in cm'] * 0.01
x2 = df2['stellung der messuhr in cm'] * 0.01
x1_messung3 = x1
x2_messung3 = x2

D1 = df1['biegung in micrometer'] / 1000000
D2 = df2['biegung in micrometer'] / 1000000
D1_messung3 = D1
D2_messung3 = D2

lx1 = np.abs(L - x1)
lx2 = np.abs(L - x2)

plt.scatter(x1, D1, c='b', marker='+', 
    label='Messuhr 1')
plt.scatter(x2, D2, c='g', marker='+',
        label='Messuhr 2')

# curve fit
x_all = np.append(x1, x2)
D_all = np.append(D1, D2)
popt, pcov = opt.curve_fit(D, x_all, D_all)
E = popt[0]
print(f'Elastizitätsmodul für Stab 2: \t {E:.4}')
error = np.sqrt(np.diag(pcov))
print(f'Abweichung: \t{error[0]:.4}')

# plot der Theoriekurve
x = np.linspace(0,L)
plt.plot(x, D(x,E), 'r', 
        label=rf'Theoriekurve für $E={{{E:.4}}}$Pa')

# plot der sigma umgebung
e = error[0]
plt.fill_between(x, D(x,E+e), D(x,E-e), 
        facecolor='red', alpha=0.5, label=rf'$\sigma$-Umgebung')

c = np.sqrt(E / dichte2)
print(f'Schallgeschwindigkeit in Stab 2:\t{c}')

plt.xlabel(r'$\frac{x}{cm}$')
plt.legend()
#plt.title('Stab 2, einseitig eingespannt')
plt.title(rf'Messdaten und Fit zu Stab 2, einseitig eingespannt')
plt.xlabel(r'$x / \si{m}$')
plt.ylabel(r'$D(x) / \si{m}$')

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
