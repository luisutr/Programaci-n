# -*- coding: utf-8; mode: python -*-
def rango_matriz(A):
    return Gauss(A).rango()


def lin_solve(A, B):
    a = Gauss(A).diag()
    b = a.repetir_ops([[x] for x in B])
    return sum(b, []), a.op


def inv_matriz(A):
    a, n = Gauss(A), len(A[0])
    assert a.rango() == n, 'No hay inversa'
    a.diag()
    return a.repetir_ops(identidad(n)), a.op


def identidad(n):
    return [[1 if i == j else 0 for i in range(n)] for j in range(n)]


class ZeroRowError(Exception):
    pass


from copy import deepcopy


class Gauss(object):
    def __init__(self, A):
        self.A = deepcopy(A)
        self.op = []

    def rango(self):
        self.rref()
        return len([x for x in self.A if x != [0] * len(self.A[0])])

    def diag(self):
        ''' Asume A matriz n x m.
            La diagonaliza.
        '''
        self.rref()
        for i in reversed(range(len(self.A))):
            fila = self.A[i]
            pv = left_most(fila)
            if pv >= len(fila): continue
            self.reducir_filas_arriba(i, pv)
        return self

    def rref(self):
        ''' Asume self.A matriz n x m.
            Construye la forma escalonada reducida por filas.
        '''
        try:
            for i in range(len(self.A)):
                self.reducir_filas(i, self.elegir_pivote(i))
        except ZeroRowError:
            pass
        return self

    def reducir_filas(self, i, pv):
        for j in range(i + 1, len(self.A)):
            fila = self.A[j]
            self.mac(j, i, -fila[pv])
        return self

    def reducir_filas_arriba(self, i, pv):
        for j in reversed(range(i)):
            fila = self.A[j]
            self.mac(j, i, -fila[pv])
        return self

    def elegir_pivote(self, i):
        pv, f = min((left_most(fila), i + j) for j, fila in enumerate(self.A[i:]))
        assert pv >= i, 'No redujo bien en el paso anterior'
        if pv >= len(self.A[0]):
            raise ZeroRowError('No hay más pivotes')
        self.xch(i, f)
        self.div(i, self.A[i][pv])
        return pv

    def repetir_ops(self, B):
        X = Gauss(B)
        for op in self.op:
            {'xch': X.xch, 'div': X.div, 'mac': X.mac}[op[0]](*op[1:])
        return X.A

    def xch(self, i, j):
        self.op.append(('xch', i, j))
        if i == j: return
        self.A[i], self.A[j] = self.A[j], self.A[i]

    def div(self, i, k):
        self.op.append(('div', i, k))
        f = self.A[i]
        for j, x in enumerate(f):
            f[j] = x / k

    def mac(self, i, j, k):
        if k == 0: return
        self.op.append(('mac', i, j, k))
        a, b = self.A[i], self.A[j]
        for n, x in enumerate(b):
            a[n] += x * k


def left_most(f):
    for i, x in enumerate(f):
        if x != 0: return i
    return len(f)

def parametricas(impl):
    param = [ es_parametro(impl, i) for i in range(len(impl[0]))]
    return [ fila_parametricas(impl, param, i) for i in range(len(impl[0]))]

def es_parametro(impl, i):
    for fila in impl:
        if left_most(fila) == i:
            return False
    return True

def fila_parametricas(impl, param, i):
    if param[i]:
        return [0]*sum(param[:i]) + [1] + [0]*sum(param[i+1:])
    for fila in impl:
        if fila[i] == 1:
            return [ -x for i,x in enumerate(fila) if param[i] ]
    raise ValueError('Reduce primero la matriz implícita usando Gauss-Jordan')

def implicitas(gen):
    A = Gauss(gen).rref()
    B = A.repetir_ops(identidad(len(gen)))
    return [f for i,f in enumerate(B) if A.A[i] == [0]*len(gen[0]) ]

def transpuesta(matriz):
    matriz_t = []
    for i in zip(*matriz):
        matriz_t.append(list(i))
    return matriz_t

def tuplas_a_lista(S):
    lista_completa = []
    for i in S:
        lista =[]
        for j in i:
            for x in j:
                lista.append(x)
        lista_completa.append(lista)
    return lista_completa

def diagonalizar(A):
    triangulada = Gauss(A).diag()
    return triangulada.A

def eliminar_zeros(matriz):
    final = []
    for j, fila in enumerate(matriz):
        suma = 0
        for i in fila:
            if i == 0:
                suma += 0
            else:
                suma += 1
        if suma != 0:
            final.append(matriz[j])
    return final

def sacar_base(S):
    matriz = diagonalizar(S)
    final = eliminar_zeros(matriz)
    return final

def pasar_tuplas(M,rango):
    tupla_matriz = []
    for fila in M:
        suma = 0
        vector = []
        for element in range(rango) :
            suma += rango
            a = tuple((fila[suma-rango:suma]))
            vector.append(a)
        tupla_matriz.append(tuple(vector))
    return tupla_matriz

def suma(S1,S2):
    matriz1,matriz2 = (sacar_base(tuplas_a_lista(S1))),(sacar_base(tuplas_a_lista(S2)))
    print("Matriz 1")
    print(matriz1)
    print("Matriz 2")
    print(matriz2)
    rango = rango_matriz(matriz1)
    union_1 = matriz1 + matriz2
    gen_union = sacar_base(union_1)
    print("Suma final:")
    return pasar_tuplas(gen_union,rango)

def interseccion(S1,S2):
    matriz1 , matriz2 = transpuesta(sacar_base(tuplas_a_lista(S1))), transpuesta(sacar_base(tuplas_a_lista(S2)))
    print("Matriz 1")
    print(sacar_base(tuplas_a_lista(S1)))
    print("Matriz 2")
    print(sacar_base(tuplas_a_lista(S2)))
    rango = rango_matriz(matriz1)
    implicitas1 ,implicitas2 = implicitas(matriz1), implicitas(matriz2)
    implicitas_union = implicitas1 + implicitas2
    matriz_final = sacar_base(transpuesta(parametricas(sacar_base(implicitas_union))))
    print("Interseccion Final")
    return  pasar_tuplas(matriz_final,rango)

a = [ ((1,0,0),
          (-0,0,0),
          (0,0,0)),
         ((0,0,0),
          (0,1,0),
          (0,0,0)),
         ((0,0,0),
          (0,0,0),
          (0,0,1)) ]
b = [ ((0,0,0),
          (0,1,0),
          (0,0,0)),
         ((0,0,0),
          (0,1,0),
          (0,0,1))]






print("Suma:")
print((suma(a,b)))
print("---------------------------------------------------------------------------")
print("Interseccion:")
print((interseccion(a,b)))