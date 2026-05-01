def preparar_matriz(matriz):
    i=0
    while i < len(matriz):
        fila=matriz[i]
        for j in range(len(fila)):
            elemento=fila[j]
            if j==i and elemento==0:
                matriz.append(matriz[i])
                matriz.pop(i)

        i+=1



    return matriz
print preparar_matriz([[0,0,0],[1,1,5],[5,0,0],[1,1,0]])



def dividir_lista(fila,elemento):
   aux=[]
   for i in fila:
       if i!=0 and elemento!=0:
           aux.append(float(float(i)/float(elemento)))
       elif i == 0:
           aux.append(i)
       elif i!=0 and elemento==0: #ESTO ES ERROR NO SE PUEDE DAR EL CASO DE DIVIDIR POR CERO
           aux.append(i)
   return aux

def hacer_fila_base(matriz,posicion):
    matriz=preparar_matriz(matriz)

    fila=matriz[posicion]
    elemento=fila[posicion]
    fila_base=dividir_lista(fila,elemento)
    matriz[posicion]=fila_base
    return matriz

    #Prepara siempre arriba la fila base
    #matriz.append(fila_base)
    #matriz.pop(posicion)

#print hacer_fila_base([[5,1,5],[7,1,6],[1,1,1]])




#def hacer_ceros(matriz):
    #matriz=hacer_fila_base(matriz)
    #aux=[]
    #for i in range(len(matriz)-1):
        #elemento=0
        #fila=matriz[i+1]
        #pivote=elegirpivote(matriz,i)

        #while elemento<=i:
            #for j in range(len(fila)):
                #aux.append((fila[elemento]*pivote[j])-fila[j])
            #matriz[i+1]=aux
        #elemento+=1
#print hacer_ceros([[1.0, 0.2, 1.0], [7, 1, 6], [1, 1, 1]])


def hacer_ceros(matriz):
    for i in range(len(matriz)-1):
        elementos = i+1
        for posicion in range(elementos):
            fila=matriz[i+1]
            matriz=hacer_fila_base(matriz,posicion)
            fila_base = matriz[posicion]
            aux=[]
            for j in range(len(fila)):
                operacion=(fila[posicion]*fila_base[j])-fila[j]
                aux.append(operacion)
            matriz[i+1]=aux
    print matriz
    return matriz

print hacer_ceros([[1, 2, 1], [7, 1, 6], [1, 1, 1]])
