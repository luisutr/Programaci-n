def calculacorrelacion(x,y,m,N):
    correlacion = []
    for k in m:
        suma = []
        if k < 0:
            for n in range(N+k):
                suma.append(y[n-k]*x[n])
            correlacion.append(sum(suma))
        else:
            for n in range(N-k):
                suma.append(x[n+k]*y[n])
            correlacion.append(sum(suma))
    return correlacion

def xcorr(x, y):
    if len(x) > len (y):
        N = len(x)
        for i in range(N-len(y)):
            y.append(0)
    else:
        N = len (y)
        for i in range(N-len(x)):
            x.append(0)
    m = range(-1*(N-1),N)
    correlacion = calculacorrelacion(x,y,m,N)
    return tuple(correlacion), m


print(xcorr([1,1,1], [1,2,3,2,1]), ((1,3,6,7,6,3,1,0,0),range(-4,5)))
'''Esta prueba es la que no me pasa'''
