def obtener_caracter_hexadecimal(valor):
    # Lo necesitamos como cadena
    valor = str(valor)
    equivalencias = {
        "10": "a",
        "11": "b",
        "12": "c",
        "13": "d",
        "14": "e",
        "15": "f",
    }
    if valor in equivalencias:
        return equivalencias[valor]
    else:
        return valor

def conviertedecimalabase(decimal,base):
    if decimal <= 0:
        return "0"
        # Aquí almacenamos el resultado
    binario = ""
    # Mientras se pueda dividir...
    while decimal > 0:
        # Saber si es 1 o 0
        residuo = int(decimal % base)
        #si es base hex hay que convertir numeros a letras
        if base == 16:
            residuo = obtener_caracter_hexadecimal(residuo)
        # Ir agregando el número (1 o 0) a la izquierda del resultado
        binario = str(residuo) + binario
        # E ir dividiendo el decimal
        decimal = int(decimal / base)
    return binario

print(conviertedecimalabase(2023,16))


def conversorabytes(tam):
    bytes = 0
    unidad=tam[-2:]
    lista = tam.split(" ")
    num = float(lista[0])
    if "KB"==unidad:
        bytes = num * 1024
    elif "MB"==unidad:
        bytes = num * 2048
    elif "GB"==unidad:
        bytes = num * 3072
    elif "EB"==unidad:
        bytes = num * (10**18)
    else:
        bytes = num
    return bytes


print(conversorabytes("40 KB"))

def ordenaportam(lista):
    resul={}
    for tam in lista:
        bytes=conversorabytes(tam)
        resul[tam]=bytes
    return list(reversed(sorted(resul)))

print(ordenaportam(["3 MB","1 GB", "40 KB", "0.5 EB"]))



a=1
b=1
c=0
d=1
#((aANDb)OR(cANDd))
if ((a and b)or(c and d)):
    print(True)
else:
    print(False)
#(((aANDb)ORc)XOR(NOT(d)))
if (((a and b)or c) ^(not(d))):
    print(True)
else:
    print(False)
#(((dXORc)ANDc)OR(aORb))
if (((d^c)and c)or(a or b)):
    print(True)
else:
    print(False)
#(NOT(aORd)AND(cXORd))
if (not(a or d)and(c^d)):
    print(True)
else:
    print(False)