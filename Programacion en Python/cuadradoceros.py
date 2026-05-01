import copy

def cuadradoceros(M):
    dmayor=0
    mayor=()
    elementos=[]
    listasub2={}
    fin=0
    #bucle de la posicion de inicio
    for iniciox in range(len(M)):
        for inicioy in range(len(M)):
            #bucle de la posicion de fin (siempre sera desde inicio hasta len[M])xq las matrices son cuadradas
            elementos=[]
            for dim in range(len(M)):
                for fila in range(len(M)):
                    elemento=[]
                    for e in range(iniciox,dim):
                        elemento.append(M[fila][e])
                        fin=e
                    if elemento != [] and sum(elemento)==0 and len(elemento)>1:
                        elementos.append(copy.deepcopy(elemento))
                if elementos !=[]:
                    dimension = len(elementos)*len(elementos[0])
                    #print(elementos)
                    #Guardo en un diicionario la matriz y como clave sus tuplas de inicio y fin
                    listasub2[(iniciox,inicioy),(fin,fila)]=(copy.deepcopy(elementos))
                    #print (listasub2)
                    if dmayor < dimension:
                        dmayor=dimension
                        mayor=(iniciox,inicioy),(fin,fila)
    return mayor, listasub2[mayor]


print(cuadradoceros([[1,0,0,1],[1,0,0,1],[0,0,0,1],[1,1,1,1]]))


#La solucion era mejor pensar el resultado en las tuplas y como se modifican y varian segun se mueve por la matriz.
#partir de ahi sin preocuparse anto de la matriz. ahber creado un sistema que fuese capaz de sacar todas las cordenadas
