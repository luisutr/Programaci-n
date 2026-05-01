'''void loop{
    int v[tam][tam],t[tam][tam];
    v = rellenaMatriz(tam);
    t = rellenaMatriz(tam);
    traspuesta(v,t)
    serial.print(t)
}
void traspuesta(int v2[tam][tam], int t2[tam][tam]){
    ....
}
'''
def prin():
    a=[1,2,3]
    b = a
    otra(b)
    print(a)
    print(b)

def otra(x):   # x = b
    x.pop()
    x.append(4)

prin()

a = [1,2,3]
#quiero hacerme una copia independiente de a en b
b=[]
for i in a:
    b.append(i)
b.pop()
b.append(5)
print(a)
print(b)

c = 5
d = c
d = 7

print(c)
print(d)
'''
3 = 1x2x3       1-3
4 = 1x2x3x4     1-4
5 = 1x2x3x4x5   1-5
n = 1-n

fact=1;
for (int i = 1; i<=n;i ++){
    fact*=i
}
'''