# Ejemplos de estadistica descriptiva con python
import numpy as np # importando numpy
from scipy import stats # importando scipy.stats
import pandas as pd # importando pandas

np.random.seed(2131982) # para poder replicar el random
datos = np.random.randn(5, 4) # datos normalmente distribuidos
print(datos)

'''array([[ 0.46038022, -1.08942528, -0.62681496, -0.63329028],
       [-0.1074033 , -0.88138082, -0.34466623, -0.28320214],
       [ 0.94051171,  0.86693793,  1.20947882, -0.16894118],
       [-0.12790177, -0.58099931, -0.46188426, -0.18148302],
       [-0.76959435, -1.37414587,  1.37696874, -0.18040537]])'''

# media arítmetica
datos.mean() # Calcula la media aritmetica de

#-0.14786303590303568

np.mean(datos) # Mismo resultado desde la funcion de numpy

#-0.14786303590303568

datos.mean(axis=1) # media aritmetica de cada fila
#array([-0.47228757, -0.40416312,  0.71199682, -0.33806709, -0.23679421])


datos.mean(axis=0) # media aritmetica de cada columna
#array([ 0.0791985 , -0.61180267,  0.23061642, -0.2894644 ])

# mediana
np.median(datos) 
#-0.23234258265023794

np.median(datos, 0) # media aritmetica de cada columna
#array([-0.1074033 , -0.88138082, -0.34466623, -0.18148302])

# Desviación típica
np.std(datos)
#0.73755354584071608

np.std(datos, 0) # Desviación típica de cada columna
#array([ 0.58057213,  0.78352862,  0.87384108,  0.17682485])

# varianza
np.var(datos) 
#0.54398523298221324

np.var(datos, 0) # varianza de cada columna
#array([ 0.337064  ,  0.6139171 ,  0.76359823,  0.03126703])

# moda
stats.mode(datos) # Calcula la moda de cada columna
# el 2do array devuelve la frecuencia.
'''(array([[-0.76959435, -1.37414587, -0.62681496, -0.63329028]]),
 array([[ 1.,  1.,  1.,  1.]]))'''

datos2 = np.array([1, 2, 3, 6, 6, 1, 2, 4, 2, 2, 6, 6, 8, 10, 6])
stats.mode(datos2) # aqui la moda es el 6 porque aparece 5 veces en el vector.
#(array([6]), array([ 5.]))

# correlacion
np.corrcoef(datos) # Crea matriz de correlación.
'''array([[ 1.        ,  0.82333743,  0.15257202,  0.78798675, -0.02292073],
       [ 0.82333743,  1.        , -0.13709662,  0.86873632,  0.41234875],
       [ 0.15257202, -0.13709662,  1.        , -0.47691376,  0.21216856],
       [ 0.78798675,  0.86873632, -0.47691376,  1.        , -0.03445705],
       [-0.02292073,  0.41234875,  0.21216856, -0.03445705,  1.        ]])'''

# calculando la correlación entre dos vectores.
np.corrcoef(datos[0], datos[1])
#array([[ 1.        ,  0.82333743],[ 0.82333743,  1.        ]])

# covarianza
np.cov(datos) # calcula matriz de covarianza
'''array([[ 0.43350958,  0.18087281,  0.06082243,  0.11328658, -0.01782409],
       [ 0.18087281,  0.11132485, -0.0276957 ,  0.06329134,  0.16249513],
       [ 0.06082243, -0.0276957 ,  0.36658864, -0.06305065,  0.15172255],
       [ 0.11328658,  0.06329134, -0.06305065,  0.04767826, -0.00888624],
       [-0.01782409,  0.16249513,  0.15172255, -0.00888624,  1.39495179]])'''

# covarianza de dos vectores
np.cov(datos[0], datos[1])
#array([[ 0.43350958,  0.18087281],[ 0.18087281,  0.11132485]])

# usando pandas
dataframe = pd.DataFrame(datos, index=['a', 'b', 'c', 'd', 'e'], columns=['col1', 'col2', 'col3', 'col4'])
print(dataframe)
'''
col1	col2	col3	col4
a	0.460380	-1.089425	-0.626815	-0.633290
b	-0.107403	-0.881381	-0.344666	-0.283202
c	0.940512	0.866938	1.209479	-0.168941
d	-0.127902	-0.580999	-0.461884	-0.181483
e	-0.769594	-1.374146	1.376969	-0.180405
'''

# resumen estadistadistico con pandas
dataframe.describe()
'''
col1	col2	col3	col4
count	5.000000	5.000000	5.000000	5.000000
mean	0.079199	-0.611803	0.230616	-0.289464
std	0.649099	0.876012	0.976984	0.197696
min	-0.769594	-1.374146	-0.626815	-0.633290
25%	-0.127902	-1.089425	-0.461884	-0.283202
50%	-0.107403	-0.881381	-0.344666	-0.181483
75%	0.460380	-0.580999	1.209479	-0.180405
max	0.940512	0.866938	1.376969	-0.168941 '''

# sumando las columnas
dataframe.sum()
'''
col1    0.395993
col2   -3.059013
col3    1.153082
col4   -1.447322
dtype: float64 '''

# sumando filas
dataframe.sum(axis=1)
'''
a   -1.889150
b   -1.616652
c    2.847987
d   -1.352268
e   -0.947177
dtype: float64 '''

dataframe.cumsum() # acumulados
'''
col1	col2	col3	col4
a	0.460380	-1.089425	-0.626815	-0.633290
b	0.352977	-1.970806	-0.971481	-0.916492
c	1.293489	-1.103868	0.237998	-1.085434
d	1.165587	-1.684867	-0.223887	-1.266917
e	0.395993	-3.059013	1.153082	-1.447322
''' 

# media aritmetica de cada columna con pandas
dataframe.mean()
'''
col1    0.079199
col2   -0.611803
col3    0.230616
col4   -0.289464
dtype: float64
'''

# media aritmetica de cada fila con pandas
dataframe.mean(axis=1)
'''
a   -0.472288
b   -0.404163
c    0.711997
d   -0.338067
e   -0.236794
dtype: float64
'''