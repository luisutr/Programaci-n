meses = [0,31,28,31,30,31,30,31,31,30,31,30,31]
mesesb = [0,31,29,31,30,31,30,31,31,30,31,30,31]

def sumar_dias(fecha, dias):
    dias += fecha[0] - 1
    fecha = (1, fecha[1], fecha[2])
    while dias > 0:
        fecha, dias = sumar_mes(fecha, dias)
    return fecha

def sumar_mes(fecha, dias):
    dm = dias_mes(fecha)
    if dm > dias:
        return (1+dias,fecha[1],fecha[2]), 0
    return siguiente_mes(fecha), dias - dm

def dias_mes(fecha):
    ndias = [[0,31,28,31,30,31,30,31,31,30,31,30,31],
             [0,31,29,31,30,31,30,31,31,30,31,30,31]]
    return ndias[es_bisiesto(fecha[2])][fecha[1]]

def siguiente_mes(fecha):
    if fecha[1] == 12:
        return (fecha[0], 1, fecha[2]+1)
    return (fecha[0], fecha[1]+1, fecha[2])

def es_bisiesto(y):
    return y % 400 == 0 or (y % 4 == 0 and y % 100 != 0)


print sumar_dias((2,2,2014),900)