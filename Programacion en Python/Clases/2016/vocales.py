__author__ = 'luisutrilla'

def ejercicio(x):
    lista=[]
    try:
        for i in x:
            funcion=(i*i)/(2.*i)
            lista.append(funcion)
        return lista
    except TypeError:
        print 'no se aceptan vocales'

print ejercicio([2,3,'a',8])
print ejercicio([2,3,8])