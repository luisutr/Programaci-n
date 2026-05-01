# Validar sudokus
def valid_solution(matriz):
  fila = []
  columna = []
  # Recorrer las filas y ver que no se repite ningun numero
  for i in range(len(matriz[0])):
    for j in range(len(matriz[0])):
      if matriz[i][j] in fila or matriz[i][j] == 0:
        return False
      fila.append(matriz[i][j])
    fila = []
  # Recorrer las columnas
  for i in range(len(matriz[0])):
    for j in range(len(matriz[0])):
      if matriz[j][i] in fila or matriz[i][j] == 0:
        return False
      columna.append(matriz[j][i])
    columna = []
  return True


matriz= [[5, 1, 7, 6, 9, 8, 2, 3, 4], [2, 8, 9, 1, 3, 4, 7, 5, 6], [3, 4, 6, 2, 7, 5, 8, 9, 1], [6, 7, 2, 8, 4, 9, 3, 1, 5], [1, 3, 8, 5, 2, 6, 9, 4, 7], [9, 5, 4, 7, 1, 3, 6, 8, 2], [4, 9, 5, 3, 6, 2, 1, 7, 8], [7, 2, 3, 4, 8, 1, 5, 6, 9], [8, 6, 1, 9, 5, 7, 4, 2, 3]]
#print(valid_solution(matriz))

print("++++++++++++++++++++++++++++++")

for x in range(0, 9, 3):
    for y in range(0, 9, 3):
        print(x,y)

def submatrices(matriz):
    submatriz = []
    for x in range(0, 9, 3):
        for y in range(0, 9, 3):
            # x,y es punto de comienzo de submatriz
            # recorro matriz pero solo 3 posiciones
            sub = []
            for fila in range(x, x + 3):
                for columna in range(y, y + 3):
                    sub.append(matriz[fila][columna])
            submatriz.append(sub)
    return submatriz

print(submatrices(matriz))

def resuelvesudoku(matriz):
    if valid_solution(matriz) == False:
        return "No se puede resolver"
    submssss = submatrices(matriz)
    #los elementos de las submatrices estan ahora en la lista subm
    # recorro los elementos y si hay repetidos o uno de ellos es 0
    for subm in submssss:
        for i in subm:
                if subm.count(i)>1 or i == 0:
                    return "No se puede resolver"
    return "Sudoku bueno"

print(resuelvesudoku(matriz))

