__author__ = 'luisutrilla'

def suma_rango (primero,segundo):
        suma=0
        for i in range(primero, segundo):
            suma = i + suma
        suma=suma+segundo
        return suma

#print suma_rango(2,8)

def buscar_vocal(cadena):
    suma=0
    for i in cadena:
        if i in ["a","e","i","o","u"]:
        	suma = suma + 1
    if suma > 0:
        return  suma
    else:
        return -1

#print buscar_vocal("texto")


def dibujar_cuadrado(l):
    dibujar_ancho(l)
    for i in range ((l-2)/2):
        dibujar_largo(l)
    dibujar_ancho(l)



def dibujar_ancho(l):
    print '+' + '-'*(l-2) + '+'


def dibujar_largo(l):
    print  '|' + ' '*(l-2) + '|'


print dibujar_cuadrado(5)

