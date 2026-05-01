m = [[2, 2, 2, 2, 2],
    [2, 3, 0, 0, 0],
    [1, 1, 1, 1, 1],
    [4, 4, 4, 4, 4],
    [2, 2, 6, 7, 0]]

m[0][3]
m[1][3]
m[2][3]

for i in range(len(m)):
    m[i][3] = 0
    m[i][4] = 0

def mostrarmatriz(m):
    for fila in m:
        con=""
        for elemnto in fila:
            #print(elemnto,end="")
            con += str(elemnto) + " "
        print(con)

mostrarmatriz(m)

print("******************")
hiper= [
            [
                [2, 3, 4],
                [1, 2],
                2,
                [1]
            ],
            [
                2,
                [2, 3],
                1,
                4,
                [2, 2, 6, 7]
            ],
            5
        ]
'''
            [
                [2, 3, 4, 0, 0],
                [1, 2, 0, 0, 0],
                [2, 0, 0, 0, 0]
                [1, 0, 0, 0, 0]
                [0, 0, 0, 0, 0]
            ],
            [
                2,
                [2, 3],
                1,
                4,
                [2, 2, 6, 7]
            ],
            5


normali 

    si el elemento es un numero --- >¿??¿¿
    
    si es lista ¿?¿? --> recorro y miro si son sublistas estan completas sino tengo rellenarlas 
                                        si son enteros tengo crear una lista meto el entero como primero elemento y luego 0 

'''
def genero_matriz_entero(n,d):
    m=[]
    for i in range(d):
        sub=[]
        for j in range(d):
            sub.append(0)
        m.append(sub)
    m[0][0]=n
    return m

#recibe elemento que puede ser matriz o incluso un entero
def normaliza(elemento,d):
    if type(elemento) == int:
        return  genero_matriz_entero(elemento,d)
    # si no es un entero la otra posibilidad es que es una lista
    for n_fila in range(d):
        # ojo pongo un if para que normalice solo las filas que existen, las que no existen en el else se crean a 0s
        if n_fila < len(elemento):
            # miro si solo es un entero, creo una fila nueva a cero y pongo el entero como primer elemento
            if type(elemento[n_fila]) == int:
                sub=[]
                for i in range(d):
                    sub.append(0)
                sub[0]= elemento[n_fila]
                #sustituyo el enetero por la fila nueva
                elemento[n_fila] = sub
            # es que es un alista pero no esta completa, la completo a 0
            if type(elemento[n_fila]) == list:
                if len(elemento[n_fila]) != d:
                    for i in range(len(elemento[n_fila]), d):
                        elemento[n_fila].append(0)
        # las filas que no existen en la matriz las creo nuevas, filas de 0
        else:
            sub = []
            for i in range(d):
                sub.append(0)
            elemento.append(sub)
    return elemento

#print(normaliza([[2, 3, 4],[1, 2],2,[1]], 5))

def normalizarconjunto(conjuntom,d):
    resultado = []
    for m in conjuntom:
        mnorma = normaliza(m,d)
        resultado.append(mnorma)
    return resultado


''' print(normalizarconjunto([
            [
                [2, 3, 4],
                [1, 2],
                2,
                [1]
            ],
            [
                2,
                [2, 3],
                1,
                4,
                [2, 2, 6, 7]
            ],
            5
        ], 5))
'''

def normam(hiper,d):
    for i in range(len(hiper)):
        elemento = hiper[i]
        if type(elemento) != list:
            if type(hiper)==int:
                m=[]
                for filas in range(d):
                    fila=[]
                    for columnas in range(d):
                        fila.append(0)
                    m.append(fila)
                m[0][0]=hiper[i]
                hiper[i]=m
            if type(hiper) == list:
                # es que es un alista pero no esta completa, la completo a 0
                if len(hiper) != d:
                    for i in range(len(hiper), d):
                        hiper.append(0)
        if type(hiper[i]) == list:
            normam(hiper[i],d)
    return hiper

print(normam(hiper,5))