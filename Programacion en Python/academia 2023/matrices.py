#   0 1 2
m=[[1,2,3], #0
   [4,5,6], #1
   [7,8,9]] #2


print(m[0])
fila = m[0]
print(fila)
print(fila[0])
print(m[0][0])
print(m[1][1])
print(m[2][2])

def diagonalprin():
    diagonal=[]
    for i in range(len(m)):
        diagonal.append(m[i][i])
    return diagonal
def columna(n):
    columna =[]
    for i in range(len(m)):
        columna.append(m[i][n])
    return columna
def fila(n):
    fila = []
    for i in range(len(m)):
        fila.append(m[n][i])
    return fila

def diagmovidaizq(matriz,nfila,ncolumna):
  diagonal=[]
  for i in range(nfila,len(matriz)):
    diagonal.append(matriz[i][len(matriz)-i])
  return diagonal

#print(diagmovidaizq([[1,2,3,4], [4,5,6,7], [7,8,9,0], [1,2,3,4]],0,2))

mnum=[[2,3,6],
      [1,5,7],
      [4,8,9]]
print(mnum[1:][1])
def paresmatrix(mnum):
    resul=[]
    for fila in mnum:
        for num in fila:
            if num%2==0:
                resul.append(num)
    return resul
print(paresmatrix(mnum))

L=[[1,2,3,4],[2,3,5,6],[3,4,6,7],[4,5,7,8]]
#    0,    1,    2,   3

print("manejo de matrices "+str(L[1][0]))

def mitadderechamatriz(m):
    for fila in m:
        print(fila[2:])
mitadderechamatriz(L)

def mitadderechamatrizconrage(m):
    for i in range(len(m)):
        print(m[i][2:])
mitadderechamatrizconrage(L)

for fila in L:
    for i in fila:
        if i%2==0:
            print(i)

L2 = [1,2,[2,3,4],5]
for fila in L2:
    if type(fila)==list:
        for i in fila:
            if i%2==0:
                print(i)



#   0 1 2
m=[[1,0,0], #0
   [4,0,6], #1
   [0,0,0]] #2


print(sum(m[1]))

suma=0
for i in range(len(m)):
    suma+=m[i][2]
print(suma)

def fila_mas_ceros(m):
    filaceros=0
    filamasceros = 0
    ganadora=0
    for numfila in range(len(m)):
        contador = 0
        for i in m[numfila]:
            if i == 0:
                contador+=1
        if filamasceros < contador:
            filamasceros = contador
            ganadora=numfila
    return ganadora

print(fila_mas_ceros(m))

