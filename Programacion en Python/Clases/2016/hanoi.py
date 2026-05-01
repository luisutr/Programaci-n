__author__ = 'luisutrilla'

def hanoi(N, inc='1', temp='2', fin='3'):

    if N > 0:
        hanoi(N-1, inc, fin, temp)
        print 'se mueve de torre', inc, 'a torre', fin
        hanoi(N-1, temp, inc, fin)

discos = int(input("Ingresa el numero de discos:"))
hanoi(discos)