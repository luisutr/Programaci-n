__author__ = 'Luis'

def arbolnavidad(altura):
    for i in range(altura):
        espacios = altura - i - 1
        asteriscos = 1 + i * 2
        print " " * espacios + "*" * asteriscos

arbolnavidad(4)


def arbol(h):
    for i in range(1,h+1):
        print (int(h)-i)*" "+"*"*i+" "*(int(h)-i)

arbol(5)