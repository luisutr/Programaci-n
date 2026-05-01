def find_short(s):
    lista = s.split(" ")
    auxlong=len(lista[0])
    for i in lista:
        if auxlong > len(i):
            auxlong=len(i)
    return auxlong

print(find_short("bitcoin take over the world maybe who knows perhaps"))