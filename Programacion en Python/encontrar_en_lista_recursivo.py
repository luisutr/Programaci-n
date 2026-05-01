def esta(elem, lista):
    if lista == []:
        return False
    if elem == lista[0]:
        return True
    else:
        return esta(elem, lista[1:])


print (esta(2,[3,5,6,7,8,9,2,0]))
