"""original number =2997 , n=3
2997 = 222+999+999+777"""

def ConcatenatedSum(sum,n):
    return 0

ConcatenatedSum(2997,3)
ConcatenatedSum(-2997,3)



"""For k = 6 and elements = [6, 4, 10, 10, 6], the output should be splitByValue(k, elements) = [4, 6, 10, 10, 6].

For k = 5 and elements = [1, 3, 5, 7, 6, 4, 2], the output should be splitByValue(k, elements) = [1, 3, 4, 2, 5, 7, 6].
Remplaza a partir del numero los menores que queden, luego mete el numero y los que ya sean mayores"""


"""hacemos un split, metemos la primera lista, de la segunda, solo los que sean menores y vamos haceiendo pop para elimnarlos de esta
luego metemos el numero en cuestion y luego la lista despues de haber hecho los pop"""


"""
          a
         b c
        a b c
       a b c a
      b c a b c
     a b c a b c
    a b c a b c a
   b c a b c a b c
  a b c a b c a b a
 b c a b c a b a b c
a b c a b a b c a b c
. . . . . . . . . . .
. . . . . . . . . . .
. . . . . . . . . . .
. . . . . . . . . . .
          |
          |
          .
          .
          
          a

          b  

          a    

          a        

          b        

          a          
          .

          .

          .

El centro es: abaabaabaabaaba......

Generamos listas desde 1 elemento hasta  19 que forman el arbol y de ahi sacamos su centro

"""
