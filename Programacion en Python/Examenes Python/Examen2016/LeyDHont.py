def reparto_d_hont(n, votos):
    precios_ordenados = sorted(precios_por_escanno_partido(votos, n),
                               key = celda_precio,
                               reverse=True)
    return cuenta_escannos(precios_ordenados[:n])
def precios_por_escanno_partido(votos, n):
    precios = []
    for partido in votos:
        precios += precios_por_escanno(partido, n)
    return precios
def precios_por_escanno(partido, n):
    return [ (partido[0], partido[1]/i) for i in range(1,n+1) ]

def cuenta_escannos(precios):
    escannos = {}
    for p in precios:
        incrementa_cuenta_escannos(escannos, celda_partido(p))
    return sorted([(k, escannos[k]) for k in escannos ],
                  key = celda_precio,
                  reverse = True)

def incrementa_cuenta_escannos(escannos, partido):
    if partido in escannos:
        escannos[partido] += 1
    else:
        escannos[partido] = 1
def incrementa_cuenta_escannos(escannos, partido):
    if partido in escannos:
        escannos[partido] += 1
    else:
        escannos[partido] = 1

def celda_precio(celda):
    return celda[1]

def celda_partido(celda):
    return celda[0]