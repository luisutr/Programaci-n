def ercode(img):
    sol = makematriz=(img)
    marca = 0
    for fila in range(len(img)-1):
        if sum(img[fila]) > 3:
            for col in range(len(img)-1):
                if img[fila][col] == 1 and marca == 0:
                    sol[fila+1][col+1]=1
                    marca = 1
    return sol

def makematriz(img):
    sol=[]
    for fil in range(len(img)):
        fila=[]
        for col in range(len(img)):
            fila.append(0)
        sol.append(fila)
    return sol

img = [[0,0,0,0,0,0,0,0,0],
       [0,0,1,1,1,0,0,0,0],
       [0,0,1,1,1,0,0,0,0],
       [0,0,1,1,1,0,0,0,0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0]]
print(ercode(img))