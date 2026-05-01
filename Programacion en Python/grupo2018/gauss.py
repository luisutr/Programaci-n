# -*- coding: utf-8; mode: python -*-

def rango_matriz(A):
    return Gauss(A).rango()


def lin_solve(A, B):
    a = Gauss(A).diag()
    b = a.repetir_ops([[x] for x in B])
    print "Triangulada"
    print a.A
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


"""print rango_matriz([[1,1,1], [1,0,1], [1,2,3]])

print lin_solve([[1,1,1], [1,0,1], [1,2,3]], [1,2,3])

print inv_matriz([[1,1,1], [1,0,1], [1,2,3]])"""