from mensaje import *

# Abrimos el puerto del arduino a 115200
PuertoSerie = abrirPort("COM3")

# Creamos un bucle infinito
opc = "x"
while opc != "0":
    opc = input("Escriba la opción a realizar (M o B)=: ")
    if opc == "M":
        v1 = ""
        v2 = ""
        K = int(input("Escriba dimensión: "))
        for i in range(K):
            v1 += input("Introduce número del primer vector: ") + ","
        for i in range(K):
            v2 += input("Introduce número del segundo vector: ") + ","
        cadena = opc + ":" + str(K) + ":" + v1[0:-1] + ":" + v2[0:-1] + "\n"
        sendMensaje(PuertoSerie, cadena)

        # Recibimos mensaje de arduino
        resultado = receiveMensaje(PuertoSerie)
        print(resultado)

    if opc == "B":
        cadena = opc
        sendMensaje(PuertoSerie, cadena)

        # Recibimos mensaje de arduino
        resultado = receiveMensaje(PuertoSerie)
        print(resultado)