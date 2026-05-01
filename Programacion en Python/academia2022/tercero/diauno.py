def menu():
    print("1) Insertar lista de numeros")  #metodo split() y convertir a lista de numeros enteros
    print("2) Calcula media") # metodo sum() para ayudarme a calcular e imprimir la media
    print("3) Calcula moda")
    print("4) Salir ")


def princiapl():
    listan = []
    lista = ""
    media=0
    menu()
    op = input("Pulse el numero de opción y despues Intro: ")
    while op!="4":
        if op == "1":
            lista = input("Inserta lista tipo 2,24,6,58,9 de la longitud que quieras:")
            lista = lista.split(",")
            for i in lista:
                listan.append(int(i))
        elif op == "2":
            media=sum(listan)/len(listan)
            print("Media: "+str(media))
        elif op == "3":
            print("Estoy en la opción 3")
        else:
            print("Solo puedes dar valores del menu")
        op = input("Pulse el numero de opción y despues Intro: ")
    return ("Gracias")


print(princiapl())


