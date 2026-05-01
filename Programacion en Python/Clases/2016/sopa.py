# coding=utf-8
__author__ = 'luisutrilla'

def match(palabra, tablero, i, j, direccion):
    """ Busca la ocurrencia de la palabra en el tablero de la sopa de letras
        a partir de la posicion i,j en la direccion indicada.
        Entradas:
            palabra  : palabra a buscar.
            i, j     : posición a partir de la cual inicia la búsqueda.
            direccion: dirección en que se debe realizar la búsqueda.
        Salidas:
            (i,j,direccion) donde i,j indican la palabra donde inicia en
                            el tablero.
            None en caso de que no exista ningua ocurrencia de palabra en
            el tablero.
        Restricción:
            dirección in ["izq-der", "der-izq", "arr-abj", "abj-arr",
                          "diag-arr-der", "diag-abj-der",
                          "diag-arr-izq", "diag-abj-izq"].
    """
    i1, j1 = i, j
    num_lineas = len(tablero)
    largo_linea = len(tablero[0]) if len(tablero[0]) else 0

    k = 0
    while k < len(palabra) and 0 <= i < num_lineas and \
          0 <= j < largo_linea and palabra[k] == tablero[i][j]:

        k += 1

        ## Incrementa o decrementa los índices i,j según sea la dirección
        ## de la búsqueda

        if direccion == "izq-der":
            j += 1
        elif direccion == "der-izq":
            j -= 1
        elif direccion == "arr-abj":
            i += 1
        elif direccion == "abj-arr":
            i -= 1
        elif direccion == "diag-arr-der": ## busca en el sentido / de arriba
                                          ## hacia abajo de derecha a izquierda
            pass ## no implementado
        elif direccion == "diag-abj-der": ## busca en el sentido \ de abajo
                                          ## hacia arriba de derecha a izquierda
            pass ## no implementado
        elif direccion == "diag-arr-izq": ## busca en el sentido / de arriba
                                          ## hacia abajo de izquierda a derecha
            pass ## no implementado
        elif direccion == "diag-abj-izq": ## busca en el sentido \ de abajo
                                          ## hacia arriba de izquierda a derecha
            pass ## no implementado

    if k == len(palabra):
        return (i1, j1, direccion)
    else:
        return None

class SopaDeLetras():
    """ Implementa una clase que permite instaurar un tablero para el
        juego de sopo de letras y luego buscar palabras en éste.
    """

    def __init__(self, texto):
        """ Crea una nueva instancia de tablero de la sopa de letras.
            Entradas:
                texto: texto con el cual se creará el tablero de la sopa
                       de letras.
            Salidas:
                Una instancia de sopa de letras.
            Restricciones:
                Ninguna.
        """
        if not isinstance(texto, str):
            raise TypeError("Se esperaba una tira de caracteres")

        self.tablero = texto.split("\n")  # Crea una lista con las lineas del texto

        ## Verifica que todas las lineas en tablero tengan la misma longitud
        if not all([len(linea) == len(self.tablero[0])
                    for linea in self.tablero]):
            raise TypeError("Las líneas no tiene el mismo largo")

    def busque_horizontal(self, palabra):
        """ Busca palabra, en sentido horizontal, en la sopa de letras.
            Entradas:
                palabra: palabra a buscar.
            Salidas:
                None si la palabra no se encuentra en la sopa de letras.
                (x,y,dir) si la palabra se ecuentra en la sopa de letras,
                en donde x, y representan la linea - columna en que aparece;
                dir indica la dirección ("izq-der" o "der-izq").
            Restricciones:
                Ninguna
        """

        if not(isinstance(palabra, str)):
            raise TypeError("Se esperaba una tira de caracteres")

        if not palabra:
            return None  # Intentó buscar la hilara nula

        for i in range(len(self.tablero)):
            linea = self.tablero[i]
            for j in range(len(linea)):
                pos = match(palabra, self.tablero, i, j, "izq-der")
                if pos == None:
                    pos = match(palabra, self.tablero, i, j, "der-izq")
                if pos != None:
                    return pos
        return None

    def busque_vertical(self, palabra):
        """ Busca palabra, en sentido vertical, en la sopa de letras.
            Entradas:
                palabra: palabra a buscar.
            Salidas:
                None si la palabra no se encuentra en la sopa de letras.
                (x,y,dir) si la palabra se ecuentra en la sopa de letras,
                en donde x, y representan la linea - columna en que aparece;
                dir indica la dirección ("arr-abj" o "abj-arr").
            Restricciones:
                Ninguna
        """

        if not(isinstance(palabra, str)):
            raise TypeError("Se esperaba una tira de caracteres")

        if not palabra:
            return None  # Intentó buscar la hilara nula

        for i in range(len(self.tablero)):
            linea = self.tablero[i]
            for j in range(len(linea)):
                pos = match(palabra, self.tablero, i, j, "arr-abj")
                if pos == None:
                    pos = match(palabra, self.tablero, i, j, "abj-arr")
                if pos != None:
                    return pos
        return None


