def prueba(nombre):
    mensaje = "Hola "
    salir=1
    if nombre == "Luis":
        nombre = nombre+" Utrilla "
    mensaje = mensaje+nombre
    #for i in range(3):
    while(salir!=0):
        salir = int(input("Para salir pulsa 0"))
        print(mensaje)
    return "Hasta Luego"

print(prueba("Luis"))
