# -*- coding: utf-8; mode: python -*-


#Escriba un programa que pida dos números enteros y escriba qué números son pares y cuáles impares desde el primero hasta el segundo.

def paresimpares ():
    numero1 = int(input("Escriba un número entero: "))
    print("Escriba un número entero mayor o igual que", str(numero1) + ":")
    numero2 = int(input())

    if numero2 < numero1:
        print("¡Le he pedido un número entero mayor o igual que", numero1,"!")
    else:
        for i in range(numero1, numero2 + 1):
            if i % 2 == 0:
                print("El número", i, "es par")
            else:
                print("El número", i, "es impar")

paresimpares()

#Escriba un programa que pida un número entero mayor que cero y que escriba sus divisores.
def divisores ():
    numero = int(input("Escriba un número entero mayor que cero: "))

    if numero <= 0:
        print("¡Le he pedido un número entero mayor que cero!")
    else:
        print "Los divisores de", numero, "son :",
        for i in range(1, numero + 1):
            if numero % i == 0:
                print (i),
divisores()


def esprimo():
    numero = int(input("Escriba un número entero mayor que 1: "))

    if numero <= 1:
        print("¡Le he pedido un número entero mayor que 1!")
    else:
        contador = 0
        limite = round(numero ** 0.5)
        for i in range(1, limite + 1):
            if numero % i == 0:
                contador = contador + 1
        if contador == 1:
            print(numero, "es primo")
        else:
            print(numero, "no es primo")
