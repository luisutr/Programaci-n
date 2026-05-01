a = {'a':1,'e':2}
b = {'a':1,'b':2}
#{'a':(1,1),'b':2,'e':2}

for clave, valor in a.items():
    if clave == "a":
        print((clave, valor))
        print(a[clave])

clavesa = list(a.keys())
clavesb = list(b.keys())
claves = clavesa+clavesb
print(claves)
valores = a.values()
print(valores)

#modifica un diccionario CUIDADO DICE QUE NO LOS MODIFIQUEIS SI USAS ESTO HACER UNA COPIA DEL DICC
#a.update(b)
#print(a)



def mezcladiccuno(a,b):
    clavesa = list(a.keys())
    clavesb = list(b.keys())
    claves = clavesa + clavesb
    mezcla={}
    for i in claves:
        if i not in list(mezcla.keys()):
            if i in list(a.keys()):
                mezcla[i]=a[i]
            else:
                mezcla[i]=b[i]
        else:
            if i in list(a.keys()):
                mezcla[i]=(mezcla[i], a[i])
            else:
                mezcla[i]=(mezcla[i], b[i])
    return (mezcla)

def mezcladicc(a,b):
    mezcla={}
    for clave,valor in a.items():
        if clave not in list(mezcla.keys()):
            mezcla[clave] = valor
        else:
            mezcla[clave] = (mezcla[clave], valor)
    for clave,valor in b.items():
        if clave not in list(mezcla.keys()):
            mezcla[clave] = valor
        else:
            mezcla[clave] = (mezcla[clave], valor)
    return mezcla

#print(mezcladicc(a,b))