def sortedDictValues1(adict):
    dicorden={}
    lista = sorted(adict.items())
    for i in lista:
        dicorden[i[0]]=i[1]
    return dicorden

x={"a":2, "b":3, "d":1, "c":1}

print(sortedDictValues1(x))

