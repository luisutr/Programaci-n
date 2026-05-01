def infected_zeroes2(lst):
    if sum(lst)==0:
        return 0
    count=1
    if lst[len(lst)-1] == 0:
        lst[len(lst)-2] = 0
    if lst[0] == 0:
        lst[1] = 0
    while sum(lst)!=0:
        for i in range(1,len(lst)-1):
            if i < len(lst):
                if lst[i]==0:
                    lst[i-1]=0
                    lst[i+1]=0
        count+=1
    return count

def infected_zeroes(lista):
    cadena=""
    for i in lista:
        cadena+=str(i)
    return cadena.split("0")


print infected_zeroes([0])
print infected_zeroes([0,1,1,0])
print infected_zeroes([0,1,1,1,0])
print infected_zeroes([1,1,0,1,1])
print infected_zeroes([0,1,1,1])
