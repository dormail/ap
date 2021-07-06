# plot.py

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from functions import differentiate, normalize

def create_plot(fn_input,
        xlabel='',
        ylabel='',
        output='output.pdf'):
    data = pd.read_csv(fn_input)
    x,y = data['x'], data['y']
    
    y = normalize(y)
    x_dif, y_dif = differentiate(x, y)
    y_dif = normalize(y_dif)
    
    plt.scatter(x,y,
            marker='+',
            label='Data')
    plt.scatter(x_dif, y_dif,
            marker='+',
            label='Derivative')
    plt.legend()
    plt.xlabel=xlabel
    plt.ylabel=ylabel
    plt.savefig(output)
    print('Plot saved in ' + output)
    plt.clf()

data_dir = 'Daten/'
create_plot(data_dir + '0025.csv', output='build/0025.pdf')
create_plot(data_dir + '1480.csv', output='build/1480.pdf')
create_plot(data_dir + '1680.csv', output='build/1680.pdf')
create_plot(data_dir + '1975.csv', output='build/1975.pdf')

