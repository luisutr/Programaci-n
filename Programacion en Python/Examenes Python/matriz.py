
def traza(m):
    return sum([m[i][i] for i in range(len(m))])

print traza([[1,2,3],[4,5,6],[7,8,9]])
print traza([[1,0,0],[0,1,0],[0,0,1]])