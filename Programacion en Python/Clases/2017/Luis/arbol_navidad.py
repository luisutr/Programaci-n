import sys
 
def es_par(numero):
    return (numero % 2 == 0)
 
def dibujar_rombo(lineas):
    lineas = int(lineas)
    if es_par(lineas):
        print ('El numero de lineas es par, no puedo escribir un rombo perfecto')
    else:
        espacios = int(lineas / 2)        
        disminuyo = False
        cantidad = 1
        str = ''
        for i in range(lineas):
            for n in range(espacios):
                str += ' '                
            for n in range(cantidad):
                str += '*'
            print(str)
            if len(str) == lineas:
                disminuyo = True
            if disminuyo:
                cantidad -= 2
                espacios += 1
            else:
                cantidad += 2
                espacios -= 1
            str = ''

def imprimirRombo(n):
    n = n//2
    for i in range(n,0,-1):
        for j in range(n,(n-(i+1)),-1):
            print (''),
        for k in range(i+1,n+1):
            print ('*'),
        print
    for i in range(0,n):
        for j in range(n,(n-(i+1)),-1):
            print (''),
        for k in range(i+1,n+1):
            print ('*'),
        print()

imprimirRombo(10)


dibujar_rombo(9)
    #dibujar_rombo(9)     