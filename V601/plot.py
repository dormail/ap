# plot.py

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from functions import differentiate, normalize

def create_plot(temp,
        xlabel='',
        ylabel='',
        ydif_scale=1,
        y_scale=1,
        remove_max_dif=False):
    fn_input = 'Daten/' + str(temp) + '.csv'
    data = pd.read_csv(fn_input)
    x,y = data['x'], data['y']
    y = normalize(y)
    

    x_dif, y_dif = differentiate(x, y)

    # remove max derivative if needed
    if(remove_max_dif):
        n = np.argmax(y_dif)
        x_dif[n] = 0
        y_dif[n] = 0

    y_dif = normalize(y_dif)

    plt.scatter(x,y / y_scale,
            marker='+',
            label='Messdaten')
    plt.scatter(x_dif, y_dif / ydif_scale,
            marker='+',
            label='Ableitung')

    plt.legend()

    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    plt.tight_layout()

    output = 'build/' + str(temp) + '.pdf'
    plt.savefig(output)
    print('Plot saved in ' + output)
    plt.clf()

    # export data as a latex table
    x_dif = np.append(x_dif, np.nan)
    y_dif = np.append(y_dif, np.nan)
    d = {   'x': x,
            'y': y,
            #'xdif': x_dif,
            'ydif': y_dif
            }

    df = pd.DataFrame(d)
    output = 'build/' + str(temp) + '.tex'
    df.to_csv(output,
            sep='&',
            float_format="%.3f",
            header=False,
            index=False,
            decimal=',',
            line_terminator=' \\\\\n')
    print('Data saved in ' + output)

data_dir = 'Daten/'
create_plot('0025', xlabel=f'$U_A / $V', ylabel=f'$I_A$')
create_plot(1480, xlabel=f'$U_A / $V', ylabel=f'$I_A$',
        remove_max_dif=False)
create_plot(1680,
        remove_max_dif=True)
create_plot('1975', remove_max_dif=False)

