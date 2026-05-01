def elem(signal,k):
    if k >= len(signal) or k < 0:
        return 0.
    return signal[k]

def conv_elem(u, v, n):
    sum = 0.
    for k in range(len(u)):
        sum += elem(u,k)*elem(v,n-k)
    return sum

def convolucion(u,v):
    return [ conv_elem(u,v,i) for i in range(len(u)+len(v)-1) ]

u = [ 1., 2., 1., 2., 1., 2., 1., 2. ]
v = [ 1., 2., 3., 2., 1. ]
print convolucion(u,v)

