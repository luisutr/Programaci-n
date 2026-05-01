__author__ = 'luisutrilla'

def pinta_cuadrado(lado):
    for y in range(0, lado):
        for x in range(0, lado):
            if (y==0) or (x==0) or (y==lado-1) or (x==lado-1):
                if (y==0) and (x==0) or (y==lado-1) and (x==0) or (x==lado-1) and (y==0) or (y==lado-1) and (x==lado-1):
                    print "+",
                elif (y!=lado-1 and y!=0):
                    print "|",
                else:
                    print "-",
            else:
                print" ",
        print""

        lista = range(1,7)
        longitud = len(lista)


pinta_cuadrado(6);


