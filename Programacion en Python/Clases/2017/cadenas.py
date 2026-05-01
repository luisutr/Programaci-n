from string import*


def cifras(entero):
   lista=[]
   cadena=str(entero)
   for i in (cadena):
       i = int(i)
       lista.append(i)
   return lista

#print cifras(1954)


def buscar_texto (cadena, subcadena):
    cuenta = 0
    i= 1
    while i < len(cadena):
        if i==cadena.find(subcadena,i,len(cadena)):
            i=cadena.find(subcadena,i,len(cadena))+len(subcadena)
            cuenta += 1
        else:
            i +=1

    return cuenta

# este no funciona bien

print buscar_texto("No por mucho madrugar amanece mas temprano","ma")