def es_escalera_henar(escalera):
    lista=[]
    for i in escalera:
        lista.append(i[0])
    diccionario = {"1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "D":10, "J":11, "Q":12, "K":13}
    sublista=[]
    for j in lista:
        x=diccionario.get(j)
        sublista.append(x)
    for n in range(len(sublista)-1):
        if sublista[n]+1!=sublista[n+1]:
            return False
    return True

def es_escalera(mano):
    global lista
    lista=[]
    ordenada=[]
    aaa=str_a_entero(lista)
    for i in mano:
        lista=[]
        lista.append((i[0]))
    aaa=str_a_entero(lista)
    for j in aaa:
        bbb=sorted(aaa)
        ordenada.append(bbb)
    for a in range(len(ordenada)-1):
        if ordenada[a+1]!=ordenada[a]+1:
            return False
    return True
def str_a_entero(lista):
    entero=[]
    for k in lista:
         n=int(k)
         entero.append(n)
    return entero


print (es_escalera(['2P','3D','4T','5C','6C']))

print (es_escalera(["1P","2P","3P","4P","5P"]))
