import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df1 = pd.read_csv('daten1.csv')
df2 = pd.read_csv('daten2.csv')
df3 = pd.read_csv('daten3.csv')

print(df1.head())

# messung 1
# stab der an beiden enden aufliegt
d1 = df1['stellung der messuhr in cm']
x1 = df1['biegung in micrometer']

plt.scatter(d1,x1, c='k', marker='+')
plt.savefig('build/plot1.pdf')

plt.close()

# messung 2
# stab1 mit einem freien ende
d2 = df2['stellung der messuhr in cm']
x2 = df2['biegung in micrometer']

plt.scatter(d2,x2, c='k', marker='+')
plt.savefig('build/plot2.pdf')
plt.close()

# messung 3
# stab2 mit einem freien ende
d3 = df3['stellung der messuhr in cm']
x3 = df3['biegung in micrometer']

plt.scatter(d3,x3, c='k', marker='+')
plt.savefig('build/plot3.pdf')


#plt.show()

# in matplotlibrc leider (noch) nicht möglich
# plt.tight_layout(pad=0, h_pad=1.08, w_pad=1.08)
