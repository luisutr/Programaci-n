## EJERCICIO 1

from math import *

def primer_multiplo (n,L):
    for posicion, valor in enumerate(L):# indicar el número que ocupa esa posición dentro de la lista
        while valor % n==0 :        # Con el porcentaje nos fijamos en el resto, daría resto 0
            return (posicion) 
    else: # En el caso que no encuentre múltiplos obtendremos el valor -1
        return -1 
print(primer_multiplo(295, [922, 972, 746, 231, 54, 746, 686, 926, 247, 914, 873, 387, 332, 369, 211, 840, 66, 637, 420, 754, 386, 984, 837, 52, 916, 197, 232, 168, 933, 487, 577, 825, 657, 507, 606, 761, 324, 617, 49, 704, 854, 981, 475, 299, 570, 90, 689, 63, 712, 848, 293, 370, 244, 57, 733, 404, 486, 749, 818, 579, 758, 586, 144, 958, 17, 866, 932, 397, 891, 918, 998, 728, 635, 619, 293, 207, 450, 784, 167, 730, 955, 461, 740, 160, 835, 132, 960, 269, 445, 62, 797, 722, 572, 755, 616, 105, 668, 464, 312, 1, 263, 252, 819, 539, 406, 32, 658, 757, 905, 871, 309, 772, 313, 452, 539, 334, 255, 143, 841, 66, 472, 524, 438, 476, 219, 930, 908, 696, 964, 42, 957, 337, 304, 118, 609, 823, 430, 762, 947, 110, 859, 302, 497, 77, 807, 195, 776, 901, 394, 400, 389, 10, 794, 460, 89, 62, 980, 775, 629, 425, 129, 662, 702, 867, 291, 31, 544, 287, 327, 0, 86, 490, 510, 52, 524, 473, 355, 73, 823, 111, 169, 301, 292, 766, 5, 499, 18, 741, 250, 25, 872, 202, 726, 953, 48, 541, 957, 938, 992, 979, 704, 580, 565, 788, 612, 318, 23, 250, 906, 263, 5, 84, 420, 335, 80, 672, 312, 879, 24, 147, 753, 775, 250, 955, 124, 403, 717, 17, 13, 847, 1, 494, 16, 118, 18, 184, 541, 824, 188, 585, 524, 203, 73, 549, 208, 622, 414, 418, 486, 868, 241, 199, 311, 913, 462, 381, 562, 267, 253, 118, 296, 800, 369, 986, 791, 412, 428, 780, 746, 529, 795, 407, 759, 949, 347, 977, 520, 686, 94, 662, 730, 452, 954, 169, 492, 715, 744, 248, 585, 716, 219, 723, 943, 93, 328, 890, 548, 165, 848, 285, 949, 770, 876, 511, 571, 95, 867, 487, 33, 855, 528, 821, 193, 16, 764, 272, 666, 814, 651, 552, 488, 967, 605, 223, 339, 954, 403, 56, 759, 279, 372, 651, 86, 127, 522, 213, 208, 982, 90, 637, 31, 395, 580, 271, 23, 868, 447, 615, 460, 922, 875, 951, 363, 66, 937, 106, 566, 358, 791, 858, 538, 150, 789, 599, 998, 649, 37, 148, 194, 756, 411, 216, 567, 558, 640, 390, 39, 752, 702, 108, 779, 913, 533, 516, 621, 396, 355, 901, 320, 599, 660, 192, 510, 54, 799, 743, 356, 484, 285, 711, 650, 510, 25, 890, 447, 227, 51, 407, 259, 491, 167, 812, 924, 404, 875, 241, 749, 562, 480, 874, 198, 268, 865, 243, 341, 371, 275, 439, 236, 119, 244, 36, 258, 803, 288, 756, 414, 848, 875, 580, 694, 745, 658, 110, 496, 987, 875, 311, 665, 316, 288, 85, 518, 896, 121, 832, 199, 308, 345, 667, 816, 59, 995, 139, 126, 570, 366, 17, 233, 590, 424, 218, 718, 705, 530, 126, 429, 662, 200, 624, 31, 163, 847, 39])
)

# Las listas empiezan enumerando desde 0


## EJERCICIO 2 

def concatena_lineas (L): 
    esp= '' # Creamos un espacio en el que añadiremos las cadenas
    var1= '\n' # Creamos una variable para que cada cadena aparezca en una línea
    for cadena in L: 
            esp = esp + cadena + var1 # Concatenamos 
    return esp

print(concatena_lineas(['En las noches claras', 'resuelvo el problema de la soledad del ser.', 'Invito a la luna y con mi sombra somos tres.']))

## EJERCICIO 3

def prob_mismo_cumple(n):
    p = 1.0
    for i in range (1,n+1):
        p=p*(366-i)/365
    return 1-p
print(prob_mismo_cumple(10), 0.1169481777110779)
print(prob_mismo_cumple(10), 0.1169481777110779)
print(prob_mismo_cumple(30), 0.7063162427192686)
print(prob_mismo_cumple(50), 0.9703735795779884)
print(prob_mismo_cumple(70), 0.9991595759651571)
print(prob_mismo_cumple(90), 0.9999938483561236)

## EJERCICIO 4

def suma_serie (n): # Seguimos los mismos pasos que en el ejercicio 2 
    s=0
    
    for elemento in range(1,n+1):
        
        serie= 1/elemento**2
        s= s + serie
    return s

print(suma_serie(90))

## EJERCICIO 5
def primer_feo(sec):
    for num in sec:
      if es_feo(num) == True:
        return num
    return None

def es_feo(num):
  feo = False
  if (num%2 == 0):
    feo = True
  if (num%3 == 0):
    feo = True
  if (num%5 == 0):
    feo = True

  for valor in range (7,999):
    if es_primo(valor) == 0:
        if (num%valor == 0):
          return False

  return feo

def es_primo(numero):
    for valor in range(numero):
        if (valor > 1):
            if (numero%valor == 0):
                return -1
    return 0

print(primer_feo([922, 971, 741, 231, 53, 741, 687, 927, 247, 914, 873, 387, 332, 369, 211, 840, 66, 637, 420, 754, 386, 984, 837, 52, 916, 197, 232, 168, 933, 487, 577, 825, 657, 507, 606, 761, 327, 617, 49, 704, 854, 981, 475, 299, 570, 689, 63, 712, 848, 293, 370, 244, 57, 733, 404, 749, 818, 579, 758, 586, 144, 958, 17, 866, 932, 397, 891, 918, 998, 728, 635, 619, 293, 207, 450, 784, 167, 730, 955, 461, 740, 160, 835, 132, 960, 269, 445, 62, 797, 722, 572, 755, 616, 105, 668, 464, 312, 1, 263, 252, 819, 539, 406, 32, 658, 757, 905, 871, 309, 772, 313, 452, 539, 334, 255, 143, 841, 66, 472, 524, 438, 476, 219, 930, 908, 696, 964, 42, 957, 337, 304, 118, 609, 823, 430, 762, 947, 110, 859, 302, 497, 77, 807, 195, 776, 901, 394, 400, 389, 10, 794, 460, 89, 62, 980, 775, 629, 425, 129, 662, 702, 867, 291, 31, 544, 287, 327, 86, 490, 510, 52, 524, 473, 355, 73, 823, 111, 169, 301, 292, 766, 5, 499, 18, 741, 250, 25, 872, 202, 726, 953, 48, 541, 957, 938, 992, 979, 704, 580, 565, 788, 612, 318, 23, 250, 906, 263, 5, 84, 420, 335, 80, 672, 312, 879, 24, 147, 753, 775, 250, 955, 124, 403, 717, 17, 13, 847, 1, 494, 16, 118, 18, 184, 541, 824, 188, 585, 524, 203, 73, 549, 208, 622, 414, 418, 868, 241, 199, 311, 913, 462, 381, 562, 267, 253, 118, 296, 800, 369, 986, 791, 412, 428, 780, 746, 529, 795, 407, 759, 949, 347, 977, 520, 686, 94, 662, 730, 452, 954, 169, 492, 715, 744, 248, 585, 716, 219, 723, 943, 93, 328, 890, 548, 165, 848, 285, 949, 770, 876, 511, 571, 95, 867, 487, 33, 855, 528, 821, 193, 16, 764, 272, 666, 814, 651, 552, 488, 967, 605, 223, 339, 954, 403, 56, 759, 279, 372, 651, 86, 127, 522, 213, 208, 982, 90, 637, 31, 395, 580, 271, 23, 868, 447, 615, 460, 922, 875, 951, 363, 66, 937, 106, 566, 358, 791, 858, 538, 150, 789, 599, 998, 649, 37, 148, 194, 756, 411, 216, 567, 558, 640, 390, 39, 752, 702, 108, 779, 913, 533, 516, 621, 396, 355, 901, 320, 599, 660, 192, 510, 54, 799, 743, 356, 484, 285, 711, 650, 510, 25, 890, 447, 227, 51, 407, 259, 491, 167, 812, 924, 404, 875, 241, 749, 562, 480, 874, 198, 268, 865, 243, 341, 371, 275, 439, 236, 119, 244, 36, 258, 803, 288, 756, 414, 848, 875, 580, 694, 745, 658, 110, 496, 987, 875, 311, 665, 316, 288, 85, 518, 896, 121, 832, 199, 308, 345, 667, 816, 59, 995, 139, 126, 570, 366, 17, 233, 590, 424, 218, 718, 705, 530, 126, 429, 662, 200, 624, 31, 163, 847, 39]))
#144


## EJERCICIO 6

def suma_digitos (N):
    N = int(N)
    s = 0
    while N > 10:
        # convertir a cadena para poder recorrer el numero
        cadena = str(N)
        suma = 0
        for i in cadena:
            suma = suma + int(i)
        N = suma
        # ir sumando los digitos
        # convertir a entero
        # actualizas N con ese valos del sumatorio
    return N

print(suma_digitos(3424234234242342342342342342345346546567567),7)


## EJERCICIO 7

def en_mandelbrot(x,y):
    c =complex(x,y)
    z=0
    for i in range(80):
        z = z**2 + c
        if abs(z) > 2:
            return False
    return True

print(en_mandelbrot(-0.75, 0.1))
print(en_mandelbrot(-0.75, 0))

# EJERCICIO 8

def primer_persistente(n):
    for i in range(1, 9999999):
        persistencia = calcula_persistencia(i)
        if persistencia == n:
            return i


def calcula_persistencia(x):
    persistencia = 0
    if x <= 9:
        return persistencia
    m = str(x)
    while len(m) >= 2:
        num = 1
        for e in m:
            num *= int(e)
        persistencia += 1
        m = str(num)
    return persistencia

print(primer_persistente(2))






## EJERCICIO 9
 
from math import sqrt 
def primer_cuadron_fuerte ():

    for i in range (1000000):
        if cuadron(i) == True:
            c1 = str(i)
            if c1[0] == "1":
                c2 = c1.replace("1","2",1)
                if cuadron(int(c2)) == True:
                    return 1

def cuadron(n):
    raiz = sqrt(n)
    entera = int(raiz)
    decimales = raiz - entera
    if decimales == 0.0:
        return True
    else:
        return False



## EJERCICIO 10 

def es_ondulante(n):
  num = str(n)
  for posi, i in enumerate(num):
    if (posi > 1) and (posi < (len(num)-1)):
      if (num[posi-1] <= i and (num[posi+1] >= i)):
        return False
      if (num[posi-1] >= i and (num[posi+1] <= i)):
        return False
  return True




## EJERCICIO 11

def polyder (pol):
    deri = []
    for posi,valor in enumerate(pol):
        if posi >= 0:
            deri.append(posi*valor)
    return deri


## EJERCICIO 12

def polyval(p,x):
  result = 0.0
  for posi,valor in enumerate(p):
    result = result + valor*(x**posi)
     
  return result