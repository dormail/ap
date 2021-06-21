# 5.py

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

conv = 2 * np.pi / 360 # conversion deg->rad

# 100 Linien/mm
d = 10 * 10**(-6) # gitterkonstante in SI

gruen1 = [3, 6, 9.1, 12.2, 15.5, 18.8, 22]
gruen2 = [3.2, 6.2, 9.5, 12.6, 16, 19.2, 22.8]
kgruen = np.arange(1, 8)

rot1 = [3.8, 7.2, 11.1, 15]
rot2 = [3.8, 7.5, 11.1, 15]
krot = np.arange(1, 5)

rot = np.add(rot1, rot2)
rot = np.divide(rot, 2)
gruen = np.add(gruen1, gruen2)
gruen = np.divide(gruen, 2)
rot = rot * conv
gruen = gruen * conv

lambda_rot = d * np.divide(np.sin(rot), krot)
lambda_gruen = d * np.divide(np.sin(gruen), kgruen)

lambda_rot_std = np.std(lambda_rot)
lambda_gruen_std = np.std(lambda_gruen)
lambda_rot = np.mean(lambda_rot)
lambda_gruen = np.mean(lambda_gruen)

print(f'100 Linien/mm')
print(f'lambda_rot = {lambda_rot} \pm {lambda_rot_std}')
print(f'lambda_gruen = {lambda_gruen} \pm {lambda_gruen_std}')

# 300 Linien/mm
d = 3.3 * 10**(-6) # gitterkonstante in SI

gruen1 = [9, 18.2]
gruen2 = [9.3, 19]
kgruen = np.arange(1, 3)

rot1 = [11, 22.2]
rot2 = [11, 22.8]
krot = np.arange(1, 3)

rot = np.add(rot1, rot2)
rot = np.divide(rot, 2)
gruen = np.add(gruen1, gruen2)
gruen = np.divide(gruen, 2)
rot = rot * conv
gruen = gruen * conv

lambda_rot = d * np.divide(np.sin(rot), krot)
lambda_gruen = d * np.divide(np.sin(gruen), kgruen)

lambda_rot_std = np.std(lambda_rot)
lambda_gruen_std = np.std(lambda_gruen)
lambda_rot = np.mean(lambda_rot)
lambda_gruen = np.mean(lambda_gruen)

print(f'300 Linien/mm')
print(f'lambda_rot = {lambda_rot} \pm {lambda_rot_std}')
print(f'lambda_gruen = {lambda_gruen} \pm {lambda_gruen_std}')

# 600 Linien/mm
d = 1.67 * 10**(-6) # gitterkonstante in SI

gruen1 = [18.8]
gruen2 = [19.5]
kgruen = np.arange(1, 2)

rot1 = [23.5]
rot2 = [22.8]
krot = np.arange(1, 2)

rot = np.add(rot1, rot2)
rot = np.divide(rot, 2)
gruen = np.add(gruen1, gruen2)
gruen = np.divide(gruen, 2)
rot = rot * conv
gruen = gruen * conv

lambda_rot = d * np.divide(np.sin(rot), krot)
lambda_gruen = d * np.divide(np.sin(gruen), kgruen)

lambda_rot_std = np.std(lambda_rot)
lambda_gruen_std = np.std(lambda_gruen)
lambda_rot = np.mean(lambda_rot)
lambda_gruen = np.mean(lambda_gruen)

print(f'600 Linien/mm')
print(f'lambda_rot = {lambda_rot} \pm {lambda_rot_std}')
print(f'lambda_gruen = {lambda_gruen} \pm {lambda_gruen_std}')
