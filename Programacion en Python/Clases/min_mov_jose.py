__author__ = 'luis'


movimientos = 0
def minimov_recu(n,movimientos):
    if n%2==0 and n>1:
        movimientos+=1
        n=n/2
    if n%2!=0 and n>1:
        n=n-1
        movimientos+=1
    if n == 1:
        return movimientos
    else:
        return minimov_recu(n,movimientos)

def minimov(n):
    return minimov_recu(n,0)

print minimov(200)