def calculaCollatzIterativo(pNumero):
    while pNumero > 1:
        print('Numero actual: {0}'.format(pNumero))

        if pNumero % 2 == 0:
            pNumero = pNumero // 2

        else:
            pNumero = pNumero * 3 + 1
    else:
        print('Numero actual: {0}'.format(pNumero))


def calculaCollatz(pNumero):
    print('Numero actual: {0}'.format(pNumero))

    if pNumero != 1:
        if pNumero % 2 == 0:
            pNumero = pNumero // 2
        else:
            pNumero = pNumero * 3 + 1
        calculaCollatz(pNumero)

print(calculaCollatz(6))