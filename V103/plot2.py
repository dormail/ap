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

# funktion um die x achse zu skalieren
def skalierung(x):
    r = 0.005 # radius der staebe in meter
    m = 0.949 # masse des gewichtes in Kg
    
    F = m * 9.81 # Kraft durch die Masse m
    
    I = np.pi * r**4 / 4 # flaechentraegheistmoment
    L = 0.53 # hebelarm in metern
    return (L * x**2 - x**3 / 3)

# allgemeine Daten
r = 0.005 # radius der staebe in meter
m = 0.949 # masse des gewichtes in Kg

F = m * 9.81 # Kraft durch die Masse m

I = np.pi * r**4 / 4 # flaechentraegheistmoment

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


# curve fit
x_all = np.append(x1, x2)
D_all = np.append(D1, D2)
popt, pcov = opt.curve_fit(D, x_all, D_all)
E = popt[0]
print(f'E-Modul für Stab 1 nach Messung 2: \t {E:.4}')
error = np.sqrt(np.diag(pcov))
e = error[0]
print(f'Abweichung: \t{error[0]:.4}')

# messwerte
plt.scatter(skalierung(x1), D1, c='b', marker='+', 
    label='Messuhr 1')
plt.scatter(skalierung(x2), D2, c='g', marker='+',
        label='Messuhr 2')
#plt.title('Stab 1, einseitig eingespannt')
plt.title(rf'Messdaten und Fit zu Stab 1, einseitig eingespannt')


# plot der Theoriekurve
x = np.linspace(0,L)
plt.plot(skalierung(x), D(x,E), 'r', 
        label=rf'Theoriekurve für $E={{{E:.4}}}$')
        #label=rf'Theoriekurve für $E={{{E:.4}}} \, \frac{{N}}{{m^2}}$')
print(skalierung(x[-1]))
print(D(x[-1], E))
# plot der sigma umgebung
plt.fill_between(skalierung(x), D(x,E+e), D(x,E-e), 
        facecolor='red', alpha=0.5, label=rf'$\sigma$-Umgebung')

c = np.sqrt(E / dichte1)
print(f'Schallgeschwindigkeit in Stab 1:\t{c}')

plt.title(rf'Messdaten und Fit zu Stab 1, einseitig eingespannt')
plt.legend()
plt.xlabel(r'$(Lx^2 - x^3/3) / \si{\meter}$')
plt.ylabel(r'$1 / \si{m}$')

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
plt.close()

# messwerte
plt.scatter(skalierung(x1), D1, c='b', marker='+', 
    label='Messuhr 1')
plt.scatter(skalierung(x2), D2, c='g', marker='+',
        label='Messuhr 2')
#plt.title('Stab 1, einseitig eingespannt')
plt.title(rf'Messdaten und Fit zu Stab 2, einseitig eingespannt')


# plot der Theoriekurve
x = np.linspace(0,L)
plt.plot(skalierung(x), D(x,E), 'r', 
        label=rf'Theoriekurve für $E={{{E:.4}}}$')
        #label=rf'Theoriekurve für $E={{{E:.4}}} \, \frac{{N}}{{m^2}}$')
# plot der sigma umgebung
plt.fill_between(skalierung(x), D(x,E+e), D(x,E-e), 
        facecolor='red', alpha=0.5, label=rf'$\sigma$-Umgebung')

c = np.sqrt(E / dichte1)
print(f'Schallgeschwindigkeit in Stab 2:\t{c}')

plt.title(rf'Messdaten und Fit zu Stab 2, einseitig eingespannt')
plt.legend()
plt.xlabel(r'$(Lx^2 - x^3/3) / \si{\meter}$')
plt.ylabel(r'$1 / \si{m}$')

plt.savefig('build/plot3.pdf')
plt.close()
