#practica3

def producto(args, kwds):
    if type(args)==list:
        args=(args),
    pools=args*kwds
    def cycle(values, uplevel):
        for prefix in uplevel:  # cycle through all upper levels
            for current in values:  # restart iteration of current level
                yield prefix + (current,)
    step = iter(((),))
    for pool in pools:
        step = cycle(pool, step)   # build stack of iterators
    return step

def sumas(n):
    try:
        soluciones=[]
        x = list(range(1,n))
        permutaciones=[]
        for i in range(1,n+1):
            permutaciones+=([list(p) for p in producto(x, i)])
        for lista in permutaciones:
            if sum(lista)==n and tuple(sorted(lista)) not in soluciones:
                soluciones.append(tuple(sorted(lista)))
        soluciones.append((n,))
        return (soluciones)
    except (RuntimeError, StopIteration):
        return (soluciones)

print(sumas(4))
print(sumas(5))
print(sumas(6))
print(sumas(7))

# Descomenta la siguiente línea y la última para ejecutar las pruebas
from unittest import TestCase, main

class Test(TestCase):

    def test_sumas(self):
        def check_sumas(n, sz):
            S = sumas(n)
            self.assertEqual(len(S), sz, 'sumas({}) deberia tener {} secuencias'.format(n,sz))
            L = set(tuple(sorted(e)) for e in S)
            self.assertEqual(len(L), sz, 'sumas({}) deberia tener {} secuencias diferentes'.format(n,sz))
            for e in L:
                self.assertEqual(sum(e), n, 'La suma de {} no da {}'.format(e,n))
        check_sumas(4,5)
        check_sumas(5,7)
        check_sumas(6,11)
        check_sumas(7,15)



# Si usas Jupyter o VSCode descomenta la última línea
# Si usas IDLE, Python o PyCharm descomenta la penultima
main()
#main(argv=['first-arg-is-ignored'], exit=False)
