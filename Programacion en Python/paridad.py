###Bob se prepara para someterse a un test de cociente intelectual. La tarea mas frecuente en este test es encontrar cual
#  de los numeros dados difiere de los demas. Bob observa que casi siempre un numero difiere de los demas en paridad.
# Ayuda a Bob, para comprobar sus respuestas necesita un programa que entre los numeros dados encuentre el que es diferente de los demas respecto
# a la paridad, y devolver la posicion de ese numero.
#Recuerda que tu tarea es ayudar a Bob a resolver un test de inteligencia real, por lo que las posiciones de los elementos empiezan en 1 (no en 0).

def es_par(numero):
    if numero % 2 == 0:
        return 0
    else:
        return 1

def funcion_paridad (lista):
    if ((lista[0]%2)==0 and lista[1]%2 == 0):
        paridad = 0
    elif ((lista[0]%2) !=0 and lista[1]%2 != 0):
        paridad = 1
    elif ((lista[2]%2)==0):
        paridad = 0
    else:
        paridad = 1
    for i in range(len(lista)):
        if paridad != es_par(lista[i]):
            return i+1
    return "no hay diferentes"

print(funcion_paridad([2,2,2,1,2,2,2]))
