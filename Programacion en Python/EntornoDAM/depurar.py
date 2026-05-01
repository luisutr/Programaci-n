def notas(n):
    if n < 5:
        return "suspenso"
    elif n>=5 and n<6:
        return "suficiente"
    elif n>=6 and n<7:
        return "bien"
    elif n>=7 and n<9:
        return "notable"
    elif n>=9 and n<=10:
        return "sobresaliente"
    return "La nota introducida es erronea"

