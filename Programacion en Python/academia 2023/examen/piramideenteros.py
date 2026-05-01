def piramide_enteros2(n):
  M=1
  for i in range(1,n):
    for j in range(i,M+1):
      print(j%10,end="")
    for k in range(M-1,i-1,-1):
      print(k%10,end="")
    print()
    M+=2

piramide_enteros2(9)

def sumita(n):
    #34543
    s=""
    for i in range(n,n+n):
        s+=str(i%10)
    for j in range(n+n-2,n-1,-1):
        s += str(j%10)
    return s
#sumita(7)

def piramide_enteros(n):
    for i in range(1,n):
        print(sumita(i))

piramide_enteros(9)

# 34543 --->  si empiza en 3 y TIENE QUE TERMINAR 3, con numeros conscutivos --> 34543




