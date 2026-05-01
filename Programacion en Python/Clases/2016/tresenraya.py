__author__ = 'luisutrilla'

##--------> Proyecto 3 en raya para python <--------##
#--------->           braulio23            <--------##
import os,random
longitud = "0"
latitud = "0"
combinacion=["xxx","ooo"]

fichas = [[" "," "," "],[" "," "," "],[" "," "," "]]
def printtablero():
    os.system("clear")
    for i in range(7):
        print " "

    print "                        "+fichas[0][0]+"    |    "+fichas[0][1]+"    |    "+fichas[0][2]
    print "                        -----+---------+------"
    print "                        "+fichas[1][0]+"    |    "+fichas[1][1]+"    |    "+fichas[1][2]
    print "                        -----+---------+------"
    print "                        "+fichas[2][0]+"    |    "+fichas[2][1]+"    |    "+fichas[2][2]
    for i in range(5):
        print ""
    return 0
def ponerficha(estilo,longitud,latitud,quien=0):
    if longitud>3 or latitud>3:
        print "Numero no permitido"
        raw_input()
        return 1
    if fichas[longitud][latitud]==" ":
        fichas[longitud][latitud] = estilo
        return 0
    else :
        if quien==0:
            printtablero()
            print "Esa casilla ya esta ocupada"
            raw_input()
            return 1
        else :
            return 1
def asignar(quien=0):
    global longitud
    global latitud
    if quien==0:

        longitud=raw_input("Coordenada X : ")
        latitud=raw_input("Coordenada Y : ")
    else :
        longitud = random.randint(0,2)
        latitud = random.randint(0,2)


    return 0
def comprobar(quien=0):

        if fichas[0][0]+fichas[0][1]+fichas[0][2]==combinacion[quien]:
            alertar(quien)
        elif fichas[0][0]+fichas[1][0]+fichas[2][0]==combinacion[quien]:
            alertar(quien)
        elif fichas[0][0]+fichas[1][1]+fichas[2][2]==combinacion[quien]:
            alertar(quien)
        elif fichas[1][0]+fichas[1][1]+fichas[1][2]==combinacion[quien]:
            alertar(quien)
        elif fichas[2][0]+fichas[1][1]+fichas[0][2]==combinacion[quien]:
            alertar(quien)
        elif fichas[0][1]+fichas[1][1]+fichas[2][1]==combinacion[quien]:
            alertar(quien)
        elif fichas[0][2]+fichas[1][2]+fichas[2][2]==combinacion[quien]:
            alertar(quien)
        return 0
def alertar(quien):
    if quien==0:
        print "Estupendo !!! Has ganado!!!!"
        raw_input()

    else :
        print "Muy mal !!! Has perdido !!!"
        raw_input()
    exit(1)

def tresenraya():
    while 1:

      printtablero()
      asignar()
      while ponerficha("x",int(longitud)-1,int(latitud)-1)==1:
          printtablero()
          asignar()
      printtablero()
      comprobar()
      raw_input()
      asignar(1)

      while ponerficha("o",int(longitud),int(latitud),1)==1:
          asignar(1)
      comprobar(1)


tresenraya()