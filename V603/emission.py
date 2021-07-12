# emission.py

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import polyfit
from uncertainties import unumpy as unp, ufloat

theta, N = np.genfromtxt('daten/EmissionCu.dat', unpack=True, comments='#')

# find peaks
from scipy.signal import find_peaks, peak_widths
peak_pos = find_peaks(N,
        width=3,
        prominence=900,
        distance=5)

peak_pos = peak_pos[0]

widths = peak_widths(N, peak_pos,
        rel_height=0.5)
widths = widths[0]

peaks = theta[peak_pos]

print(f'peak_pos: {peak_pos}')
print(f'Peaks: {peaks}')
print(f'Widths: {widths}')

# Plotting
# Scatter der non-peaks
# Filter der Werte nach peak/nonpeak
half_width_round = np.ceil(widths / 2)
index = np.ones_like(N)
index[peak_pos[0] - 0 : peak_pos[0] + 4] = 0
index[peak_pos[1] - 1 : peak_pos[1] + 3] = 0
N_nonpeak = N[index == 1]
theta_nonpeak = theta[index == 1]


plt.scatter(theta_nonpeak, N_nonpeak,
        marker='+',
        label='Messdaten - Bremsberg')

# scatter der peaks
plt.scatter(theta[index==0], 
        N[index==0],
        marker='+',
        label='Messdaten - Peak')

# Plot der Linien
plt.plot([theta[peak_pos[0]], theta[peak_pos[0]]], [100, np.max(N) + 100],
        c='r',
        ls='--',
        label=r'$K_\beta$',
        alpha=0.3)

plt.plot([theta[peak_pos[1]], theta[peak_pos[1]]], [100, np.max(N) + 100],
        c='g',
        ls='--',
        label=r'$K_\alpha$',
        alpha=0.3)

# visuals
plt.xlabel(r'$\theta$')
plt.ylabel(r'$N / (\text{Imp} / \text{s})$')
plt.yscale('log')
plt.legend()
plt.tight_layout()

plt.savefig('build/EmisionCu.pdf')
print('Figure saved in build/EmissionCu.pdf')

print(f'Theta_alpha = {theta[peak_pos[1]]}')
print(f'Theta_beta = {theta[peak_pos[0]]}')

# zeug 1zu1 von Nikola kopiert
# valores de la naturaleza
h = 6.62607015 * 10**(-34)
c = 299792458
d_LiF = 201.4
d_LiF *= 10**(-12)

# set k_alpha and k_beta line variables
kbeta = 20.2
kalpha = 22.5

kalpha_ = unp.uarray(kalpha, 0.25)
kbeta_ = unp.uarray(kbeta, 0.25)
# K_alpha y K_beta energias
lam_alpha = 2 * d_LiF * unp.sin(kalpha_ * np.pi / 180)
lam_beta = 2 * d_LiF * unp.sin(kbeta_ * np.pi / 180)

E_alpha = h * c / lam_alpha
E_beta = h * c / lam_beta

E_alpha *= 6.242 * 10**(18)
E_beta *= 6.242 * 10**(18)

print(f'E_a = {E_alpha}')
print(f'E_b = {E_beta}')

