import random

def creaDiccionario():
    cartas = {}
    for c in ('rojo','verde','azul','negro'):
        for n in range(1,6):
            cartas[c[0]+str(n)]= (c,n)
    return cartas

def muestraDiccionario(cartas):
    for e in cartas:
        print( e, cartas[e] )

def baraja(cartas):
    l = [e for e in cartas ]
    print('antes',l)
    random.shuffle(l)
    return l

def sacaCarta(l):
    return l.pop()

# crea el diccionario de cartas
cartas = creaDiccionario()
# muestra las cartas por pantalla
#muestraDiccionario(cartas)
# las baraja, genera una lista con la mezcla
l = baraja(cartas)
print('después', l )
# sacar cartas
s = ''
while s!='fin':
    s = input('s para sacar, b para barajar, fin para terminar\n')
    if s=='s' or s=='S':
        c = sacaCarta(l)
        print( cartas[c], l )
    elif s=='b' or s=='B':
        l = baraja(cartas)
        print('después', l)
    elif s == 'fin':
        break

