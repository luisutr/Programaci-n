def tiposFOR(l):
    l_s, l_f, l_i, l_otros = [], [], [], []
    for i in l:
        if str(type(i)) == '<class \'int\'>':
            l_i.append(i)
        elif type(i)==type(0.):
            l_f.append(i)
        elif str(type(i))=='<class \'str\'>':
            l_s.append(i)
        else:
            l_otros.append(i)
    return [l_i, l_f, l_s, l_otros]

def tiposWHILE(l):
    l_s, l_f, l_i, l_otros = [], [], [], []
    i = 0
    while i<len(l):
        if str(type(l[i])) == '<class \'int\'>':
            l_i.append(l[i])
        elif type(l[i])==type(0.):
            l_f.append(l[i])
        elif str(type(l[i]))=='<class \'str\'>':
            l_s.append(l[i])
        else:
            l_otros.append(l[i])
        i += 1
    return [l_i, l_f, l_s, l_otros]
    
l = [1,1.,'0','1',2,2.2,[1,2,3]]
print(tiposFOR(l))
print(tiposWHILE(l))

