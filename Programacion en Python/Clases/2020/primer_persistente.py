def primer_persistente(n):
    for i in range (10,10000):
        grado = gradopersistencia(i)
        if (grado == n):
            return i

def gradopersistencia(num):
    grado = 0
    while (len(str(num))>=2):
        per = 1
        for i in str(num):
            per *= int(i)
        num = per
        grado += 1
    return grado

print(primer_persistente(4))

# 11             ***** BUCLE que va del 10 al 99999***
# 1 * 1 = 1 ***** RECORRO NUMERO
# --> 1  como es menor que 10 ya hemos terminado  **** CONDICION  SI ES MENOR ESE ES EL GRADO****
#                               ****** SI ES MAYOR QUE 10 TIENE QUE SEGUIR DESCOMPONIENDO ******
# grado persistencia 1  ***** CONDICION SI EL GRADO ES == AL QUE ME PIDEN TENEMOS SOLUCION *****
#21
# 2*1 = 2 y es < 10
# grado 1
#25
#2*5 = 10 > 10 --> 1*0 = 0 < 10
#grado 2
#




