def rpn_to_algebraic(s):
    operadores = ["-", "+", "*"]
    s = s.split(" ")
    lista = []
    for i in s:
        if i not in operadores:
            lista.append(i)
        else:
            B = lista.pop()
            A = lista.pop()
            lista.append("(" + A +" "+i+" "+ B + ")")
    return lista.pop()


print(rpn_to_algebraic('12 3 - 2 5 * +'), '((12 - 3) + (2 * 5))')
print(rpn_to_algebraic('1 2 3 4 - - -'), '(1 - (2 - (3 - 4)))')
print(rpn_to_algebraic('1 2 - 3 - 4 -'), '(((1 - 2) - 3) - 4)')
print(rpn_to_algebraic('1'), '1')