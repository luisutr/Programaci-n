from datetime import datetime
now = datetime.now()
def saluda(nombre):
    if now.hour < 14:
        print("Buenos dias, "+nombre)
    elif now.hour < 21:
        print("Buenos tardes, " + nombre)
    else:
        print("Buenos noches, " + nombre)

def dimeedad():
    return int(input("Dime tu edad, por favor:"))

def automata(personalidad):
    if personalidad == "simpatico":
        nombre = input("Hola colegui, dime tu nombre: ")
        saluda(nombre)
        edad = dimeedad()
        if edad > 18 and now.hour>20:
            print("Colegui vamos a la Ramona a por unas beers !!")
        elif edad > 18 and now.hour<20 and now.hour>15:
            print("Colegui vamos a echar unos vicios!! ")
    elif personalidad == "agresivo":
        nombre = input("Que pasa looser, dime tu nombre: ")
        saluda(nombre)
        edad = dimeedad()
        if edad > 18 and now.hour > 20:
            print("Dame lo que tengas encima o te machaco !!")
        elif edad > 18 and now.hour < 20 and now.hour > 15:
            print("Espera a que sean mas de las ocho y veras !!! ")

automata("agresivo")