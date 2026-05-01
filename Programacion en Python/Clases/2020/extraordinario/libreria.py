def es_par(n):
    if n%2==0:
        return True
    else:
        return False

def devuelve_impares(a,b):
    impares = []
    for i in range(a,b+1):
        if es_par(i) == False:
            impares.append(i)
    return impares

def devuelve_vocales(cadena):
    listadevcales=[]
    vocales = ["a","e","i","o","u"]
    for i in cadena:
        if i.lower() in vocales:
            listadevcales.append(i)
    return listadevcales

