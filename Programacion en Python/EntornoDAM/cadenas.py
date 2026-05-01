cadena = "hola"
cadena = cadena[0].upper()+cadena[1:]
print(cadena)
quote = "How can mirrors be real if our eyes aren't real"

def decadenaalista(string):
    palabra=""
    lista=[]
    for i in string:
        if i!=" ":
            palabra+=i
        else:
            lista.append(palabra)
            palabra = ""
    lista.append(palabra)
    return lista


def to_jaden_case(string):
    lista = decadenaalista(string)
    mayus=""
    for palabra in lista:
        palabra = palabra[0].upper() + palabra[1:]
        mayus+=palabra+" "
    return mayus

print(to_jaden_case(quote))


quote = "How can mirrors be real if our eyes aren't rea"
print(quote.split(" "))