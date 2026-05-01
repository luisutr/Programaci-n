def convierteacadena(comun):
    return ''.join(map(str, comun))

def creacadena(i,comun,listaA,listaB):
    if i in listaA:
        if i in comun:
            if listaA.count(i) >= listaB.count(i):
                comun.append(i)
        else:
            comun.append(i)
    return comun

def lcs(a,b):
    listaA=list(a)
    listaB=list(b)
    comun=[]
    for i in listaB:
        comun = creacadena(i,comun,listaA,listaB)
    return convierteacadena(comun)

print(lcs("abcde" , "cde"))
print(lcs("abcde","aBcDe"))
print(lcs("ababcbcde", "abbccdde"))