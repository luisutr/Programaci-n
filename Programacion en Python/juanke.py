###You have an array of numbers.
###Your task is to sort ascending odd numbers but even numbers must be on their places.

###Zero isn't an odd number and you don't need to move it. If you have an empty array, you need to return it.

###Example

###sortArray([5, 3, 2, 8, 1, 4]) == [1, 3, 2, 8, 5, 4]

def sort_array(source_array):
    ordenada=[]
    orden=sorted(source_array)
    for i in source_array:
        if i%2==0:
            ordenada.append(i)
        if i%2!=0:
            ordenada.append(impares(source_array))
    return ordenada
def impares(source_array):
    odd=[]
    for j in source_array:
        if j%2!=0:
            odd.append(j)
    return sorted(odd)

###esto es lo que he conseguido,y me sale este resultado:
###[[1, 3, 5], [1, 3, 5], 2, 8, [1, 3, 5], 4]
###pero no consigo ver como hacerlo, a ver si puedes ayudarme. gracias!

### Por lo que veo es mas facil solo hay que cambiar las posiciones de los numeros cuando
###coinciden con sus valores cambiados (emepzamos por 1 no por 0). ejempl
###[5, 3, 2, 8, 1, 4]
### 1           5
###[1, 3, 2, 8, 5, 4]
def sort_array(source_array):
    try:
        for i in range(len(source_array)):
            num1 = source_array[source_array[i]-1]
            num2 = source_array[i]
            if num2 < len(source_array)+1 and num1 == i+1:
                source_array[source_array[i]-1] = num2
                source_array[i] = num1
    except Exception:
        pass
    return source_array

print sort_array([5, 3, 2, 8, 1, 4])
