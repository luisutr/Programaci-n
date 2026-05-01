def op(code):
    op_tab = ['', '+', '-']
    return op_tab[code]


def get(num, i):
    temp = num
    while i != 0:
        k = temp // 3  # division con redondeo resultado = 3, no 3.3333
        if k == 0:
            return op(temp)
        else:
            temp = k
            i -= 1
    return op(temp % 3)


def suma100():
    result = []
    i = 0
    the_number = "123456789"
    while True:
        t, j = "", 0
        while j < 8:
            t += (the_number[j] + get(i, j))
            j += 1
        t += the_number[8]
        i += 1
        if eval(t) == 100:
            i = 0
            t += "*"
            while (i <= len(t)):
                if t[i] == "*":
                    return result
                if t[i + 1] == "+" or t[i + 1] == "-":
                    result.append(int(t[i]))
                    i = i + 1
                elif t[i] == "+":
                    result = result
                    i = i + 1
                elif t[i] == "-":
                    result.append(int(t[i] + t[i + 1]))
                    i = i + 2
                elif t[i + 1] != "*":
                    result.append(int(t[i] + t[i + 1]))
                    i = i + 2
                else:
                    result.append(int(t[i]))
                    i = i + 1

            return t, result


print suma100()
