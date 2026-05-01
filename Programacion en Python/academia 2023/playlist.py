vglobal = "no vale"
def cancionmaslarga(playlist):
  posmax = -1
  maxt = 0
  # recorro las cnaciones para poder ir comparando cada valor con maxt que
  # inicialmente la he dado un valor muy bajo, para que pueda comparar con la primera
  # y que si ya esa es mayor, que lo va a cumplir siempre, pues que la tome como maximo
  #Como me piden que devuelva la posicion, elijo el método enumerate() que me devuelve posicion y valor
  for pos, val in enumerate(playlist):
    if maxt <  val:
      maxt = val
      posmax = pos
  return "la posición de la cancion más larga es la numero " + str(posmax+1)

#print(cancionmaslarga([3.50,2.25,3.45,4.50,2.37,3.55]))

duraciones=[3.50,2.25,3.45,4.50,2.37,3.55]
titulos=["free bird","tragic kingdom","doggie","dream on","something in the way", "el mambo"]

def ordenatitulos(duracion, titulos):
  ordena=[]
  cancion=""
  while len(ordena)!=len(titulos):
    min = 99
    for i in range(len(duracion)):
      if duracion[i]<min and titulos[i] not in ordena:
        min=duracion[i]
        cancion=titulos[i]
    ordena.append(cancion)
  return ordena

print(ordenatitulos(duraciones,titulos))