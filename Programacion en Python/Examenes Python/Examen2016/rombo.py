
def imprimir_rombo(n):
    assert n % 2 == 0, 'El argumento debe ser par'
    assert n >= 2, 'El argumento debe ser mayor o igual a 2'
    for i in range(n/2):
        imprimir_linea_rombo('/', '\\', i, n)
    for i in reversed(range(n/2)):
        imprimir_linea_rombo('\\', '/', i, n)

def imprimir_linea_rombo(a,b,i,n):
    print ' '*(n/2-i-1)+a+' '*(2*i)+b