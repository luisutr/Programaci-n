def buscar_texto (cadena, subcadena):
   return recorrecadena(cadena, subcadena,0,0)

def recorrecadena (cadena, subcadena,veces,posicion):
    posicion = cadena.find(subcadena,posicion,len(cadena))
    if posicion != -1:
        veces += 1
        posicion = posicion+1
    else:
        posicion+=1
    if posicion <= len(cadena) - len(subcadena):
        return recorrecadena(cadena, subcadena,veces,posicion)
    else:
        return veces

#print buscar_texto("aaaa vxvxvxholaholavxv   vxv", "vxv")
print buscar_texto("repareparepare repare pare repare", "repare")