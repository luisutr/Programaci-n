

def notacioncutre(operacion):
    operacion = operacion.split(" ")
    operacion.append("fin")
    operalg=[]
    aux=False
    for i in range(len(operacion)-1):
        if operacion[i] not in ["+","-","*","/"]:
            operalg.append(operacion[i])
        else:
                if operacion[i] in ["*","/"]:
                    operalg.insert(i - 1, operacion[i])
                    operalg.insert(i-2,"(")
                    operalg.append(")")
                    aux = True
                else:
                    if aux == True:
                        operalg.insert(i - 3, operacion[i])
                        aux= False
                    else:
                        operalg.insert(i - 1, operacion[i])
    operalg = ''.join(operalg)
    return operalg


def rpn_to_algebraic(opracion):
    if len(opracion)>1:
        listanum=[]
        listaop=[]
        opracion = opracion.split(" ")
        for i in opracion:
            if i not in ["+","-","*","/", " "]:# es un numero
               listanum.append(i)
            elif i != " ":
                listaop.append(i)
        listaop.append(" ")
        resultado=""
        for i in range(len(listanum)):
            resultado+=listanum[i]+listaop
        return resultado
    else:
        return opracion



print(rpn_to_algebraic('12 3 - 2 5 * +'))#((12 - 3) + (2 * 5))'
print(rpn_to_algebraic('1 2 3 4 - - -'))#, '(1 - (2 - (3 - 4)))')
print(rpn_to_algebraic('1 2 - 3 - 4 -'))#, '(((1 - 2) - 3) - 4)')
print(rpn_to_algebraic('1'))#, '1')