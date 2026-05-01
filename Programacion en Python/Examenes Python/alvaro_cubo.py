def dibujar_cuadrado(a):
    dibujar_ancho(a)
    dibujar_largo(a)
    dibujar_ancho(a)

def dibujar_ancho(a):
    print ("+"+ "-"*(a-3)+"+")

def dibujar_largo(a):
    for i in range(1,(a//2)-2):
        print ("|"+ " "*(a-3)+"|")



dibujar_cuadrado(4)