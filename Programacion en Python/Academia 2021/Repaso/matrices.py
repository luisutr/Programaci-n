matriz = [[1,2,3],
          [4,5,6],
          [7,8,9]]

matriz = [[1,2,3],[4,5,6],[7,8,9]]
#            0        1       2
#          0,1,2   0,1,2   0,1,2



print(matriz[2][-1])

horizontal = matriz[2]
print(horizontal)

vertical =[]
for x in matriz:
    vertical.append(x[0])

print(vertical)
