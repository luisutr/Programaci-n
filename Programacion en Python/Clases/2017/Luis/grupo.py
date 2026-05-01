def principal(m):
    m_restada=[]
    m_dividida=[]
    m_colocada = matriz_colocar(m,0) # y me deja siempre la pivote en la primera fila
    for i in range(len(m_colocada)):
         m_dividida.append(dividir(m_colocada[i]))
         pivote = fila_colocar(m_dividida,0)
    m_restada.append(pivote)
    for i in range(len(m_dividida)-1):
        m_restada.append(restar(pivote,m_dividida[i+1]))
    return m_restada


def restar(fila1, fila2):
    resta=[]
    for i in range(len(fila1)):
        resta.append(fila1[i]-fila2[i])
    return resta
def dividir(fila):
    division=[]
    for i in range(len(fila)):
        if fila[0] != 0:
            division.append(float(fila[i]/float(fila[0])))
        if fila[0] == 0:
            division.append(fila[i])
    return division

def matriz_colocar(m, posicion):
    for i in range(len(m)):
        if m[0][posicion] == 0:
            aux=m.pop(posicion)
            m.append(aux)
    return m

def fila_colocar(m, posicion):
    for i in range(len(m)):
        if m[0][posicion] == 0:
            aux=m.pop(posicion)
            m.append(aux)
    pivote0 = m[0]
    return pivote0

print(principal([[0,2,4],[3,2,3],[2,0,4]]))