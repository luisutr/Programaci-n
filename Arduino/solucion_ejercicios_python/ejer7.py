d = {'L':('cordero','manzana'),
    'M':{'bacalao','yogur'},
     'X': {'pollo', 'platano'},
     'J': {'merluza', 'natillas'},
     'V': {'ternera', 'mousse'},
     'S': {'lenguado', 'pera'},
     'D': {'conejo', 'helado'},
     }

def menu():
    print()
    print('0) Salir')
    print('1) Rellenar el menú completo.')
    print('2) Consultar el menú de un día.')
    print('3) Cambiar el menú de un día.')
    print('4) Mostrar el menú completo.')
    return input('Dame una opcion de las anteriores: ')

def mostrar_dia(dia):
    print('{} -> {}'.format(dia, d[dia]))

def mostrar_todo():
    for e in d:
        print( '{} -> {}'.format( e, d[e]) )

def cambiar_dia(clave, primero, postre):
    d[clave] = {primero, postre}

def cambiar_menu():
    for e in d:
        primero = input('Dame el primer plato.')
        postre = input('Dame el postre.')
        cambiar_dia(e, primero, postre)

opc = ''
while opc!='0':
    opc = menu()
    if opc=='1':
        cambiar_menu()
        mostrar_todo()
    elif opc=='2':
        dia = input('¿De qué día quieres ver el menú? (L, M, X, J, V, S, D)')
        mostrar_dia(dia)
    elif opc == '3':
        clave = input('¿De qué día quieres cambiar el menú? (L, M, X, J, V, S, D)')
        primero = input('Dame el primer plato.')
        postre = input('Dame el postre.')
        cambiar_dia(clave, primero, postre)
        print('{} -> {}'.format(clave, d[clave]))
    elif opc == '4':
        mostrar_todo()

