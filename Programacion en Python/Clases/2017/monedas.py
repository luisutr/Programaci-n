# -*- coding: utf-8; mode: python -*-
"""El nombre voraz proviene de que, en cada paso, el algoritmo escoge el mejor
"pedazo" que es capaz de "comer" sin preocuparse del futuro. Nunca deshace una
decisión ya tomada: una vez incorporado un candidato a la solución permanece
ahí hasta el final; y cada vez que un candidato es rechazado, lo es para siempre."""

def calcula(monto, valor):
    moneda = valor
    for i in range(len(valor)):
        moneda[i]=0
        while (valor[i] <= monto):
            moneda[i]+=1
            monto = monto - valor[i]
    return moneda

def monedas():
    moneda = [500, 100, 50, 10, 5, 1]
        
    #Quiero 23456 en monedas
    saldo = 23476
    cambio = calcula(saldo, moneda)

    print ("Vuelto: "+ str(saldo))

    for i in range(len(cambio)):
        print (str(moneda[i])+" = "+str(cambio[i])+" unidad(es)")


monedas()