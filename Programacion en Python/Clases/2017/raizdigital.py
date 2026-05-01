__author__ = 'Luis'

def digital_root(n):
    raiz_d = 0
    for i in str(n):
        raiz_d += int(i)
    if len(str(raiz_d)) > 1:
        return digital_root(raiz_d)
    else:
        return raiz_d




print digital_root(493193)
