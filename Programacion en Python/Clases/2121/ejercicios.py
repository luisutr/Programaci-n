

lista = [3,5,6,1,2]
#        0,1,2,3,4

#  lista[1] --> 5

print(lista[1])

range(len(lista))  # len --> 5 , range --> [0,1,2,3,4]

print(range(5)) # [0,1,2,3,4]
print(range(2,5)) # [2,3,4]
print(range(2,9,2)) # [2,4,6,8]

for posicion in range(len(lista)):
    print(posicion, lista[posicion])

for posicion, valor in enumerate(lista):
    print(posicion, valor)

print("----------------------------------")

matriz =[[2,4,2,6],
         [7,9,3,2],
         [9,5,2,1],
         [1,3,6,3]]
#           0          1          2         3
print(matriz[1][1])
fila = matriz[1]
print(fila[1])

matriz[0][0]
matriz[1][0]
matriz[2][0]
matriz[3][0]
for i in range(len(matriz)):
    matriz[i][i]=0
print(matriz)


def ejercicio_matriz(matriz):
   numerospares = []
   posicion = []
   for i in range(len(matriz)):
      for j in range(len(matriz)):
         if matriz[i][j]%2 == 0:
            numerospares.append(matriz[i][j])
            posicion.append((i,j))
   return (numerospares,posicion)
print(ejercicio_matriz([[2,4,2,6],[7,9,3,2],[9,5,2,1],[1,3,6,3]]))


#funcion devuelve string de elementos fila  (numero fila)   -> (0) "2426"
#funcion devuelve string de elementos columna  (numero de columna) --> (0) "2791"
##funcion devuelve string de elementos diagonal  (numero de fila y columna )  (0,0) --> "2923"
print("-------------------------")
def ejercicio2_matriz(matriz, n_fila, n_columna):
    fila = ''
    columna = ''
    diagonal = ''
    for i in range(len(matriz)):
        fila = fila + str(matriz[n_fila][i])
        columna = columna + str(matriz[i][n_columna])
    # para la diagonal
    limite = False
    while limite==False:
        if n_fila >= len(matriz[0]):
            limite = True
        if n_columna >= len(matriz):
            limite = True
        if limite == False:
            diagonal = diagonal + str(matriz[n_fila][n_columna])
        n_fila = n_fila+1
        n_columna = n_columna+1
    return (fila, columna, diagonal)


print(ejercicio2_matriz([[2, 4, 2, 6], [7, 9, 3, 2], [9, 5, 2, 1], [1, 3, 6, 3]], 0, 0))
matriz =[[2,4,2,6],
         [7,9,3,2],
         [9,5,2,1],
         [1,3,6,3]]


print("-------------------------")
cadena = 'me gusta la mermelada'
print(cadena.find('la'))
print(cadena.find('lo'))

m=[[2,4,2,6],[7,9,3,2],[9,5,2,1],[1,3,6,3]]
def devuelve_diag(a,b):
	A=len(m)-max(a,b)
	diag=""
	i=0
	while i<A:
		diag+=str(m[a+i][b+i])
		i+=1
	return diag
print(devuelve_diag(2,2))



# SOPA DE LETRAS

def devuelve_fila(matriz,n_fila):
  fila = ''
  for i in range(len(matriz)):
    fila = fila + str(matriz[n_fila][i])
  return fila
#print(devuelve_fila([[2, 4, 2, 6], [7, 9, 3, 2], [9, 5, 2, 1], [1, 3, 6, 3]],0))

# Hacer la funcion que dada una columna te la devuelva en una cadena de caracteres:
def devuelve_columna(matriz,n_columna):
  columna = ''
  for j in range(len(matriz)):
    columna = columna + str(matriz[j][n_columna])
  return columna
#print(devuelve_columna([[2, 4, 2, 6], [7, 9, 3, 2], [9, 5, 2, 1], [1, 3, 6, 3]],0))

# A continuacion, se saca la diagonal, dando un punto inicial de la matriz:
def devuelve_diagonal(matriz,n_fila,n_columna):
  diagonal = ''
  while n_columna <= len(matriz)-1 and n_fila <= len(matriz)-1:
    diagonal = diagonal + str(matriz[n_fila][n_columna])
    n_columna = n_columna + 1
    n_fila = n_fila +1
  return diagonal
#print(devuelve_diagonal([[2, 4, 2, 6], [7, 9, 3, 2], [9, 5, 2, 1], [1, 3, 6, 3]],1,2))


# como la mtriz de una sopa de letras es cuadrada, misma long de filas que de columnas
def sopa_letras(matriz,palabras):
# Recorrer todas las filas en busca de esas palabras
    solucion = {}
    for palabra in palabras:
        # FILAS y COLUMNAS
        # ----------------
        #buscamos en las filas y columnas
        for i in range(len(matriz)):
            fila = devuelve_fila(matriz,i)
            columna = devuelve_columna(matriz,i)
            estaf = fila.find(palabra)
            estac = columna.find(palabra)
            if estaf != -1:
                solucion[i,estaf]=palabra
            elif estac !=-1:
                solucion[i,estac]=palabra
            # DIAGONALES
            # ----------
            #lanzo otro bucle para que llame a devolver_doagonal por cada celda
            for j in range(len(matriz)):
                diagonal = devuelve_diagonal(matriz,i,j)
                estad = diagonal.find(palabra)
                if estad != -1:
                    solucion[i,j] = palabra
    return solucion

print(sopa_letras([['h','o','l','a'],
                   ['o','a','p','b'],
                   ['c','l','k','c'],
                   ['f','h','a','e']],['hola',"ola"]))