from math import *

def libras_a_gramos(l):
    return 453.59237*l
print(libras_a_gramos(1e12))

def velocidad_orbital(M,r,a):
    G = 6.674 * (10 ** -11)
    #G = 6.674e-11
    v=sqrt(2*G*M*((1/r)-(1/(2*a))))
    return v

print(velocidad_orbital(20,1,2))
