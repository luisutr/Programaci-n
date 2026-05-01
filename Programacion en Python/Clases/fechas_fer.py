__author__ = 'luis'

def dias_entre_fechas(tupla1,tupla2):
    dia1,mes1,ano1 = tupla1
    dia2,mes2,ano2 = tupla2
    meses = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    febrero = {2:29}
    restodia1 = 0
    restodia2 = 0
    restomes1 = 0
    restomes2 = 0
    restoano1 = 0
    restoano2 = 0
    anosmedios = 0
    bisiesto = []

    for n in range (ano1,(ano2+1)):
        if n %400 == 0:
            bisiesto.append(n)
        if n%4 == 0 and n%100 != 0:
            bisiesto.append(n)


    restodia1 = meses[mes1] - dia1
    if mes1 == 12:
        restomes1 = 0
    for i in range(mes1+1,13):
        restomes1 += meses[i]
    restoano1 = restodia1 + restomes1
    if mes1 <= 2 and ano1 in bisiesto:
        restoano1 += 1

    restodia2 = meses[mes2] - dia2
    if mes2 == 12:
        restomes2 = 0
    for a in range(mes2+1,13):
        restomes2 += meses[a]
    restoano2 = restodia2 + restomes2
    if mes2 > 2 and ano2 in bisiesto:
        restoano2 += 1

    if ano2 - ano1 > 1:
        for k in range((ano1+1),ano2):
            if k in bisiesto:
                anosmedios += 366
            anosmedios += 365
    anosmedios == 0


    return anosmedios + restoano1 + (365 - restoano2)


print dias_entre_fechas((25,10,2000),(4,1,2002))


import time
from datetime import *

fecha2 = datetime(2000, 10, 25, 0, 0, 0)
fecha1 = datetime(2002, 1, 4, 0, 0, 0)
diferencia = fecha1 - fecha2
print("Fecha1:", fecha1)
print("Fecha2:", fecha2)
print("Diferencia:", diferencia)
print("Entre las 2 fechas hay ", diferencia.days, "dias y ", diferencia.seconds, "seg.")