
#media de la media de los vectores
def mediademedia(vec1,vec2):
    m1,m2,mf = 0,0,0
    for i in range(len(vec2)):
        m1+=int(vec1[i])
        m2+=int(vec2[i])
    return ((m1/len(vec1))+(m2/len(vec2)))/2


# split trocea una cadena y devuelve una lista
mensaje = "1#4#1,4,5,3#6,5,3,8"

mensaje = mensaje.split("#")
print(mensaje)
vec1 = mensaje[2].split(",")
print(vec1)
vec2 = mensaje[3].split(",")
print(mediademedia(vec1,vec2))


# convertir de lista a cadena
seq1 = ['hello', 'world', 'hello', 'python']
cadena = ' '.join(seq1)
print(cadena)

# quitar caraxcteres delante y detras de una cadena strim()
str = "00000003210Runoob01230000000"
print(str.strip('0') )

str2 = "   Runoob      "
print(str2.strip()) # El parámetro está vacío, el primer espacio se elimina de forma predeterminada