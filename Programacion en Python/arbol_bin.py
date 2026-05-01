'''miArbol = ['a',   #raíz
      ['b',  #subárbol izquierdo
       ['d', [], []],
       ['e', [], []] ],
      ['c',  #subárbol derecho
       ['f', [], []],
       [] ]
     ]

miArbol = ['a', ['b', ['d',[],[]], ['e',[],[]] ], ['c', ['f',[],[]], []] ]
print(miArbol)
print('subárbol izquierdo = ', miArbol[1])
print('raíz = ', miArbol[0])
print('subárbol derecho = ', miArbol[2])
'''
'''
def raiz(r):
    return [r, None, None]
def insertarDerecho(r,nodo):
    r[2]=raiz(nodo)
def insertarIzquierdo(r,nodo):
    r[1]=raiz(nodo)

def arbol_binario(arbol):
    r = raiz(arbol[0])
    auxiliar = arbol[0]
    for i in range(1,3,1):
        nodo=arbol[i]
        nodoant=arbol[i-1]
        if nodo>nodoant:
            insertarDerecho(r,nodo)
        else:
            insertarIzquierdo(r,nodo)
    for i in range(3,5,1):
        HD = r[2][0] # el nodo es el dos, pero como el mismo ya es una estructura arbol de padre e hijos,
        # debo coger el padre, posicion [0]
        HI = r[1][0]
        #Ademas de los valores como entero, necesito su estructura arbol para llamar a insertar y meter los nuevos
        AHD = r[2]
        AHI= r[1]
        nodo = arbol[i]
        #A parti de ahora, vemos los casos donde puden ir los siguientes nodos,
        # en el hijo arbol izquierdo o en el hijo arbol derecho y en estos a izquierda o a derecha
        # Caso_1 Izquierda Izquierda menor que los dos
            # [1][] a derecha o a izquierda
        #Caso_2 Izquierda Derecha - mayor que el de la izquierda y menos que el de la derecha
        if nodo > HI and nodo < HD:
            insertarDerecho(AHI, nodoant)
        # mayor que los dos
        elif nodo > HI and nodo>HD:
            insertarDerecho(AHD,nodo)
        # mayor que izq y menor que derech
        elif nodo > HI and nodo<HD:
            insertarIzquierdo(AHD,nodo)
    nodo=arbol[-1]
    AIHD = r[1][2]
    AIHI = r[1][1]
    ADHD = r[2][2]
    ADHI = r[2][1]
    HIHD = r[1][2][0]
    if type(r[1][1])== list:
        HIHI = r[1][1][0]
    if type(r[2][2]) == list:
        HDHD=r[2][2][0]
    if type(r[2][1]) == list:
        HDHI=r[2][1][0]
        # mayor que los dos
        if nodo > HDHI and nodo > HDHD:
            insertarDerecho(ADHD, nodo)
        # mayor que izq y menor que derech
        elif nodo > HDHI and nodo < HDHD:
            insertarIzquierdo(ADHD, nodo)
    return r


print(arbol_binario([3, 8, 1, 13, 5, 9]))
#(3, (1, None, None), (8, (5, None, None), (13, (9, None, None), None)))
print(arbol_binario(range(5)))
# (0, None, (1, None, (2, None, (3, None, (4, None, None))))))
print(arbol_binario(list(reversed(range(5)))))
#(4, (3, (2, (1, (0, None, None), None), None), None), None))
print(arbol_binario([]), None)

'''
def dearbolalista(arbol,lista):
    for i in arbol:
        if type(i) == int:
            lista.append(i)
        elif type(i) == tuple:
            dearbolalista(i,lista)
    return lista

def buscar(arbol, valor):
    lista = dearbolalista(arbol,[])
    if valor in lista:
        return True
    return False

#print(buscar((3, (1, None, None), (8, (5, None, None), (13, (9, None, None), None))),13))


def arbol_a_conjunto(arbol):
    lista=[]
    for i in arbol:
        if type(i) == int:
            lista.append(i)
        elif type(i) == tuple:
            dearbolalista(i,lista)
    return set(lista)

print(arbol_a_conjunto((4, (3, (2, (1, (0, None, None), None), None), None), None)),
                 {0,1,2,3,4})

