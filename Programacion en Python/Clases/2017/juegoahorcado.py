__author__ = 'luisutrilla'

partes_cuerpo=["brazo_d","brazo_i","pierna_d", "pierna_i", "cabeza"]

def recorrerpalabra(palabra, palabrajuego):
    letra = raw_input("ingrese letra: ")
    for i in range(len(palabra)):
        if palabra[i] == letra:
            palabrajuego.pop(i)
            palabrajuego.insert(i,letra)
    for j in palabrajuego:
        if letra == j:
            return palabrajuego
        else:
            partes_cuerpo.pop()
            return palabrajuego

def juego():
    palabra = raw_input("Ingrese palabra: ")
    palabrajuego=[]
    incompleto=True
    for i in range(len(palabra)):
        palabrajuego.append("_")
    for i in palabrajuego:
        if i == "_":
            incompleto=True
            if len(partes_cuerpo)!=0:
                palabrajuego=recorrerpalabra(palabra,palabrajuego)
            else:
                print "Has Perdido"
    for j in palabrajuego:
        if j != "_":
            incompleto=False
    if incompleto == False:
        print "ganado"



# no funciona este


juego()