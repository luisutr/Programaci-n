def valores(solucion):
    a = str(solucion.pop())
    b = str(solucion.pop())
    return a,b

def rpn_to_algebraic(s):
    solucion=[]
    signos=['/','*','-','+']
    for i in s.split():
        if i not in signos:
            solucion.append(i)
        else:
            a,b = valores(solucion)
            solucion.append(str('('+b+' '+i+' '+a+')'))
    return solucion[0]

print(rpn_to_algebraic('12 3 - 2 5 * +'))#((12 - 3) + (2 * 5))'
print(rpn_to_algebraic('1 2 3 4 - - -'))#, '(1 - (2 - (3 - 4)))')
print(rpn_to_algebraic('1 2 - 3 - 4 -'))#, '(((1 - 2) - 3) - 4)')
print(rpn_to_algebraic('1'))#, '1')

myList = [ x if x%2 else x*100 for x in range(1, 10) ]
