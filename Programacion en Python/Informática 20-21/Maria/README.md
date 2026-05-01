# Práctica 1. Ramificación, condicionales e iteración

Ésta es la primera práctica evaluable.  Reúne un variado grupo de prácticas relacionadas con la iteración.  Resuelve los ejercicios en cualquier orden.

# 1. Ejercicios básicos

## 1.1. El primer múltiplo de un número

Implementa la función `primer_multiplo` que recibe como argumentos un número entero `n` y una lista `L` de números enteros y devuelve la posición del primer múltiplo de `n` que encuentre en la lista `L`. Si no hay ninguno debe devolver -1.

## 1.2. Concatenar cadenas de texto

Define una función `concatena_lineas` que admita un único argumento con una lista de cadenas de texto, que corresponde al contenido de cada línea de texto de un poema.  La función debe devolver el resultado de concatenar todas las cadenas insertando un carácter terminador de línea tras cada línea.  Por ejemplo:

```
>>> concatena_lineas(['No por mucho madrugar', 'amanece más temprano'])
'No por mucho madrugar\namanece más temprano\n'
```

## 1.3. Probabilidad de coincidencia en la fecha de cumpleaños

Define una función de nombre `prob_mismo_cumple` que admita un único argumento entero n. Esta función debe devolver un número real que corresponde a la probabilidad de que al menos dos personas de un grupo de n personas cumplan años en el mismo día.  Consulta [esta página](https://es.wikipedia.org/wiki/Paradoja_del_cumplea%C3%B1os) para más información.

### Pista

Calcularemos la probabilidad inversa, la de que todos cumplan en día diferente.

La probabilidad de que la persona 1 cumpla un día en el que todavía no hayamos contabilizado a otra persona es


<img src="https://render.githubusercontent.com/render/math?math=P_1 = \frac{365}{365}&mode=display">

La probabilidad de que la persona 2 cumpla en cualquiera de los otros días es

<img src="https://render.githubusercontent.com/render/math?math=P_2 = \frac{364}{365}&mode=display">

Y en general la probabilidad de que la persona *i* cumpla en cualquiera de los otros días en los que no se han contabilizado alguna de las *i-1* personas anteriores es:

<img src="https://render.githubusercontent.com/render/math?math=P_i = \frac{365 - i %2B 1}{365}&mode=display">

Combinando todas las probabilidades

<img src="https://render.githubusercontent.com/render/math?math=P_{dif} = \prod_{i=1}^n \frac{366 - i}{365}&mode=display">

La probabilidad que se pide es la opuesta

<img src="https://render.githubusercontent.com/render/math?math=P = 1 - \prod_{i=1}^n \frac{366 - i}{365}&mode=display">

## 1.4. Suma de serie

Define una función de nombre `suma_serie` con un argumento `n` que devuelva el valor de la suma de los primeros n términos de la serie siguiente:

<img src="https://render.githubusercontent.com/render/math?math=\sum \frac{1}{n^2} = \frac{1}{1^2} %2B \frac{1}{2^2} %2B \frac{1}{3^2} %2B \cdots&mode=display">

## 1.5. Números feos

Un número feo es aquel cuyos únicos divisores primos son 2, 3 o 5. Define una función de nombre `primer_feo` que admite como argumento una secuencia de números enteros.  La función debe devolver el primer número feo de la secuencia o bien `None` si no contiene ninguno.

## 1.6. Suma de dígitos

Define una función de nombre `suma_digitos` que admite como argumento un número entero.  Debe devolver un número entero de una sola cifra, resultante de sumar los dígitos del número mientras el resultado tenga más de un dígito.

Por ejemplo, para el número 187 la suma de los dígitos resulta 16, que tiene más de un dígito.  Por tanto volvemos a aplicar el mismo procedimiento, que resulta en un 7.  Éste ya solo tiene un dígito y por tanto es el resultado final.

## 1.7. Conjunto Mandelbrot

El conjunto de Mandelbrot es el conjunto de números complejos c para los cuales el método iterativo

<img src="https://render.githubusercontent.com/render/math?math=\begin{matrix} z_0=0 \\ z_{n%2B1}=z_n^2%2Bc \end{matrix}&mode=display">

no tiende a infinito, es decir, no es divergente.

Define una función de nombre `en_mandelbrot` que admite dos argumentos reales `x` e `y`, correspondientes a la parte real e imaginaria del número complejo `c`.  Aplica el método iterativo para determinar si esas coordenadas corresponden a un punto del conjunto Mandelbrot.  Para determinar la divergencia puedes utilizar el siguiente criterio:

* Sí, en valor absoluto, <img src="https://render.githubusercontent.com/render/math?math=z_{n%2B1}"> supera el valor de 2 entonces es divergente y debe devolver `False`.

* Si al cabo de 80 iteraciones no se ha superado el límite, entonces no es divergente y debe devolver `True`.

## 1.8. Números persistentes

En *El prodigio de los números* de Clifford A. Pickover, cap. 15, aparece un ejemplo de serie numérica: 969, 486, 192, 18, 8. Cada número se calcula multiplicando los dígitos del anterior.

A partir de este ejemplo define el concepto de persistencia de un número como el número de pasos del tipo referido (4 en nuestro ejemplo) que hay que llevar a cabo antes de que el número colapse bajo la forma de un único dígito.

Define una función `primer_persistente(n)` que devuelva el primer número con persistencia `n`. 

Nota: Puede usarse enumeración exhaustiva, puesto que el valor de `n` será relativamente bajo. Así, por ejemplo, no se conoce números con persistencia 12 o superior.

## 1.9. Cuadrones fuertes

¿Cuál es el menor cuadrado perfecto que comienza con el dígito 1, que sigue siendo un cuadrado perfecto al reemplazar el 1 por un 2? 

Define una función `primer_cuadron_fuerte` sin argumentos que calcule este valor. 

## 1.10. Números ondulantes

Un número es ondulante cuando sus dígitos son alternativamente mayores o menores que los dígitos adyacentes.  Por ejemplo, el número 4253612 es ondulante.

Define una función `es_ondulante` que acepta un único argumento entero positivo.  Debe devolver `True` si el argumento es ondulante y `False` en caso contrario.

# 2. Ejercicios de conjetura y comprobación

Los siguientes ejercicios se encaminan hacia la exploración del método de *guess and check* que ya hemos visto en clase.

## 2.1. Derivación de polinomios

Sea un polinomio expresado como una lista de los coeficientes en orden.  Por ejemplo `[0, 1]` es *x*, `[2,4,1]` es <img src="https://render.githubusercontent.com/render/math?math=2%2B4x%2Bx^2">.

Elabora una función `polyder` que calcule la derivada del polinomio que se pasa como argumento. Por ejemplo:

``` 
>>> polyder([2,5,2,1])
[5, 4, 3]
```

## 2.2. Evaluación de polinomios

*Elabora* una función `polyval` que evalúa un polinomio `p` para un valor de `x` indicado como segundo argumento. Por ejemplo:

```
>>> polyval([0,1,1],3)
12
```

## 2.3. Teorema de Bolzano

El teorema de Bolzano dice que, para funciones continuas, todos los valores comprendidos entre *f(a)* y *f(b)* están entre los valores de la función en el intervalo *[a,b]*.  En particular si *f(a)>0* y *f(b)<0* entonces seguro que hay una raiz en el intervalo *[a,b]*.

Utiliza este teorema para aplicar el método de bisección para calcular una raiz mediante una función `root_bolzano`.  Utiliza valores aleatorios para encontrar los valores iniciales de *a* y *b* que cumplan la condición de interés.  Asegúrate de que la precisión es mejor que `1e-7`. Por ejemplo:

```
>>> root_bolzano([-4,0,1])
1.9999938724366215
```

Nota: las pruebas de este ejercicio asumen una implementación correcta de `polyval`.

### Pista

Puedes y debes usar la función `polyval` definida con anterioridad.

Para generar números aleatorios entre un mínimo y un máximo puedes usar esta función:

```
def rng(minimo, maximo):
    from random import random
    return minimo + random()*(maximo - minimo)
```

## 2.4. Newton-Raphson general

Define una función `root_newton_raphson(polinomio,epsilon)` para utilizar el método de Newton-Raphson para encontrar una raiz cualquiera de un polinomio que se indica como primer argumento con un margen de error que se indica como segundo argumento.

Puedes y debes usar las funciones `polyval` y `polyder` definidas con anterioridad.

# Pruebas

Para las pruebas se utiliza el entorno `pytest`.  Esta vez tendrás que instalar `pytest` para ejecutar las pruebas.  Para ello abre un intérprete de órdenes (o Terminal en MacOSX) y escribe:

```
python -m pip install -U pytest
```

Ahora comprueba que tienes `pytest` correctamente instalado:

```
pytest --version
pytest 6.1.0
```

Puedes ejecutar todas las pruebas simplemente ejecutando `pytest`.

