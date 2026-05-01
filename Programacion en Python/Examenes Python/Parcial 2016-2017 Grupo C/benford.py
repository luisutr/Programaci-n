def bendfor(lista):
    uno = 0.000
    dos = 0.000
    tres = 0.000
    cuatro = 0.000
    cinco = 0.000
    seis = 0.000
    siete = 0.000
    ocho = 0.000
    nueve = 0.000
    totales = 0.000
    for i in lista:
        descompuesto = []
        numero = str(i)
        for n in numero:
            descompuesto.append(n)
        if descompuesto[0] == "1":
            uno += 1
            totales += 1
        if descompuesto[0] == "2":
            dos += 1
            totales += 1
        if descompuesto[0] == "3":
            tres += 1
            totales += 1
        if descompuesto[0] == "4":
            cuatro += 1
            totales += 1
        if descompuesto[0] == "5":
            cinco += 1
            totales += 1
        if descompuesto[0] == "6":
            seis += 1
            totales += 1
        if descompuesto[0] == "7":
            siete += 1
            totales += 1
        if descompuesto[0] == "8":
            ocho += 1
            totales += 1
        if descompuesto[0] == "9":
            nueve += 1
            totales += 1
    recuento = (uno/totales,dos/totales,tres/totales,cuatro/totales,cinco/totales,seis/totales,siete/totales,ocho/totales,nueve/totales)
    return recuento


print bendfor([10,100,1000,10000,20,30,40,566,644,98])