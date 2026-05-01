def imprimir_hex(n):
    if n >= 1:
        imprimir_horzontal(n)
        imprime_a(n)
        imprime_b(n)
        imprimir_horzontal(n)
    else:
        print "no se puede hacer con ese numero"

def imprimir_horzontal(n):
    print " "*(n)+"-"*(n)+" "*(n)

def imprime_a(n):
     for i in range (n):
            if i == 0:
                print " "*(n -i -1)+"/"+" "*(n)+"\\",
                print
            else:
                print " "*(n -i -1)+"/"+" "*(2*(i+1)+1)+"\\",
                print

def imprime_b(n):
    for i in  reversed (range (n)):
            if i == 0:
                print " "*(n -i -1)+"\\"+" "*(n)+"/",
                print
            else:
                print " "*(n -i -1)+"\\"+" "*(2*(i+1)+1)+"/",
                print

imprimir_hex(3)