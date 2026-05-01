x = [i % 10 for i in range(10)]
h = [1./3,1./3,1./3,]


x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

if len(h)< len(x):
    for i in range(len(x)):
        if i >= len(h):
            h.append(0)

def fir_elem(h,x,n):
    suma = 0
    for i in range(len(x)):
        if(n-i)<len(x):
            suma += h[i]*x[n-i]
    return suma

print(fir_elem(h,x,4))

def fir(h,x):
    señal = []
    for i in range(len(h) + len(x) - 1):
        señal.append(fir_elem(h,x,i))
    return señal

print(fir(h,x))


def nota_media(expediente):
    suma = 0
    dicc = {"Sobresaliente": 9, "Notable": 7.5}
    for i in expediente:
        suma += dicc[i]
    return suma/len(expediente)
print(nota_media(['Sobresaliente','Notable']))




