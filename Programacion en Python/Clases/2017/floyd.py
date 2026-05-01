
ultimo = 1 
numNiveles = int( input() ) 
for nivel in range(1, numNiveles+1): 
    for numero in range(1,nivel+1): 
        print( ultimo , " " , end=' ')
        ultimo += 1 
    print(" ") 