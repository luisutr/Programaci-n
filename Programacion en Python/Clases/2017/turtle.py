__author__ = 'luisutrilla'

import turtle

def arbol(tam, prof):
    if prof==0:
        return
    else:
        turtle.forward(tam)
        turtle.left(45)
        arbol(tam*2/3, prof-1)
        turtle.right(90)
        arbol(tam*2/3, prof-1)
        turtle.left(45)
        turtle.back(tam)



print arbol(10,6)

