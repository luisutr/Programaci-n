def conjuga(verbo):
    sol = []
    raiz = verbo[0:-2]
    termi= verbo[-2:len(verbo)]
    listar = ['o', 'as', 'a', 'amos', 'ais', 'an']
    lister = ['o', 'es', 'e', 'emos', 'eis', 'en']
    listir = ['o', 'es', 'e', 'imos', 'is', 'en']
    if termi == "ar":
        for i in listar:
            sol.append(raiz+i)
    if termi == "er":
        for i in lister:
            sol.append(raiz+i)
    if termi == "ir":
        for i in listir:
            sol.append(raiz+i)
    return sol

