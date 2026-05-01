def cuartiles(tupla):
    tupla=sorted(tupla)
    if len(tupla) < 4:
        return(q1(tupla), q2(tupla), tupla[-1], tupla[-1])
    return(q1(tupla), q2(tupla), q3(tupla), q4(tupla))

def q1(tupla):
    posicion=(len(tupla)+1)/4
    d = posicion - int(posicion)
    posicion = int(posicion)
    xn=tupla[posicion-1]
    xn_uno=tupla[posicion+1-1]
    percentil = xn+(d*(xn_uno-xn))
    if percentil - int(percentil) == .0:
        return int(percentil)
    return percentil
def q2(tupla):
    n = int(len(tupla) / 2)
    n_uno = int(len(tupla) / 2 + 1)
    xn = tupla[n - 1]
    xnuno = tupla[int(n_uno) - 1]
    mediana = (xn + xnuno) / 2
    if len(tupla)%2==0:
        return mediana
    return tupla[n]
def q3(tupla):
    n = 3*(len(tupla) + 1)/4
    d = n - int(n)
    n = int(n)
    if n >= len(tupla):
        return tupla[-1]
    return tupla[n-1]+d*(tupla[n+1-1]-tupla[n-1])
def q4(tupla):
    return max(tupla)

print(cuartiles((63,34,60,30,45,32,56,40,21,37,54,33,28,53,19,45,28,52,24,29)),
                         (28.25, 35.5, 52.75, 63))
print(cuartiles(range(10)), (1.75, 4.5, 7.25, 9))
print(cuartiles((1,2,3)), (1,2,3,3))
print(cuartiles((1,1,1)), (1,1,1,1))
