def pasillopersonas(pasillo):
    listaperson = []
    pasos = 0
    persona = False
    for i in pasillo:
        if i == ">":
            persona=True
        elif i == "<":
            listaperson.append(pasos)
            persona=False
            pasos=0
        if persona==True:
            pasos += 1
    if min(listaperson) == 0:
        return -1
    if min(listaperson)==1:
        return 1
    return min(listaperson)-1


print(pasillopersonas('---><---'), 1)
print(pasillopersonas('--->-<------->----<-'), 1)
print(pasillopersonas('----<----->----'), -1)
print(pasillopersonas('>-----<-->--<-----'), 2)
print(pasillopersonas('>>-----<<'), 3)
print(pasillopersonas('---><---'), 1)


if "dog" in "caca cat":
    print("si")