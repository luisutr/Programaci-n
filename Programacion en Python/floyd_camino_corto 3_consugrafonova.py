# -*- coding: utf-8 -*-
'''
Teoria necesaria de iteraciones
-------------------------------

count(10)                               --> 10 11 12 13 14 ...
cycle('ABCD')                           --> A B C D A B C D ...
repeat(10, 3)                           --> 10 10 10

product('ABCD', repeat=2)	 	            AA AB AC AD BA BB BC BD CA CB CC CD DA DB DC DD
permutations('ABCD', 2)	 	                AB AC AD BA BC BD CA CB CD DA DB DC
combinations('ABCD', 2)	 	                AB AC AD BC BD CD
combinations_with_replacement('ABCD', 2)	AA AB AC AD BB BC BD CC CD DD

chain('ABC', 'DEF')                         --> A B C D E F
compress('ABCDEF', [1,0,1,0,1,1])           --> A C E F
dropwhile(lambda x: x<5, [1,4,6,4,1])       --> 6 4 1
ifilter(lambda x: x%2, range(10))           --> 1 3 5 7 9
ifilterfalse(lambda x: x%2, range(10))      --> 0 2 4 6 8
islice('ABCDEFG', 2, None)                  --> C D E F G
imap(pow, (2,3,10), (5,2,3))                --> 32 9 1000
starmap(pow, [(2,5), (3,2), (10,3)])        --> 32 9 1000
 
takewhile(lambda x: x<5, [1,4,6,4,1])       --> 1 4
izip('ABCD', 'xy') --> Ax By
izip_longest('ABCD', 'xy', fillvalue='-')   --> Ax By C- D-


Example
pair     dist    path
1 -> 2    -1     1 -> 3 -> 4 -> 2
1 -> 3    -2     1 -> 3
1 -> 4     0     1 -> 3 -> 4
2 -> 1     4     2 -> 1
2 -> 3     2     2 -> 1 -> 3
2 -> 4     4     2 -> 1 -> 3 -> 4
3 -> 1     5     3 -> 4 -> 2 -> 1
3 -> 2     1     3 -> 4 -> 2
3 -> 4     2     3 -> 4
4 -> 1     3     4 -> 2 -> 1
4 -> 2    -1     4 -> 2
4 -> 3     1     4 -> 2 -> 1 -> 3
'''

from math import inf
from itertools import product


def floyd_warshall(n, edge):
    dicc={}
    rn = range(n)
    dist = [[inf] * n for i in rn]
    nxt = [[0] * n for i in rn]
    for i in rn:
        dist[i][i] = 0
    for u, v, w in edge:
        dist[u - 1][v - 1] = w
        nxt[u - 1][v - 1] = v - 1
    for k, i, j in product(rn, repeat=3):
        sum_ik_kj = dist[i][k] + dist[k][j]
        if dist[i][j] > sum_ik_kj:
            dist[i][j] = sum_ik_kj
            nxt[i][j] = nxt[i][k]
    print("pair     dist    path")
    for i, j in product(rn, repeat=2):
        if i != j:
            path = [i]
            while path[-1] != j:
                path.append(nxt[path[-1]][j])
            print("%d → %d  %4d       %s"% (i + 1, j + 1, dist[i][j],' → '.join(str(p + 1) for p in path)))
            dicc[(i + 1, j + 1)]=dist[i][j]
    return (dicc)


#print(floyd_warshall(4, [[1, 3, -2], [2, 1, 4], [2, 3, 3], [3, 4, 2], [4, 2, -1]]))


G = [[1, 3, -2], [2, 1, 4], [2, 3, 3], [3, 4, 2], [4, 2, -1]]

def distancia(i,j,G):
    #n = numero de vertices del grafo
    dG=floyd_warshall(4,G)
    dismin=99
    for nodo, distancia in dG.items():
        if (i,j) == nodo:
            if distancia < dismin:
                dismin = distancia
                elegido = nodo

    #print (p)
    #print (w)
    return elegido, dismin


print(distancia(3,4,G))
#print(distancia(2,4,G))
#print(distancia(2,3,G))
#print(distancia(0,2,G2))



#OTRA OPCION
# Python Program for Floyd Warshall Algorithm

# Number of vertices in the graph
V = 4

# Define infinity as the large enough value. This value will be
# used for vertices not connected to each other
INF = 99999

'''para python 2.7
# Solves all pair shortest path via Floyd Warshall Algorithm
def floydWarshall(graph):
    """ dist[][] will be the output matrix that will finally
        have the shortest distances between every pair of vertices """
    """ initializing the solution matrix same as input graph matrix 
    OR we can say that the initial values of shortest distances 
    are based on shortest paths considering no  
    intermediate vertices """
    dist = map(lambda i: map(lambda j: j, i), graph)

    """ Add all vertices one by one to the set of intermediate 
     vertices. 
     ---> Before start of an iteration, we have shortest distances 
     between all pairs of vertices such that the shortest 
     distances consider only the vertices in the set  
    {0, 1, 2, .. k-1} as intermediate vertices. 
      ----> After the end of a iteration, vertex no. k is 
     added to the set of intermediate vertices and the  
    set becomes {0, 1, 2, .. k} 
    """
    for k in range(V):

        # pick all vertices as source one by one
        for i in range(V):

            # Pick all vertices as destination for the
            # above picked source
            for j in range(V):
                # If vertex k is on the shortest path from
                # i to j, then update the value of dist[i][j]
                dist[i][j] = min(dist[i][j],dist[i][k] + dist[k][j])
    printSolution(dist)

#siendo en este caso graph una matriz de pesos. Con lo cual habría que haber convertido a patriz de pesos el grafo

# A utility function to print the solution
def printSolution(dist):
    print ("Following matrix shows the shortest distances\
    between every pair of vertices")
    for i in range(V):
        for j in range(V):
            if (dist[i][j] == INF):
                print("%7s" % ("INF")),
            else:
                print("%7d\t" % (dist[i][j])),
            if j == V - 1:
                print("")

        # Driver program to test the above program
# Let us create the following weighted graph
""" 
            10 
       (0)------->(3) 
        |         /|\ 
      5 |          | 
        |          | 1 
       \|/         | 
       (1)------->(2) 
            3           """
graph = [[0, 5, INF, 10],
         [INF, 0, 3, INF],
         [INF, INF, 0, 1],
         [INF, INF, INF, 0]
         ]
# Print the solution
floydWarshall(graph)
# This code is contributed by Nikhil Kumar Singh(nickzuck_007)
'''
