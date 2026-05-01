seguir = "no"
seguir = input("¿Quieres seguir,(si/no)?: ")
while(seguir=="si"):
    print("estoy en bucle O_o")
    seguir = input("¿Quieres seguir,(si/no)?: ")
print(" ^_^ Biiiien! he salido")


def diasmes():
    meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre",
             "Noviembre", "Diciembre"]
    dias = [31,28,31,30,31,30,31,31,30,31,30,31]
    for i in range(len(meses)):
        if dias[i]==31:
            print(meses[i])
diasmes()
