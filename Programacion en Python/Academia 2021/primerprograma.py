def bulcefor(n):
    x = int(input("Dame un numero: "))
    rep = 0
    if n > x:
        rep = n-x
    concatena = ""
    for i in range(rep):
        concatena += str(i)
    return concatena


print(bulcefor(9))