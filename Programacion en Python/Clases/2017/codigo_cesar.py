import string
def codigo_cesar(texto):
    cadena=string.ascii_letters
    posicion=[]
    d=''
    for i in texto:
        cad2=[]
        for j in cadena:
            cad2.append(j)
            if i==' ':
                posicion.append(' ')
                break
            if j==i:
                posicion.append(len(cad2))
                break
    #Recorre todo el abecedario y le asigana numero a cada letra
    #recorreo lista de posiciones de cada letra y si no son caracter vacio, desplaza posiciones.
    #la excepcion la da en el caso que sea X Y o Z que vuelve a marcar com a b o c respectivamente
    print posicion
    for k in posicion:
        try:
            if k==' ':
                d+=' '
            else:
                d+=cadena[k+2]
        except:
            if cadena[k-1]=='X':
                d+='a'
            elif cadena[k-1]=='Y':
                d+='b'
            else:
                d+='c'
    return d

print codigo_cesar("XYZABC")