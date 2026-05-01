# Normal -->abcdefg
#Cesar 3 -->defghij
abcminus="abcdefghijklmnñopqrstuvwxyz"
abcmayus="ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
print(len(abcminus))
def codificacesar(frase, n):
    codificado=""

    # recorriendo y concatenando las letras desplazadas 3 veces, ojo cuando llegue a una posicion que no pueda aplciar
    # el desplazamiento, tendre que volver al inicio
    for i in range(len(frase)):
        if frase[i]==" ":
            codificado += frase[i]
        else:
            if frase[i].islower():
                pos = abcminus.find(frase[i])
                if(n+pos)<=len(abcminus):
                    codificado+=abcminus[pos+n]
                else:
                        codificado += abcminus[n-27-pos-1]

    return codificado

print(codificacesar("abc def xyz", 3))