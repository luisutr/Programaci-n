def contar_lineas(codigo):
    saltos = 0
    comen = 0
    doble_salto = 0
    for i in range(len(codigo)-1):
        if codigo[i] == '\n' and codigo[i+1] == '\n':
            doble_salto+=1
        if codigo[i] == '\n':
            saltos += 1
            posicion = i
            while (codigo[posicion+1] == " "):
                posicion+=1
            if codigo[posicion+1]=="#":
                comen+=1
    lineas = saltos
    return lineas-comen-doble_salto

codigo = '''
# Kata FizzBuzz
def fizz_buzz(a,b):
  def fb(n):
    # Divisible por 3 y por 5 sii divisible por 15
    if n%15 == 0: return 'FizzBuzz'
    if n%3 == 0: return 'Fizz'
    if n%5 == 0: return 'Buzz'
    return str(n) # Como cadena para join


  return '\\n'.join(fb(i) for i in range(a,b))
'''
print(contar_lineas(codigo))


saltos = '''

'''
espacios = "  "
tabulaciones ='''           '''

otra = '         '

print(len(saltos), len(espacios),len(tabulaciones), len(otra))

if '''
''' == '\n':
    print("hola")


def contar_lineas2(code):
    comentarios = 0
    saltodelinea = 0
    lista = code.split("\n")
    print(lista)
    for i in lista:
        i = i.strip()
        print(i)
        if len(i) > 0:
            if i[0] == "#":
                comentarios += 1
        if i == "":
            saltodelinea+=1
    return len(lista) - comentarios -saltodelinea


print(contar_lineas2('''
# Kata FizzBuzz
def fizz_buzz(a,b):
  def fb(n):
    # Divisible por 3 y por 5 sii divisible por 15
    if n%15 == 0: return 'FizzBuzz'
    if n%3 == 0: return 'Fizz'
    if n%5 == 0: return 'Buzz'
    return str(n) # Como cadena para join

  return '\\n'.join(fb(i) for i in range(a,b))
'''))


def sistema_L(e_ini,reglas,it):
    for i in range(it):
        for j in range(len(e_ini)):
            if e_ini[j] == 'F':
                e_ini[j] = reglas['F']
            if e_ini[j] == 'G':
                e_ini[j] = reglas['G']
    return e_ini


print(sistema_L("F-G-G", {'F': "F-G+F+G-F", 'G': "GG"}, 3))


def creciente_decreciente(n):
    numero = str(n)
    anterior = numero[0]
    if int(numero[0])<int(numero[1]):
      bandera = "crece"
    else:
      bandera = "decrece"
    for i in range(1,len(numero)):
      aux = bandera
      if int(numero[i])>int(anterior):
        bandera = "crece"
      elif int(numero[i])<int(anterior):
        bandera = "decrece"
      else:
          bandera = bandera
      anterior = numero[i]
      if aux != bandera:
        return 0
    if bandera == "crece":
       return 1
    if bandera == "decrece":
       return -1

print(creciente_decreciente(97739))