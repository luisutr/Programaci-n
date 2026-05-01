def calculadiagonal(m, a, b ):
    long_diag = len(m) - max(a, b)
    diag = ""
    i = 0
    while i < long_diag:
        diag += str(m[a + i][b + i])+","
        i += 1
    return diag[0:-1]

print(calculadiagonal([[1,2,3,4],[5,6,7,8],[8,9,1,2],[4,5,6,7]],1,0))
[1,6,1,7]

m = [
    [2, 4, 2, 6],
    [7, 9, 3, 2],
    [9, 5, 2, 1],
    [1, 3, 6, 3]]

diagoprin=""
for i in range(len(m)):
    diagoprin+=str(m[i][i])+","
print(diagoprin)