def rpn_to_algebraic(s):
    operadores = ["-", "+", "*"]
    s = s.split(" ")
    listanumeros = []
    for i in s:
        if i not in operadores:
            listanumeros.append(i)
        else:
            B = listanumeros.pop()
            A = listanumeros.pop()
            listanumeros.append("(" + A +" "+i+" "+ B + ")")
    return listanumeros.pop()


print(rpn_to_algebraic('12 3 - 2 5 * +'), '((12 - 3) + (2 * 5))')
print(rpn_to_algebraic('1 2 3 4 - - -'), '(1 - (2 - (3 - 4)))')
print(rpn_to_algebraic('1 2 - 3 - 4 -'), '(((1 - 2) - 3) - 4)')
print(rpn_to_algebraic('1'), '1')