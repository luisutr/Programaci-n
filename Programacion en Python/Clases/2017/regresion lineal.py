def regresion_lineal(puntos):
    xm = media([p[0] for p in puntos])
    ym = media([p[1] for p in puntos])
    xy = 0.
    xx = 0.
    for p in puntos:
        xy += (p[0]-xm)*(p[1]-ym)
        xx += (p[0]-xm)**2
    a = xy/xx
    b = ym - a*xm
    return a,b

def media(l):
    return sum(l)/len(l)

print regresion_lineal([(0.,1.), (1.,4.), (-1.,-2.)])