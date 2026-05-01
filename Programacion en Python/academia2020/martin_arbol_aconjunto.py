def arbol_a_conjunto(A):
    return set(arbol_a_lista(A, []))
def arbol_a_lista(A, conjunto):
    if A == None: 
        return set()   
    v, ramaL, ramaR = A
    if type(v)==list:
        arbol_a_lista(v, conjunto)
    elif type(v)==int:
        conjunto.append(v)
    if type(ramaL)==tuple:
        arbol_a_lista(ramaL, conjunto)
    elif type(ramaL)==int:
        conjunto.append(ramaL)
    if type(ramaR)==tuple:
        arbol_a_lista(ramaR, conjunto)
    elif type(ramaR)==int:
        conjunto.append(ramaR)
    return conjunto

print(arbol_a_conjunto(None), set())
print(arbol_a_conjunto((5,None,None)), {5})
print(arbol_a_conjunto((3, (1, None, None), (8, (5, None, None), (13, (9, None, None), None)))),                         {3,8,1,13,5,9})
print(arbol_a_conjunto((4, (3, (2, (1, (0, None, None), None), None), None), None)),{0,1,2,3,4})