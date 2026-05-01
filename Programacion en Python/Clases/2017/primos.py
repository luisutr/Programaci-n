__author__ = 'luisutrilla'

def primos(entero):
    if entero > 1:     #si es menor que 2 no es primo, por lo tanto devolverá Falso
        for i in range(2, entero):  #bucle en la secuencia de progresión aritmética 2,3,4....entero
            if entero % i == 0:    #si el resto da 0 no es primo
               return False
            return True    #de lo contrario es primo

print primos(3)    #para probarlo llamamos a la función
