
def ceros(lista):
    listasinceros=[]
    listaceros=[]
    for i in lista:
        if type(i)==bool:
            listasinceros.append(i)
        elif i == 0:
            listaceros.append(i)
        else:
            listasinceros.append(i)
    return listasinceros+listaceros
# print ceros([0, None,True,False ])


def cuentapalabras(cadena):
    lista = cadena.lower().split(" ")
    listaveces=[]
    diccresult={}
    for i in lista:
        listaveces.append(lista.count(i))
    for j in range(len(listaveces)):
        if listaveces[j] > 1:
            diccresult[lista[j]]=listaveces[j]
    return diccresult
#print cuentapalabras("Mi casa es mi casa porque es mi casa")

import string
def alfabeticamente(cadena):
    abc= string.ascii_letters
    print abc
    empieza = abc.index(cadena[0])
    for i in cadena:
        if abc.index(i) == empieza:
            si = 0
        else:
            si = 1
        empieza+=1
    if si == 0:
        return True
    else:
        return False

print alfabeticamente("acd")
