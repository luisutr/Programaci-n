

def codigo_cesar(texto):
    abecedario='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZabc'
    codificacion=[]
    for i in texto:
        for t in range(len(abecedario)):
            if abecedario[t] == i:
                if t+3 < len(abecedario):
                    codificacion.append(abecedario[t+3])
    return list_a_string(codificacion)

def list_a_string (L):
    return "".join(str(x) for x in L)

print codigo_cesar("Hola xyz XYZ")




### no se como seguir, porque lo que llevo hasta ahora lo entiendo, que es recorrer abecedario, y el texto y si son
# iguales i y t anadir al contenedor codificacion con el append el valor de la letra + 3
### pero no se como hacerlo.

#NUnca el return dentro de los for, a no ser que sepa perfectamemte lo que estoy haciendo.

#Siempre probar para ver que demonios hacee mi programa, sino nunca sabre como seguir

#Necesito saber las posiciones del abecedario, porque sino no podria hacer el desplazamiento de 3 POSICIONES

# tiene que devolver una cadena, te pongo una minifuncion que lo convierte


# Te queda controlar los espacios, al meter el abc al final se simplifica un monton