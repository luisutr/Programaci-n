nombres = ["Pedro Picapiedra", "Juan Bahamondes", "Pablo Marmol"]
adn = ["00000101010101010101", "00101010101101110111", "00100010010000001001"]
parentezco = []
 
secuencia = raw_input("Ingrese secuencia: ")
 
for i in range(len(adn)):
    contador = 0
    for gen in range(20):
        if adn[i][gen] == secuencia[gen]:
            contador += 1
    parentezco.append(contador*100/20)
 
maximo = max(parentezco)
posicion_maximo_adn = parentezco.index(maximo)
culpable = nombres[posicion_maximo_adn]
 
print "El culpable es " + culpable + " con un parentezco de " + str(maximo) + "%"