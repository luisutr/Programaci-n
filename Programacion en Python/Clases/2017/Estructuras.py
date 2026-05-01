__author__ = 'luisutrilla'
# -*- coding: utf-8; mode: python -*-


#-------------------------------------------------------------------------------
# Name:        Paises

 
paises = {
    'Pepito': {'Chile', 'Argentina'},
    'Yayita': {'Francia', 'Suiza', 'Chile'},
    'John': {'Chile', 'Italia', 'Francia', 'Peru'},
}
 
def cuantos_en_comun(a,b):
    num = len((paises[a] & paises[b]))
    return num

#print cuantos_en_comun("Pepito", "John")

#-------------------------------------------------------------------------------
# Name:        Trios pitagoricos

 
def son_pitagoricos(a,b,c):
    if c == (a**2 + b**2)**0.5:
        return True
    else:
        return False
 
def pitagoricos (n):
    lista = []
    for i in range(1,n+1):
        for j in range(1,n+1):
            for k in range(1,n+1):
                if son_pitagoricos(i,j,k):
                    lista.append((i,j,k))
 
    return lista


#-------------------------------------------------------------------------------
# Name:        Signo zodiacal

 
def determinar_signo(fecha_de_nacimiento):
    _,mes,dia = fecha_de_nacimiento
    fecha = (mes,dia)
    if (12,22) <= fecha or fecha <= (1,20):
            return 'capricornio'
    for i,j in signos.items():
        inicio,termino = j
        tupla_zodiacal =(inicio,termino)
 
        if inicio <= fecha and fecha <= termino:
            return i
 
signos = {
   'aries':       (( 3, 21), ( 4, 20)),
   'tauro':       (( 4, 21), ( 5, 21)),
   'geminis':     (( 5, 22), ( 6, 21)),
   'cancer':      (( 6, 22), ( 7, 23)),
   'leo':         (( 7, 24), ( 8, 23)),
   'virgo':       (( 8, 24), ( 9, 23)),
   'libra':       (( 9, 24), (10, 23)),
   'escorpio':    ((10, 24), (11, 22)),
   'sagitario':   ((11, 23), (12, 21)),
   'capricornio': ((12, 22), ( 1, 20)),
   'acuario':     (( 1, 21), ( 2, 19)),
   'piscis':      (( 2, 20), ( 3, 20)),
}

#print determinar_signo([1982,12,15])


#-------------------------------------------------------------------------------
# Name:        Asistencia

 
alumnos = ['Pepito', 'Yayita', 'Fulanita', 'Panchito']
asistencia = [
[True, True, True, False, False, False, False],
[True, True, True, False, True,  False, True ],
[True, True, True, True,  True,  True,  True ],
[True, True, True, False, True,  True,  True ]]
 
def total_por_alumno(asistencia):
    contador = 0
    lista = []
    for i in asistencia:
        for j in i:
            if j:
                contador += 1
        lista.append(contador)
        contador = 0
    return lista
 
def alumno_estrella(asistencia):
    maximo = max(total_por_alumno(asistencia))
    for i in range(len(alumnos)):
        if total_por_alumno(asistencia)[i] == maximo:
            return alumnos[i]


# -*- coding: cp1252 -*-
#-------------------------------------------------------------------------------
# Name:        Cumpleanos

 
n = {
    'Pepito': (1990, 10, 20),
    'Yayita': (1992, 3, 3),
    'Panchito': (1989, 10, 20),
    'Perica': (1989, 12, 8),
    'Fulanita': (1991, 2, 14),
}
 
def mismo_dia(fecha1,fecha2):
    _,_,dia1 = fecha1
    _,_,dia2 = fecha2
    if dia1 == dia2:
        return True
    else:
        return False
 
def mas_viejo(n):
    viejo = (999999,9999999,999999)
    viejo_nombre = ''
    for nombre,fecha in n.items():
        if fecha < viejo:
            viejo = fecha
            viejo_nombre = nombre
    return viejo_nombre
 
def primer_cumple(n):
    primero = (9999,9999)
    for nombre, fecha in n.items():
        _,mes,dia = fecha
        if (mes,dia) < primero:
            primero = (mes,dia)
            nombre_primero = nombre
    return nombre_primero


#-------------------------------------------------------------------------------
# Name:        Conjugador de verbos

def conjuga_verbos():
    pronombres = ['yo', 'tu', 'el', 'nosotros', 'vosotros', 'ellos']

    conjugacion = {
    'ar': ('o', 'as', 'a', 'amos', 'ais', 'an'),
    'er': ('o', 'es', 'e', 'emos', 'is', 'en'),
    'ir': ('o', 'es', 'e', 'imos', 'is', 'en')}

    verbo = raw_input("Ingrese verbo: ")

    comienzo = verbo[:-2]
    terminacion = verbo[-2:]

    for i in range(len(pronombres)):
        print pronombres[i] + " " + comienzo + conjugacion[terminacion][i]


#-------------------------------------------------------------------------------
# Name:        Campeonato de futbol

 
resultados = {
   ('Honduras', 'Chile'):    (0, 1),
   ('Espana',   'Suiza'):    (0, 1),
   ('Suiza',    'Chile'):    (0, 1),
   ('Espana',   'Honduras'): (3, 0),
   ('Suiza',    'Honduras'): (0, 0),
   ('Espana',   'Chile'):    (2, 1),
}
 
def obtener_lista_equipos(resultados):
    lista = []
    for tupla in resultados:
        for pais in tupla:
            if pais not in lista:
                lista.append(pais)
    return lista
 
def calcular_puntos(equipo, resultados):
    puntos = 0
    for tupla,marcador in resultados.items():
        if tupla[0] == equipo:
            if marcador[0] > marcador[1]:
                puntos += 3
            elif marcador [0] == marcador[1]:
                puntos += 1
        elif tupla[1] == equipo:
            if marcador[1] > marcador[0]:
                puntos += 3
            elif marcador [0] == marcador[1]:
                puntos += 1
    return puntos
 
def calcular_diferencia_de_goles(equipo, resultados):
    diferencia = 0
    for tupla,marcador in resultados.items():
        if tupla[0] == equipo:
            diferencia += marcador[0] - marcador[1]
        elif tupla[1] == equipo:
            diferencia += marcador[1] - marcador[0]
    return diferencia
 
def posiciones(resultados):
    paises = obtener_lista_equipos(resultados)
    lista = []
 
    for j in range(len(paises)):
        max_puntos = (-9999,-9999,'pais')
 
        for i in range(len(paises)):
            #(puntos, diferencia, pais)
            tupla = (calcular_puntos(paises[i], resultados), calcular_diferencia_de_goles(paises[i], resultados), paises[i])
            if max_puntos < tupla:
                max_puntos = tupla
        lista.append(max_puntos[2])
        paises.remove(max_puntos[2])
    return lista
 
#print posiciones(resultados)


#-------------------------------------------------------------------------------
# Name:        Personas
 
meses = {
    1: 'enero', 2: 'febrero', 3: 'marzo', 4: 'abril',
    5: 'mayo', 6: 'junio', 7: 'julio', 8: 'agosto',
    9: 'septiembre', 10: 'octubre', 11: 'noviembre',
    12: 'diciembre'}
 
def imprimir_nombres(personas):
    for nombre in personas:
        print nombre[0]
 
def imprimir_fechas(personas):
    for i in personas:
        _,_,fecha = i
        dia, mes, anio = fecha
        print str(dia) + " de "+ meses[mes] + " de "+ str(anio)
 
def cuantas_personas(personas):
    return len(personas)
 
def mi_cumple(personas):
    lista = []
    # Cambiar para que introduzcamos fecha con caracter delimitardor y usemos split para dividirlo y dejarlo como lista de tres
    #cumple = (21,1,1993)
    cumple = []
    cadenacumple = raw_input("Introduce fecha en este formato \"dia/mes/ano\":")
    listacumple = cadenacumple.split("/")
    for i in listacumple:
        cumple.append(int(i))
    cumple = tuple(cumple)
    for i in personas:
        nombre, apellido, fecha = i
        if fecha == cumple:
            lista.append(nombre + " " + apellido)
    return lista
 
def nombre_mas_comun(personas):
    lista = []
    dicc = {}
    for i in personas:
        nombre, apellido, fecha = i
        lista.append(nombre)
    for i in lista:
        if i not in dicc:
            dicc[i] = lista.count(i)
 
    maximo = -9999
    for nombre, repeticion in dicc.items():
        if repeticion > maximo:
            maximo = repeticion
            nombre_repetido = nombre
    return nombre_repetido

personas = (("Luis", "Utrilla",(15,12,1982)),("Carlos", "Musico",(10,10,1992)),("Antonio", "Poker",(11,11,1990)),
            ("Raul", "Tabaco",(12,12,1991)),("Mario", "Airsoft",(13,11,1994)),("Otro", "otro",(4,5,1993)),
            ("Luis", "Castillo",(15,12,1982)))

#print imprimir_nombres(personas)
#print imprimir_fechas(personas)
#print cuantas_personas(personas)
#print mi_cumple(personas)
#print nombre_mas_comun(personas)

#-------------------------------------------------------------------------------
# Nombre:      Manos de poker

 
def es_full(mano):
    conjunto_valor = set()
 
    for i in mano:
        valor, palo = i
        conjunto_valor.add(valor)       # Se agrega al conjunto el valor de la carta
 
    return len(conjunto_valor) == 2     # Si tiene 2 elementos es Full
 
def es_color(mano):
    conjunto_palo = set()
 
    for carta in mano:
        valor, palo = carta
        conjunto_palo.add(palo)
 
    return len(conjunto_palo) == 1
 
def es_escalera(mano):
    lista = []
 
    for carta in mano:
        valor, palo = carta
        lista.append(valor)
 
    lista_ordenada = sorted(lista)
 
    # Recorremos la lista y restamos los elementos adyacentes para ver si es -1
    for i in range(len(lista_ordenada)):
        # Si la iteracion alcanza el ultimo elemento es porque es escalera
        if i == len(lista_ordenada) - 1:
            return True
 
        diferencia = abs(lista_ordenada[i] - lista_ordenada[i + 1])
 
        # Si la diferencia entre dos numeros adyacentes es mayor que 1 no es escalera
        if diferencia > 1:
            return False
 
def es_escalera_de_color(mano):
    conjunto_palo = set()
 
    for carta in mano:
        valor, palo = carta
        conjunto_palo.add(palo)
 
    return es_escalera(mano) and len(conjunto_palo) == 1
 
def es_escalera_real_de_color(mano):
    conjunto_palo = set()
 
    for carta in mano:
        valor, palo = carta
        # Si es As, J, Q o K se agrega el palo al conjunto
        if valor == 1 or valor >= 10:
            conjunto_palo.add(palo)
        else:
            return False
 
    # Si son del mismo color solo habra un elemento en el conjunto
    return len(conjunto_palo) == 1
 
def es_poker(mano):
    contador_cartas = {}
 
    for carta in mano:
        valor, _ = carta
 
        if valor not in contador_cartas:
            contador_cartas[valor] = 1
        else:
            contador_cartas[valor] += 1
 
    for cantidad in contador_cartas.values():
        if cantidad == 4:
            return True
 
    return False
 
def es_trio(mano):
    contador_cartas = {}
 
    for carta in mano:
        valor, _ = carta
 
        if valor not in contador_cartas:
            contador_cartas[valor] = 1
        else:
            contador_cartas[valor] += 1
 
    for cantidad in contador_cartas.values():
        if cantidad == 3:
            return True
 
    return False
 
def es_dobre_pareja(mano):
    conjunto = set()
 
    for carta in mano:
        valor, _ = carta
        conjunto.add(valor)
 
    # Si hay 3 elementos es porque al menos hay un trio o doble par en la mano
    # entonces descartamos que sea trio agregando la condicion que no sea trio
    return len(conjunto) == 3 and not es_trio(mano)
 
def es_pareja(mano):
    conjunto_valor = set()
 
    for carta in mano:
        valor, palo = carta
        conjunto_valor.add(valor)
 
    return len(conjunto_valor) == 4

def poker():
    mano = set()
    cartas_reales = {'A': 1, 'J': 11, 'Q': 12, 'K': 13}

    for i in range(1, 6):
        carta = raw_input("Carta " + str(i) + ": ")

        if carta[0] in cartas_reales:
            valor = cartas_reales[carta[0]]
        else:
            valor = int(carta[:-1])

        pica = carta[-1]
        tupla_carta =(valor, pica)
        mano.add(tupla_carta)

    if es_escalera_real_de_color(mano):
        print "Escalera real"
    elif es_escalera_de_color(mano):
        print "Escalera de color"
    elif es_poker(mano):
        print "Poker"
    elif es_full(mano):
        print "Full"
    elif es_color(mano):
        print "Color"
    elif es_escalera(mano):
        print "Escalera"
    elif es_trio(mano):
        print "Trio"
    elif es_dobre_pareja(mano):
        print "Doble pareja"
    elif es_pareja(mano):
        print "Pareja"
    else:
        print "No forma ninguna combinacion"


#-------------------------------------------------------------------------------
# Name:        Problema de Josefo

 
# Cuando un indice tiene valor 1 es porque esta vivo,
# y cuando tiene 0 es porque esta muerto
def sobreviviente(m, n):
    personas = [1] * m
    i = 1
    while personas.count(1) > 1:
        for j in range(m):
            if i == n and personas[j] == 1:
                personas[j] = 0
                i = 1
            if personas[j] == 0:
                continue
            i += 1
 
    return personas.index(1) + 1
 
#print sobreviviente(12,3)

#-------------------------------------------------------------------------------
# Name:        Compatibilidad entre personas

 
signos_compatibles = {
#   (mujer, hombre)
    ('aries', 'tauro'),
    ('aries', 'geminis'),
    ('aries', 'cancer'),
    ('aries', 'libra'),
    ('aries', 'escorpion'),
    ('aries', 'sagitario'),
    ('aries', 'acuario'),
 
    ('tauro', 'tauro'),
    ('tauro', 'leo'),
    ('tauro', 'virgo'),
    ('tauro', 'escorpion'),
    ('tauro', 'capricornio'),
    ('tauro', 'piscis'),
 
    ('geminis', 'aries'),
    ('geminis', 'tauro'),
    ('geminis', 'geminis'),
    ('geminis', 'libra'),
    ('geminis', 'acuario'),
    ('geminis', 'piscis'),
 
    ('cancer', 'tauro'),
    ('cancer', 'cancer'),
    ('cancer', 'leo'),
    ('cancer', 'virgo'),
    ('cancer', 'libra'),
    ('cancer', 'escorpion'),
    ('cancer', 'piscis'),
 
    ('leo', 'aries'),
    ('leo', 'tauro'),
    ('leo', 'geminis'),
    ('leo', 'libra'),
    ('leo', 'capricornio'),
 
    ('virgo', 'tauro'),
    ('virgo', 'cancer'),
    ('virgo', 'leo'),
    ('virgo', 'virgo'),
    ('virgo', 'escorpion'),
    ('virgo', 'capricornio'),
    ('virgo', 'acuario'),
    ('virgo', 'piscis'),
 
    ('libra', 'aries'),
    ('libra', 'tauro'),
    ('libra', 'geminis'),
    ('libra', 'cancer'),
    ('libra', 'virgo'),
    ('libra', 'escorpion'),
    ('libra', 'acuario'),
 
    ('escorpion', 'tauro'),
    ('escorpion', 'geminis'),
    ('escorpion', 'cancer'),
    ('escorpion', 'virgo'),
    ('escorpion', 'escorpion'),
    ('escorpion', 'acuario'),
    ('escorpion', 'piscis'),
 
    ('sagitario', 'aries'),
    ('sagitario', 'geminis'),
    ('sagitario', 'leo'),
    ('sagitario', 'virgo'),
    ('sagitario', 'libra'),
    ('sagitario', 'escorpion'),
    ('sagitario', 'sagitario'),
    ('sagitario', 'capricornio'),
    ('sagitario', 'acuario'),
 
    ('capricornio', 'tauro'),
    ('capricornio', 'leo'),
    ('capricornio', 'virgo'),
    ('capricornio', 'capricornio'),
 
    ('acuario', 'aries'),
    ('acuario', 'leo'),
    ('acuario', 'libra'),
    ('acuario', 'sagitario'),
    ('acuario', 'acuario'),
    ('acuario', 'piscis'),
 
    ('piscis', 'aries'),
    ('piscis', 'tauro'),
    ('piscis', 'cancer'),
    ('piscis', 'libra'),
    ('piscis', 'capricornio'),
    ('piscis', 'piscis'),
}
 
def compatibles(p1, p2):
    signos = (p1[4], p2[4])
    if p1[1] != p2[1] and abs(p1[2] - p2[2]) < 10 and p1[3] == p2[3] and signos in signos_compatibles:
        return True
    else:
        return False
 
persona_1 = ('Pepito', 'M', 27, 'rock', 'aries')
persona_2 = ('Yayita', 'F', 23, 'rock', 'tauro')
 
#print compatibles(persona_1, persona_2)


##ejercicio
alumnos=['Carlos','Miguel','Alfonso','Batera']
asistencias=[[True,False,True,False],##tenemos una lista grande y dentro de esta
         	[False,True,False,True], ##tenemos varias listas mas pequenas
         	[True,True,False,False],
         	[True,False,False,True]]


def asistencias_alumnos():
    total_alumno = {}
    for i in range(len(alumnos)):
        alumno = alumnos[i]
        for j in range(len(asistencias)):
            asistencia = asistencias[j]
            if asistencia[i] == True:
                if total_alumno.has_key(alumno) != True:
                    total_alumno[alumno]=1
                else:
                    total_alumno[alumno]=total_alumno[alumno]+1
    return total_alumno


#print asistencias_alumnos()

def persona_cumple(personas):
    fecha1=raw_input("introduce la fecha de cumpleanos")
    lista = []
    for i in personas:
        nombre,apellido,fecha=i
        fecha = list(fecha)
        fecha2=str(fecha[0]) + "," + str(fecha[1]) + "," + str(fecha[2])
        if fecha1==fecha2 and i != None:
            lista.append(nombre)
        return lista
print persona_cumple((("Luis","Utrilla",(15,12,1982)),("Carlos","Nombela",(1,9,1993))))
