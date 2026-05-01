__author__ = 'luisutrilla'

import math

def media_geometrica(a,b):
    if a*b >= 0:
        z = a*b
        return math.sqrt (z)
    else:
        print ('no es media geometrica')

print media_geometrica(7,4)