
# coding: utf-8

# # Analizando un poco la data 
# 
# 

# In[1]:


#import all libraries!
import pandas as pd # el as pd es un alias, hace el codigo un poco mas corto


# In[2]:


#importemos (carguemos en memoria) la data
#pandas carga la data como un dataframe o matriz, tal como si tuvieramos un spreadsheet

data = pd.read_csv('data/titanic.csv')

#previsualicemos la data
data.head()


# In[3]:


#cual es la dimension (filas, columnas) de mi dataframe?
print (data.shape)


# In[4]:


# Tengo datos completos para todos los registros?
# el metodo count cuanto cada registro(fila) que tenga datos
# podemos ver que por ejemplo para la columna Cabin tengo algunos registros sin datos
print (data.count())


# In[5]:


# Pero tener datos, no significa tener datos "limpios"
# Podemos ver en la previsualizacion que para la columna Cabin tengo algunos NaN, el cual en python 
# es interpretado como un valor nulo o Null, lo cual me podria traer problemas cuando analice la data
# contemos cuantos datos nulos tenemos

# 1. Obtener los nombres de las columnas como una lista
col_names = data.columns.tolist()
# 2. Iterar sobre la lista
for column in col_names:
    print ("Valores nulos en <{0}>: {1}".format(column, data[column].isnull().sum()))


# In[6]:


# Imagina que para fines de simplicidad quieres reemplazar el female, male por F, M

# 1. Creamos un diccionario con los valores originales y los valores de reemplazo
d = {'male' : 'M', 'female' : 'F'}

# 2. Utilizamos un lambda para el reemplazo, en una sola linea n.n
data['Sex'] = data['Sex'].apply(lambda x:d[x])

#checa el cambio
data['Sex'].head()


# In[ ]:


#Una forma mas sencilla de acceder a las columnas
data.Age


# In[ ]:


# Podemos dar un vistazo a la distribucion de los datos
data.describe()


# In[ ]:


# Vemos que el minimo en Fare (precio) es 0 
# Cuantos no pagaron?
data[data.Fare == 0]


# In[7]:


# Agrupemos por Sobrevivencia y Sexo
pd.crosstab(data.Survived, data.Sex)


# In[8]:


#Como fue la sobreviviencia por clase, sexo
pclass_gender_survival_count_df = data.groupby( ['Pclass', 'Sex'] )['Survived'].sum()
pclass_gender_survival_count_df


# # Visualicemos!

# In[ ]:


# Cuantos sobrevivieron 


# In[ ]:


import matplotlib.pyplot as plt

 
fig = plt.figure(figsize=(30,10)) #creamos un canvas o figura de 30x10 pixeles

# queremos ver un plot al costado del otro, para esto pensemos en una grilla (celdas)
plt.subplot2grid((2,3),(0,0))
data.Survived.value_counts().plot(kind='bar', alpha=0.5)
plt.title('Sobrevivieron - cuenta total -')

# Hay manera un poco mas amigable de interpretar datos....con porcentajes!
plt.subplot2grid((2,3),(0,1))
data.Survived.value_counts(normalize = True).plot(kind='bar', alpha=0.5)
plt.title('Sobrevivieron - porcentaje total -')

plt.show()


# In[ ]:


#Sobrevivieron mas hombres o mas mujeres?
fig = plt.figure(figsize=(30,10))
data.Sex[data.Survived == 1].value_counts(normalize = True).plot(kind='barh', alpha=0.5, color='br')
plt.title('Sobrevivieron - Male vs Female -')
plt.show()


# In[ ]:


# Que relacion hay entre sobrevivencia y edad de los sobrevivientes
fig = plt.figure(figsize=(6,8))
plt.scatter(data.Survived, data.Age, alpha=0.5, color='#808000')
plt.show()


# In[ ]:


# La clase del ticket fue un factor de sobrevivencia (si viste Titanic, ya lo sabes!)
fig = plt.figure(figsize=(10,5))
#colors bgrcmykw
data.Pclass[data.Survived == 1 ].value_counts(normalize = True).plot(kind='bar', alpha=0.5, color='rby')
plt.title('Sobrevivientes por Clase de Ticket')
plt.show()


# In[ ]:


# Habra alguna relacion entre tipo de ticket y edad? (Poder Adquisitivo)
fig = plt.figure(figsize=(20,10))

for t_class in [1,2,3]:
    data.Age[data.Pclass == t_class].plot(kind='kde')
    
plt.legend(("1ra. Clase", "2da. Clase", "3ra.Clase"))  
plt.show()

# La linea de la 1ra clase, nos muestra que el promedio de edad del comprador es de 40 annios
# La linea de la 3ra clase, tiene un promedio mucho mas joven

# Podriamos hacer una inferencia temprana y decir que los hombres que salvaron fueron 
# en su mayoria ricos y > 30 annios


# In[ ]:


data[data.Age < 1]

