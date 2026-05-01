import matplotlib.pyplot as plt
import networkx as nx
import graph as g
import os

os.system('cls')

source = [1,2,2,2,3,4]
target = [2,1,3,4,4,3]
weight = [1,1,2,4,1,1]

G = g.graph()
G.create_network(source, target, weight)
print("Dijkstra\n")

G.dijkstra()
G.print_distances()

def floyd_warshall(self):
    nodes = list(self.graph.nodes)
    print(nodes)
    for i in nodes:
        dict_i = {}
        for j in nodes:
            if i == j:
                dict_i[j] = 0
                continue
            try:
                dict_i[j] = self.graph[i][j]['weight']
            except:
                dict_i[j] = float("inf")

        self.distances[i] = dict_i

    for i in nodes:
        for j in nodes:
            for k in nodes:
                ij = self.distances[i][j]
                ik = self.distances[i][k]
                kj = self.distances[k][j]

                if ij > ik + kj:
                    self.distances[i][j] = ik + kj

    return self.distances

