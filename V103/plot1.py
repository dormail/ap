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
# rueckgabe in milimetern
def DBeidseitigRechts(x, E):
    r = 0.005 # radius der staebe in meter
    m = 0.949 # masse des gewichtes in Kg
    
    F = m * 9.81 # Kraft durch die Masse m
    
    I = np.pi * r**4 / 4 # flaechentraegheistmoment
    L = 0.53 # hebelarm in metern
    # return F / (48 * E * I) * (4 * x**3 - 12 * L * x**2 + 9 * L**2 * x - L**3)
    return F / (48 * E * I) * (3 * L**2 * x - 4 * x**3) * 1000

def DBeidseitigLinks(x,E):
    r = 0.005 # radius der staebe in meter
    m = 0.949 # masse des gewichtes in Kg
    
    F = m * 9.81 # Kraft durch die Masse m
    
    I = np.pi * r**4 / 4 # flaechentraegheistmoment
    L = 0.53 # hebelarm in metern
    return F / (48 * E * I) * (4 * x**3 - 12 * L * x**2 + 9 * L**2 * x - L**3) * 1000


# allgemeine Daten
r = 0.005 # radius der staebe in meter
m = 0.949 # masse des gewichtes in Kg

F = m * 9.81 # Kraft durch die Masse m

I = np.pi * r**4 / 4 # flaechentraegheistmoment

### messung 1 ###
# stab der an beiden enden aufliegt
L = 0.285 # mitte in cm

### data import ###
df1 = pd.read_csv('daten/daten1_1.csv')
df2 = pd.read_csv('daten/daten1_2.csv')
x1 = df1['stellung der messuhr in cm'] * 0.01
x2 = df2['stellung der messuhr in cm'] * 0.01
D1 = df1['biegung in micrometer'] / 1000000 # nun in metern
D2 = df2['biegung in micrometer'] / 1000000 # nun in metern

### data cleaning ###
# fuer den fit muss eine seite auf die andere gebracht werden
pos_right = np.append(x1[x1 < 0.285], x2[x2 < .285])
pos_left = np.append(x1[x1 > 0.285], x2[x2 > .285])
data_right = np.append(D1[x1 < 0.285], D2[x2 < .285])
data_left = np.append(D1[x1 > 0.285], D2[x2 > .285])

fitting_data = np.append(data_left, data_right)
pos_mirrored = (.285 - (pos_left - .285))
fitting_x = np.append(pos_mirrored, pos_right)

print(fitting_x)
print(fitting_data)

# curve-fit 
popt, pcov = opt.curve_fit(DBeidseitigRechts, fitting_x, fitting_data)
error = np.sqrt(np.diag(pcov))
E = popt[0]
e = error[0]

print(f'E-Modul fuer Stab 1 nach Messung 1:\t{E:.4}')
print(f'Abweichung: \t{error[0]:.4}')



### plot der Theoriekurve ###
# linke haelfte
x = np.linspace(0,0.285)
plt.plot(DBeidseitigRechts(x,E), DBeidseitigRechts(x,E), 'r',
        label=rf'Theoriekurve für $E=({{{E:.5}}})$Pa')
plt.fill_between(DBeidseitigRechts(x, E), DBeidseitigRechts(x,E+e), DBeidseitigRechts(x,E-e), 
        facecolor='red', alpha=0.3, label=rf'$\sigma$-Umgebung')
## rechte haelfte
#plt.fill_between(D_mit_left(x, E), 1000* D_mit_left(x,E+e), 1000* D_mit_left(x,E-e), 
#        facecolor='red', alpha=0.3)
#
# datenpunkte
plt.scatter(DBeidseitigRechts(x1, E), D1, c='b', marker='+', label='Messuhr 1')
#plt.scatter(x2, D2, c='g', marker='+', label='Messuhr 2')
#plt.scatter(D_mit_left(0.64, E),130 / 1000000, c='r', marker='+', label='Fehlerhafte Messung')

# visuals
plt.xlabel(r'$D(x) / \si{m}$')
plt.ylabel(r'$1 / \si{mm}$')
plt.title(rf'Messdaten und Fit zu Stab 1, beidseitig eingespannt')
plt.legend()

plt.savefig('build/plot1.pdf')

plt.close()
