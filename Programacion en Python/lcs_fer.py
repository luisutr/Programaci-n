def lcs1(a, b):
    longs=[]
    resultado=''
    if a and b == str(''):
        return str('')
    for i in range(len(a)+1):
        longs.append([0]*(len(b)+1))
    for i in range(len(a)):
        x=a[i]
        for j in range(len(b)):
            y=b[j]
            if x == y:
                longs[i+1][j+1]=longs[i][j]+1
            else:
                longs[i+1][j+1]=max(longs[i+1][j], longs[i][j+1])
    j=len(b)
    for i in range(len(a)+1):
        if longs[i][j] != longs[i - 1][j]:
            resultado += a[i - 1]
    return resultado[1:]

print(lcs1('',''))
print(lcs1('abcde','cde'))
print(lcs1('abcde','aBcDe'))
print(lcs1('ababcbcde','abbccdde'))

