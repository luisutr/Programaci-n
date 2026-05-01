print ([0] * 4)

from math import pi
def pi_leibniz(n):
    pileib=0
    for i in range(n):
        pileib+=((-1)**i)/((2*i)+1)
    return pileib*4

print(pi_leibniz(200))


arbol = (3, (1, None, None), (8, (5, None, None), (13, (9, None, None), None)))

cadena = str(arbol)
cadea2= cadena.replace("(","")
cadea2= cadea2.replace(")","")
cadea2= cadea2.replace("None","")
cadea2= cadea2.replace(" ","")
cadea2 = cadea2.split(",")
print(cadea2)
lista=[]
for i in cadea2:
    if i!="":
        lista.append(int(i))
print(set(lista))

