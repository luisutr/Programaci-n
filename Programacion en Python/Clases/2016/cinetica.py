__author__ = 'luisutrilla'


def energia_cinetica(m,t):
    v = 9.81 * float(t) # es una formula de caida libre. g=9.8
    energia= 1 * m * (v**2)/2

    return energia

print energia_cinetica(20,6.60)