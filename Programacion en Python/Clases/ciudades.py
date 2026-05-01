def superMinero(mystr):
    contador = 0
    diamantes = 0
    for ch in mystr:
        if ch == '<':
            contador += 1
        if ch == '>' and contador > 0:
            contador -= 1
            diamantes += 1
    return diamantes



def superMinero2(mystr):
    mina_escavada = mystr[mystr.find('<'):mystr.rfind('>')]
    d_abiertos = mina_escavada.count('<')
    d_cerrados = mina_escavada.count('>')
    return d_abiertos if d_abiertos <= d_cerrados else d_cerrados


print superMinero('>><>>><<><')

print superMinero2('>><>>><<><')