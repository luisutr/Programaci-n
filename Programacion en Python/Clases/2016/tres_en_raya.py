'''
  Tres en raya
  Versión 1.0
'''
import graphics
import time

# lista donde almacenamos el tablero
tablero = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

# Si una casilla contiene ' ' está vacía, si contiene 'O' o 'X' está ocupada con esa ficha
# El número de cada elemento de la lista sería:
#  0 | 1 | 2
# -----------
#  3 | 4 | 5 
# -----------
#  6 | 7 | 8
#

#array de las posiciones ganadoras
ganadoras = [[0, 1, 2],
             [3, 4, 5],
             [6, 7, 8],
             [0, 3, 6],
             [1, 4, 7],
             [2, 5, 8],
             [0, 4, 8],
             [2, 4, 6]]

#Otras variables necesarias
tam_linea=5   #tamaño de la línea de los dibujos
jugador='O'   #simbolos de cada jugador
ordenador='X'


#Creación de la ventana principal
win = GraphWin('El Juego de tres en raya', 500, 500)
win.setBackground(color_rgb(40, 120, 180))
abajo = Rectangle(Point(0,350),Point(502,500))
abajo.draw(win)
abajo.setFill(color_rgb(150, 10, 0))
te = Text(Point(250, 425), 'TRES EN RAYA')
te.setTextColor(color_rgb(200, 240, 250))
te.setSize(36)
te.setFace('courier')
te.setStyle('bold')
te.draw(win)


#Dibujo del tablero
lineah1 = Line(Point(100,120),Point(400,120))
lineah1.setWidth(tam_linea)
lineah1.draw(win)
lineah2 = Line(Point(100,220),Point(400,220))
lineah2.setWidth(tam_linea)
lineah2.draw(win)
lineav1 = Line(Point(200,20),Point(200,320))
lineav1.setWidth(tam_linea)
lineav1.draw(win)
lineav2 = Line(Point(300,20),Point(300,320))
lineav2.setWidth(tam_linea)
lineav2.draw(win)

#Preguntar para saber quien quiere comenzar
rec=Rectangle(Point(100,70),Point(400,270))
rec.setFill(color_rgb(200, 240, 250))
rec.draw(win)
txt_titulo=Text(Point(250,120),"¿Quién comienza?")
txt_titulo.draw(win)
txt_pregunta=Text(Point(250,200),"   Usuario    Computadora")
txt_pregunta.draw(win)
if win.getMouse().getX()>250:
    turno=ordenador
else:
    turno=jugador
txt_pregunta.undraw()
txt_titulo.undraw()
rec.undraw()


#Se inicia el juego
while True:
    if turno==jugador:
        #obtener posicion
        while 1:
            click = win.getMouse()
            eleccion=int((click.getX()-100)/100)
            eleccion+=int((click.getY()-20)/100)*3
            if eleccion in range(0,9) and tablero[eleccion]==' ':
                break
    else:
        #calcular posicion
        # la primera libre
        for i in range(0,9):
          if tablero[i]==' ':
              eleccion=i
              time.sleep(0.5)
              break

    #Asignamos al tablero en memoria la marca
    tablero[eleccion]=turno

    #Dibujamos la marca
    if eleccion in [0,3,6]: posx=150
    elif eleccion in [1,4,7]: posx=250
    else: posx=350
    if eleccion in [0,1,2]: posy=70
    elif eleccion in [3,4,5]: posy=170
    else: posy=270
    if turno==jugador:   
        c = Circle(Point(posx,posy), 30)
        c.setFill("black")
        c.draw(win)
    else:
        x1=Line(Point(posx-40,posy-40),Point(posx+40,posy+40))
        x1.setWidth(5)
        x1.draw(win)
        x2=Line(Point(posx-40,posy+40),Point(posx+40,posy-40))
        x2.setWidth(5)
        x2.draw(win)

    #Comprobamos si alguien gana
    ganador=' '
    for a_comprobar in ganadoras:
        if tablero[a_comprobar[0]]==tablero[a_comprobar[1]]==tablero[a_comprobar[2]] and tablero[a_comprobar[0]]!=' ':
            ganador=tablero[a_comprobar[0]]
            break
    print(ganador)
    if ganador==jugador:
        recuadro = Rectangle(Point(0,175),Point(500,225))
        recuadro.draw(win)
        recuadro.setFill('GhostWhite')
        t = Text(Point(250, 200), '¡¡ HAS GANADO !!')
        t.setTextColor('green')
        t.setSize(36)       
        t.setStyle('bold')
        t.draw(win)
        break
    elif ganador==ordenador:
        recuadro = Rectangle(Point(0,175),Point(500,225))
        recuadro.draw(win)
        recuadro.setFill('GhostWhite')
        t = Text(Point(250, 200), '¡¡ TE GANE !!')
        t.setTextColor('green')
        t.setSize(36)       
        t.setStyle('bold')
        t.draw(win)
        break

    #Comprobamos tablas
    if not (' ' in tablero):
        recuadro = Rectangle(Point(0,175),Point(500,225))
        recuadro.draw(win)
        recuadro.setFill('GhostWhite')      
        t = Text(Point(250, 200), '¡¡ TABLAS !!')
        t.setTextColor('green')
        t.setSize(36)       
        t.setStyle('bold')
        t.draw(win)
        break
    
    #cambio de turno para el siguiente
    if turno==jugador:
        turno=ordenador
    else:
        turno=jugador


win.getMouse()
win.close()
