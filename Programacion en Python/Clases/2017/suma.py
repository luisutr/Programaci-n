__author__ = 'luisutrilla'

def multiplicar(a,b):
    resultado = a * b
    #texto = "La multiplicacion de a x b es: "
    return resultado


def multysuma(a,b,c):
    multi=multiplicar(a,b)
    return c+multi


#print(multysuma(2,3,4))


def buclefor (cadena):
    lista=[] # tipo de variable compleja que guarda varias variables de un mismo tipo en la lista

    for i in cadena:
        lista.append(i)

    return lista

print buclefor("hola jacobo")
