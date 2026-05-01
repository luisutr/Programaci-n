import random
def suma_100():
    global solved
    suma_100.prev_soln = []
    opers = ['+', '-', '']
    sumacien = ('%s'.join('123456789') % (random.choice(opers),
                                     random.choice(opers),
                                     random.choice(opers),
                                     random.choice(opers),
                                     random.choice(opers),
                                     random.choice(opers),
                                     random.choice(opers),
                                     random.choice(opers),
                                     )
             )
    if eval(sumacien) == 100:
        if sumacien not in suma_100.prev_soln:
            solved += 1
            suma_100.prev_soln.append(sumacien)
            print "Solution:", sumacien, "= 100     :-)"
            print cadena100alista(sumacien)
    else:
        pass

def cadena100alista(sumacien):
    lista=[]
    aux=""
    signo=1
    for i in sumacien:
        if i in ['1','2','3','4','5','6','7','8','9']:
            aux += i
            if i == '9':
                num=int(aux)*signo
                lista.append(num)
        elif i == '-':
            num=int(aux)*signo
            lista.append(num)
            aux=''
            signo=-1
        elif i=='+':
            num=int(aux)*signo
            lista.append(num)
            aux=''
            signo=1
    return lista


solved = 0
while solved < 2:
    suma_100()