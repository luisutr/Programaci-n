p_capital = {
    'Canada':'Ottawa',
    'Inglaterra':'Londres',
    'Francia':'Paris',
    'Israel':'Jerusalen',
    'Italia':'Roma',
    'Japon':'Tokio',
    'China':'Pekin',
    'Grecia':'Atenas'
}

c_pais = {
    'Ottawa':'Canada',
    'Londres':'Inglaterra',
    'Paris':'Francia',
    'Jerusalen':'Israel',
    'Roma':'Italia',
    'Tokio':'Japon',
    'Pekin':'China',
    'Atenas':'Grecia'
}

def acceso_diccionario(d,pais):
    try:
        return d[pais]
    except:
        return 'error'

def busca(clave):
    s = acceso_diccionario(p_capital,clave)
    if 'error'!=s:
        return s
    s = acceso_diccionario(c_pais,clave)
    if 'error'!= s:
        return s
    return clave + 'no es capital o pais en diccionario'


s = ''
while s!='fin':
    s = input('Dame un pais o capital, fin para terminar\n')
    if s!='fin':
        print( busca(s) )

