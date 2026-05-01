
import random
def lanzar_dado(n,m):
    contador=0
    for i in range(n):
        tirada = random.randint(1,6)
        if tirada ==m:
            contador += 1
    return contador

#print(lanzar_dado(20,3))

def num_primo(numero):
    primo = True
    #numero = int(input("Dame un mnumero: "))
    for i in range(2,numero):
        if numero%i == 0:
            primo = False
    return primo


def num_primos_rango():
    N1 = int(input("Dame N1:"))
    N2 = int(input("Dame N2:"))
    texto = ""
    for i in range (N1,N2+1):
        if num_primo(i) == True :
            texto += str(i)+","
    return texto[:-1]

print(num_primos_rango())