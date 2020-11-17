import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# df2 = pd.read_csv('daten2.csv')
# df3 = pd.read_csv('daten3.csv')

# print(df1.head())

# messung 1
# stab der an beiden enden aufliegt
L = 28.5 # aufhaengepunkt in cm

df1 = pd.read_csv('daten1_1.csv')
df2 = pd.read_csv('daten1_2.csv')
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
L = 53 # aufhaengepunkt in cm
df1 = pd.read_csv('daten2_1.csv')
df2 = pd.read_csv('daten2_2.csv')
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
plt.title('Stab 1, einseitig eingespannt')
plt.xlabel(r'$\frac{x}{cm}$')
plt.legend()

plt.savefig('build/plot2.pdf')
plt.close()

# messung 3
# stab2 mit einem freien ende
L = 53 # aufhaengepunkt in cm
df1 = pd.read_csv('daten3_1.csv')
df2 = pd.read_csv('daten3_2.csv')
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
