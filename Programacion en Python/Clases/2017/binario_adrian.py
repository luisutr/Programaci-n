def array(x): #CASO EN EL QUE LA LONGITUD DEL ARRAY > 1
    lista = []
    for i in range(len(x)): #AQUÍ UTILIZO UN FOR PORQUE HAY QUE RECORRER UN ARRAY DE MÁS DE UN ELEMENTO
        if x[i] == 1 or x[i] == str(1):
            lista.append(int(0))
        elif x[i] == 0 or x == str(0):
            lista.append(int(1))
    return lista

def lonely_array(solitary): #CASO EN EL QUE SABEMOS POR EL ENUNCIADO QUE LA LONGITUD DEL ARRAY == 1
    for j in solitary:
        if len(solitary) == 1 and j == 1 or j == '1':
            return 0
        elif len(solitary) == 1 and j == 0 or j == '0':
            return 1
    return array(solitary) #EN CASO DE QUE LA LONGITUD DE NUESTRO ARRAY > 1, LLAMAMOS A LA FUNCION ARRAY(X) PARA QUE SE
                           #EJECUTE

def binarySwap(n):
    if n == 1 or n == '1': #CASO BASE
        return 0
    elif n == 0 or n == '0': #CASO BASE
        return 1
    else:
        return lonely_array(n) #EN CASO DE NO SER UN CASO BASE, EJECUTA LONELY_ARRAY Y EN CASO DE QUE LA LONGITUD DEL 
                               #ARRAY > 1, PASARÁ A EJECUTAR LA FUNCIÓN ARRAY


print(binarySwap([1, [0, ['1', ['0', [1]]]]]))


print(binarySwap([1, '0']))