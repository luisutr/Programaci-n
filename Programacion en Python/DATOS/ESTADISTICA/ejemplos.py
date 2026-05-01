import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#Ejemplo: ¿Cuántos alumnos han sacado un 5 en el examen?
df = pd.read_csv("notas.csv")
# Generar tabla de frecuencias
tab = pd.crosstab(index=df["nota"],columns="frecuencia")
print(tab)

# Buscar el elemento 5 (el elemento que cumple la condición de que su índice es igual a 5)
fila = tab.loc[tab.index == 5]
# Obtenemos el valor "frecuencia" de la fila
x = fila["frecuencia"]
x = int(x)
print("%d alumnos han sacado un 5" % x)

#¿Cuántos alumnos han aprobado (sacar 5 o más)?
fila = tab.loc[tab.index >= 5]
x = fila["frecuencia"].sum()
x = int(x)
print("%d alumnos han aprobado el examen" % x)

#Haz un diagrama de sectores donde se vea claramente el porcentaje de aprobados frente al de suspensos
aprobados = tab.loc[tab.index >= 5]["frecuencia"].sum()
suspensos = tab.loc[tab.index < 5]["frecuencia"].sum()
data = np.array([aprobados,suspensos])
plt.pie(data,labels=["Aprobados","Suspensos"],autopct="%1.1f%%")
plt.xlabel("Notas del examen")
plt.savefig("aprobados.png")

'''
# Datos
x = ["A", "B", "C"]
y = [3, 5, 1]

# Gráfico de barras
fig, ax = plt.subplots()
ax.bar(x = x, height = y)
# plt.show()
'''
fig, ax = plt.subplots()
ax.bar(x = tab.index,height = tab["frecuencia"])
plt.xlabel("Notas del examen")
plt.savefig("barras.png")