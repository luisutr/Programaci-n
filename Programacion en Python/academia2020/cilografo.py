# Python program to detect cycle
# in a graph


def anadepunto(u, v):
    graph[u].append(v)

def isCyclicUtil(v, visited, recStack):
        # Mark current node as visited and
        # adds to recursion stack
        visited[v] = True
        recStack[v] = True
        # Recur for all neighbours
        # if any neighbour is visited and in
        # recStack then graph is cyclic
        for neighbour in graph[v]:
            if visited[neighbour] == False:
                if isCyclicUtil(neighbour, visited, recStack) == True:
                    return True
            elif recStack[neighbour] == True:
                return True

        # The node needs to be poped from
        # recursion stack before function ends
        recStack[v] = False
        return False

# Returns true if graph is cyclic else false
def isCyclic(self):
        visited = [False] * self.V
        recStack = [False] * self.V
        for node in range(self.V):
            if visited[node] == False:
                if self.isCyclicUtil(node, visited, recStack) == True:
                    return True
        return False


grafo = ((0, 1), (0, 2), (1, 2), (2, 0), (2, 3), (3, 3))
def tieneciclo(grafo):
    g = {}

    if g.isCyclic() == 1:
        print("Graph has a cycle")
    else:
        print("Graph has no cycle")
