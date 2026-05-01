dicc = {}

#key y value pueden ser cualquier variable int, string, float, list, dicc, tuplas... objetos dicc
dicc[1]="Zaida"
dicc[2]="Alberto"
dicc[3]="Luis"

print(dicc.keys())
print(dicc.values())
print(len(dicc))
print(max(dicc.keys()))
print(sum(dicc.keys()))

# reccorer diccionario

for clave, valor in dicc.items():
    print(clave)
    print(valor)

print(dicc)