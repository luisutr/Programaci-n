__author__ = 'luisutrilla'
import random

def exitste(cubo,valor):
    for i in range(len(cubo)):
        for j in range(len(cubo[i])):
            if cubo[i][j] == valor:
                return True
    return False

def comprobartriangulo(l1,l2,l3):

    print l1,l2,l3
    if sum(l1)+l2[2] == 20 and sum(l1)+l2[2] == sum(l2)+l3[0] and sum(l2)+l3[0] == sum(l3)+l1[0]:
        return True
    else:
        return False

def iniciocubo():
    cubo=[]
    subcobo1=[]
    subcobo2=[]
    subcobo3=[]
    for i in range(3):
        for j in range(3):
            if i == 0:
                subcobo1.append(0)
            if i == 1:
                subcobo2.append(0)
            if i == 2:
                subcobo3.append(0)
        if i == 0:
            cubo.append(subcobo1)
        if i == 1:
            cubo.append(subcobo2)
        if i == 2:
            cubo.append(subcobo3)
    return cubo


def triangulo():
    l1=[]
    l2=[]
    l3=[]
    trian=iniciocubo()
    for i in range(3):
        for j in range(3):
            valor = random.randint(0,9)
            var=exitste(trian,valor)
            while var==True:
                    valor = random.randint(0,9)
                    var=exitste(trian,valor)
            trian[i][j]=valor
            print(trian)
    for i in range(len(trian)):
        sub = trian[i]
        for j in range(len(sub)):
            if i == 0:
                l1.append(sub[j])
            if i == 1:
                l2.append(sub[j])
            if i == 2:
                l3.append(sub[j])
    while comprobartriangulo(l1,l2,l3)== False:
        print trian, sum(l1)+l2[2], sum(l2)+l3[0], sum(l3)+l1[0]
        if "si" == raw_input("Qieres seguir:"):
            triangulo()
        else:
            return "Ha salido"
    return trian



print(triangulo())