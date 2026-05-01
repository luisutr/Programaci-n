def sistema_L(e_ini,reglas,it):
    for i in range(it):
        for j in range(len(e_ini)):
            if e_ini[j] == 'F':
                e_ini[j] = reglas['F']
            if e_ini[j] == 'G':
                e_ini[j] = reglas['G']
    return e_ini


print(sistema_L("F-G-G", {'F': "F-G+F+G-F", 'G': "GG"}, 3))


dicc = {'F': "F-G+F+G-F", 'G': "GG"}
print(dicc['F'])