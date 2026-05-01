__author__ = 'Luis'

def persistence(n):
    if len(str(n))==1:
        return 0
    persistencia = 1
    for i in str(n):
        persistencia *= int(i)
    if len(str(persistencia)) > 1:
        return persistence(persistencia)
    else:
        return persistencia, persistencia_num

print persistence(999)

