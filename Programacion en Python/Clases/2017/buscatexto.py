__author__ = 'luisutrilla'

def buscatexto (arg1,arg2):
    lista = arg1.split(arg2)
    print lista
    return len(lista)-1

#print buscatexto('No por mucho madrugar amanece mas temprano cuando voy a casa de ma y madrugo', 'ma')


def buscar_texto2 (cadena, subcadena):
    cuenta = 0
    i= 0
    while i < len(cadena):
        if cadena.find(subcadena,i, len(cadena))>=0:
            i=cadena.find(subcadena)
            cuenta += 1
        else:
            i +=1

    return cuenta

#print buscar_texto2("aaaa vxvxvxholaholavxv   vxv", "vxv")

def buscar_texto (cadena, subcadena):
    cuenta = 0
    j = 0
    longitud = len(cadena)
    while j <= longitud:
        posicion = cadena.find(subcadena,j,len(cadena))
        if posicion != -1:
            cuenta += 1
            j = posicion+1
        else:
            j+=1

    return cuenta

print buscar_texto("aaaa vxvxvxholaholavxv   vxv", "vxv")
print buscar_texto("reparepare", "repare")
print buscar_texto("mamamamamamamama mama ma", "x")