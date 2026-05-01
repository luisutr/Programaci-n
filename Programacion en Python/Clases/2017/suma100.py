__author__ = 'luisutrilla'


def kum(nsplit, nelems, j, split):
        if nsplit == 0:
            kum.accum += [split]
            return
        for i in range(j, nelems):
            kum(nsplit - 1, nelems, i+1, split + [i])

def amy_wants_my_willy(s, n):
    kum.accum = []
    kum(n, len(s), 1, [])
    for split in kum.accum:
        lst, last = [], 0
        for i in range(n):
            lst += [s[last:split[i]]]
            last = split[i]
        lst += [s[last:]]
        yield lst

def suma_100():
     global solved
     prev_soln = []
     for lst in amy_wants_my_willy('123456789', 3):
        for fmt in ['%s-%s+%s-%s', '%s-%s-%s+%s', '%s+%s-%s-%s']:
            exp = fmt % tuple(lst)
            sum = eval(exp)
            if sum == 100:
                solved += 1
                prev_soln.append(exp)
                print (exp + ' = %d') % sum
                print cadena100alista(exp)
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