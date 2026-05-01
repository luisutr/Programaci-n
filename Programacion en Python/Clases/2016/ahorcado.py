__author__ = 'luisutrilla'

def crear_palabra_incognita(palabra):
    return ["_"] * len(palabra)

def perdio_juego(partes_cuerpo):
    if len(partes_cuerpo) == 0:
        return True
    return False

def imprimir_por_pantalla_palabra(adivinanza):
    for i in adivinanza:
            print i,
    print

def verificar_letra_en_palabra(letra, palabra, adivinanza):
    for i in range(len(palabra)):
            if palabra[i] == letra:
                adivinanza[i] = letra

def pierde_parte_cuerpo(partes_cuerpo):
    print "Pierde \"" + partes_cuerpo[0] + "\""
    del partes_cuerpo[0]


def juego():

    partes_cuerpo = ["pierna derecha", "pierna izquieda", "brazo derecho",
                    "brazo izquierdo", "tronco", "cabeza"]
    gana = True

    palabra = raw_input("Ingrese la palabra: ")
    adivinanza = crear_palabra_incognita(palabra)

    print "Comienza el juego!"

    while "_" in adivinanza:
        letra = raw_input("Ingrese letra")
        if letra in palabra:
            verificar_letra_en_palabra(letra, palabra, adivinanza)

            imprimir_por_pantalla_palabra(adivinanza)
        else:
            pierde_parte_cuerpo(partes_cuerpo)
            if perdio_juego(partes_cuerpo):
                print "Has perdido el juego!"
                gana = False
                break

    if gana == True:
        print "Has ganado!"

juego()