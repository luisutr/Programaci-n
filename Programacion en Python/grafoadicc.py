G=[[1,2,2],[2,3,1],[2,4,1],[3,1,2]]

def degrafoadicc(G):
    dicc={}
    for i in G:
        o,d,p=i
        if o in dicc.keys():
            dicc[o].append((d,p))
        else:
            dicc[o]=[(d,p)]
    return dicc

print(degrafoadicc(G))
