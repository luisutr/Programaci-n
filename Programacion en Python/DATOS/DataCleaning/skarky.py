
import pandas as pd

df = pd.read_csv('input/GSAF5.csv', encoding='latin-1', engine='python')
df.head()
#Conocer la base de datos
df.shape

#Conocer cuántos registros nulos hay en cada columna
df.isnull().sum()

#Conocer las columnas
df.columns

#Comprobamos que hay columnas que tienen espacio en el nombre.
#Eliminar el espacio de aquellos con la función str.rstrip()
df.columns = df.columns.str.rstrip()
df.columns

#Seleccionar las columnas necesarias para el estudio de la hipótesis: Case Number, Country, Area, Date, Year, Location, Activity, 'Injury', 'Fatal (Y/N)'
shark_df = df[['Case Number', 'Date', 'Year', 'Country', 'Area', 'Location',
       'Activity', 'Name', 'Sex', 'Age', 'Injury', 'Fatal (Y/N)']]
shark_df.head()

#Revisar si existen duplicados en la columna 'Case Number'
shark_df['Case Number'].duplicated().value_counts()
#Existen 16 'Case Number' duplicados.
#Comprobar si son el mismo caso. Para ser el mismo caso se establece que debe ser misma 'Date', mismo 'Country', misma 'Area' y misma 'Activity'

#shark_df[shark_df['Case Number'].duplicated(keep=False)][['Case Number', 'Date', 'Country', 'Area', 'Activity']]

#Crear una función para que revise si son dos 'Case Number' iguales compruebe los otros campos. Si los campos son iguales, elimina uno de los dos. si los campos son distintos, añade 'x' al final de 'Case Number'. Se añade 'x' porque en el caso de que haya un 'Case Number' similar con una letra, no sea la b o c.

#Filtrar el DataFrame solo por la actividad 'Surfing'
shark_df = shark_df[shark_df.Activity == 'Surfing']
print(shark_df.shape)
print(shark_df.Country.value_counts())

#Pintar una gráfica con los 5 países con mayor registro de ataques por tiburón.
shark_df.Country.value_counts().nlargest(5).plot.pie(labels=['USA', 'AUSTRALIA', 'SOUTH AFRICA', 'BRAZIL', 'REUNION'], fontsize=15, figsize=(6, 6), colors = ('#9dbd00','#66b3ff','#db900d','#ffcc99','#009dbd'), explode=(0.15, 0, 0, 0, 0), title = 'Countries with more shark attacks')
