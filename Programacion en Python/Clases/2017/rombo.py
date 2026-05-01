
def imprimir_rombo(n):
    assert n % 2 == 0, 'El argumento debe ser par'
    assert n >= 2, 'El argumento debe ser mayor o igual a 2'
    for i in range(n/2):
        print ' '*(n/2-i-1)+'/'+' '*(2*i)+'\\'
    for i in reversed(range(n/2)):
        print ' '*(n/2-i-1)+'\\'+' '*(2*i)+'/'



imprimir_rombo(10)