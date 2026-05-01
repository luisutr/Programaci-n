def es_primo(n):
    if n<2:
        return False
    for  i in range(2,n):
        if n%i == 0:
            return False
    return True
'''
Resolver goldbbatch: buscamos un primo, restamos ese primo al numero y si el resultado es primo --> 
hemos encontrado los dos Primos que suman el numero par > de 2 
'''
def thonsand (n): #Generar varios números primos y devolver una lista de números primos
    a = []
    for i in range(1,n+1):
        if es_primo(i):
            a.append(i)
    return a

print(thonsand(50))

'''Utilice las dos funciones anteriores para generar una lista de números primos en el rango de n
 Bucle for de dos capas, si la suma de las dos variables de iteración es igual al parámetro n, agréguelo a la lista
 Después de recorrer todas las situaciones, regrese a la lista e imprima.'''

def goldbatch_iterativo(n):
    if n%2 == 0 and n >2:
        for a in range(2,n):
            if es_primo(a):
                b = n - a
                if es_primo(b):
                    if a<=b: # para que no se repitan numeros primos
                        print("Primos", a, b)
    else:
        print("No es un numero valido")

def goldbatch_recursivo(pNumero, primos = thonsand(50), i=0, sol=[]):
    if pNumero%2== 0 and pNumero > 2 and i<len(primos):
            a = primos[i]
            b = pNumero - a
            if es_primo(b):
                if a <= b:  # para que no se repitan numeros primos
                    sol.append(("Primos", a, b))
            else:
                goldbatch_recursivo(pNumero, primos,  i+1, sol)
    return sol

print(goldbatch_recursivo(44))