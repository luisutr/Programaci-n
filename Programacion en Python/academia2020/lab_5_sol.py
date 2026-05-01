def splitN(L,n):
    r=[]
    rdiv=[]
    for i in L:
        r.append(i)
    for j in range(0, len(r), n):
        print(j)
        rdiv.append(tuple(r[j:j+n]))
    return tuple(rdiv)

print(splitN(range(6),3))

def matriz_adj(L):
    nodos = sorted(set(sum(L,tuple())))
    matriz=[]
    for y in nodos:
        fila = []
        for x in nodos:
            fila.append(1 if (x,y) in L else 0)
        matriz.append(tuple(fila))
    return tuple(matriz)

def arbol_binario(L):
    tree = None
    for i in L:
        tree = node(tree, i) 
    return tree

def node(tree, i):
    if tree == None:
        return i, None, None
    v, ramaL, ramaR = tree 
    if v > i: 
        return v, node(ramaL, i), ramaR
    return v, ramaL, node(ramaR, i)

def buscar(arbol, valor):
    if arbol == None and valor != None: 
        return False
    v, ramaL, ramaR = arbol
    if v == valor:
        return True
    elif v < valor:
        if ramaR:
            return buscar(ramaR, valor)
        return False
    if ramaL:
        return buscar(ramaL, valor)
    return False

def arbol_a_conjunto(A):
    if A == None: 
        return set()   
    v, ramaL, ramaR = A            
    return {v}.union(arbol_a_conjunto(ramaL)).union(arbol_a_conjunto(ramaR))

def mezcla(A, B):
    D = {}
    for ka, a in A.items():
        D[ka] = a
        for kb, b in B.items():
            if ka == kb in D:
                D[ka] = a,b
            elif kb not in D:
                D[kb] = b
    return D

def hay_ciclo(G): 
    l=[]
    for fila in G:
        for i in fila:
            l.append(i)
    if l[0] == l[-1]:
        return True 
    return False 

def presente_indicativo(verbo):
    terminacion = verbo[-2:]
    raiz = verbo[:-2]
    conjugaciones = {
        'ar': ('o','as','a','amos','áis','an'),
        'er': ('o', 'es', 'e', 'emos', 'éis', 'en'),
        'ir': ('o', 'es', 'e', 'imos', 'ís', 'en')
        }
    l=[]
    for clave,valor in conjugaciones.items():
        if clave == terminacion:
            for i in valor:
                l.append(raiz+i)
    return l

def cuartiles(L):
    values=sorted(L)
    if len(L) < 4:
        efin = values[-1]
        return(q1(values), q2(values), efin, efin)
    return(q1(values), q2(values), q3(values), values.pop())

def q1(values):
    d = abs((len(values)+1)/4)-int((len(values)+1)/4)
    if d != 0:
        return values[int((len(values)+1)/4)-1]+d*(values[int((len(values)+1)/4)]-values[int((len(values)+1)/4)-1])
    return values[int((len(values)/4)-1)]

def q2(values):
    if len(values) % 2 == 0:
        return (values[int((len(values)/2)-1)]+values[int(len(values)/2)])/2
    return values[int(len(values)//2)]

def q3(values):
    d = abs(3*(len(values)+1)/4)-int(3*(len(values)+1)/4)
    if d != 0:
        return values[int(3*(len(values)+1)/4)-1]+d*(values[int(3*(len(values)+1)/4)]-values[int(3*(len(values)+1)/4)-1])
    return values[int(3*(len(values)/4)-1)]


def rpn_to_algebraic(s):
    op = ['+','-','*','/']
    rpn=[]
    for i in s.split():
        if i in op:
            a = str(rpn.pop())
            b = str(rpn.pop())
            rpn.append(str('(' + str(b) + ' ' + i + ' ' + str(a) + ')'))
        else:
            rpn.append(str(int(i)))
    return rpn.pop()

def rpn_to_algebraic2(s):
    op = ['+','-','*','/']
    rpn=[]
    lista = s.split()
    print(lista)
    for i in lista:
        if i in op:
            a = str(rpn.pop())
            b = str(rpn.pop())
            rpn.append(str('(' + str(b) + ' ' + i + ' ' + str(a) + ')'))
        else:
            rpn.append(str(int(i)))
    print(rpn)
    return rpn.pop()

print(rpn_to_algebraic2('12 3 - 2 5 * +'), '((12 - 3) + (2 * 5))')