# -*- coding: utf-8 -*-

import random
import matplotlib.pyplot as plt


def leer_temperaturas():
    # 12 temperaturas ordenadas
    mx = sorted([ round(random.uniform(0.0, 40.0), 2) for x in range(12) ])
    # las reordenamos para que se parezca más a un año normal
    mx = mx[::2] + mx[::-2]
    # mínimos restando algo a los máximos
    mn = [ m - random.uniform(5.0, .3*m) for m in mx ]
    return mn, mx

tmin, tmax = leer_temperaturas()

plt.title(u'Temperatura en Madrid (año 2015)', fontsize='x-large')
plt.xlabel('mes')
plt.ylabel(u'temperatura (ºC)')
plt.xticks(range(12),['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic'])

plt.plot(tmax, 'ro--', label=u'máxima')
plt.plot(tmin, 'bo--', label=u'mínima')
leyenda = plt.legend(loc='upper right', shadow=True, fontsize='large')
plt.show()
plt.savefig('plot.pdf')