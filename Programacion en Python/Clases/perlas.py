##Tenemos un argumento de entrada que equivale al numero de perlas totales.
#sigue una serie numerica y es que cada dos perlas rojas mete una verda.
#calcula un programa que me calcule el numero de perlas verdes dependiendo del numero de entrada

def numero_perlas(numero):
    print "El numero de perlas obtenidas es:"
    print numero/3
    print "EL numero de perlas rojas"
    print numero-(numero/3)

print numero_perlas(4)
