def rpn_to_algebraic(s):
    algebraic=[]
    for i in s.split():
        if i in ['+','-','*','/']:
            a = str(algebraic.pop())
            b = str(algebraic.pop())
            algebraic.append(str('(' + str(b) + ' ' + i + ' ' + str(a) + ')'))
        else:
            algebraic.append(str(int(i)))
    return algebraic[0]


print(rpn_to_algebraic('12 3 - 2 5 * +'))#((12 - 3) + (2 * 5))'
print(rpn_to_algebraic('1 2 3 4 - - -'))#, '(1 - (2 - (3 - 4)))')
print(rpn_to_algebraic('1 2 - 3 - 4 -'))#, '(((1 - 2) - 3) - 4)')
print(rpn_to_algebraic('1'))#, '1')
