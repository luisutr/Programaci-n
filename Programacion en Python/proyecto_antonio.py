import matplotlib.pyplot as plt
import tkinter
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
from matplotlib.pyplot import figure



 # Generar datos para dibujar un gráfico sin

def sacar_lineas():#me crea una lista con las lineas del texo
    datos = []
    with open("registrador.csv") as fname:
        lineas = fname.readlines()
    for linea in lineas:
        datos.append(linea.strip('\n'))
    return datos



def obtener_valores(list):#obtiene los valores de amplitud
    count=0
    L=[]
    ejeXY=''
    Q=[0]
    pos=0
    for i in list:
        if i==',':
            count+=1
        if count==4:
            L.append(i)
    L.remove(L[0])
    for j in L:
        ejeXY+=str(j)
        pos+=1
        if pos==6:
            Q[0]=ejeXY
            ejeXY=''
    return Q[0]

def lista_de_valores():#me crea una lista con los valores requeridos eliminando las 18 lineas primeras
    valores=[]
    cont=0
    for i in sacar_lineas():
        cont+=1
        if cont>18:
            valores.append(float(obtener_valores(i)))#llamo a la funcion que me devuelve una lista con los valores de amplitud pasandole el renglon entero
    return  [i for i in range(len(valores))],valores


def graficar():
    ejeX,ejeY=lista_de_valores()
    plt.plot(ejeX, ejeY, label='linear')
    plt.grid()



def registrar_coordenada(event):
    x=[]
    y=[]
    if event.inaxes is not None:
        x.append(event.xdata)#me añade los puntos del grafico
        y.append(event.ydata)
    q,w=x[0],y[0]#guardo los puntos para representarlos
    plt.scatter(x,y)#dibuja los puntos
    plt.text(x.pop()+10,y.pop(), str(round(q) )+ ' : '+str(round (w,2)))#añado 10 para dibujarlas separadas de los puntos
    print (y)





def registrar(event):
    x=[]
    y=[]
    x.append(event.xdata)
    y.append(event.ydata)
    plt.scatter(x,y)








def _quit():
         "" "Llame a esta función al hacer clic en el botón de salida" ""
         root.quit () # Finaliza el bucle principal
         root.destroy () # destruye la ventana





root = tkinter.Tk () # Crear ventana principal de tkinter
root.title ("Usar matplotlib en tkinter")

f = figure(figsize=(5, 4), dpi=100)
f.add_subplot (111) # Agregar subgráfico: 1 fila, 1 columna, 1er

 # Visualice los gráficos dibujados en tkinter: cree un lienzo de lienzo que pertenezca a la raíz y coloque la imagen f en el lienzo
canvas = FigureCanvasTkAgg(f, master=root)



canvas.mpl_connect('button_press_event',registrar_coordenada)#me detecta un click en el grafico y me llama a la funcion registrar coordenada

canvas.draw () # Tenga en cuenta que el método show está desactualizado, use draw en su lugar
#canvas.get_tk_widget (). pack (lado = tkinter.TOP, fill = tkinter.BOTH,  expand = tkinter.YES) # ajustar con el ajuste del tamaño de la ventana

 #Se muestra la barra de herramientas de navegación de # matplotlib (no se mostrará de forma predeterminada)
toolbar = NavigationToolbar2Tk(canvas, root)
toolbar.update()
canvas._tkcanvas.pack (side = tkinter.TOP, fill=tkinter.BOTH, expand=tkinter.YES)





 # Crear un botón y enlazar la función anterior
button = tkinter.Button (master = root, text = "cerrar",bg='red', command = _quit)
 # Botón debajo
button.pack(side=tkinter.BOTTOM)

button2 = tkinter.Button (master = root, text = "graficar",bg='magenta', command = graficar)
 # Botón debajo
button2.pack(side=tkinter.BOTTOM)

#button3=tkinter.Button(master=root, text='borrar puntos', bg='yellow', command=borrar)
#button3.pack(side=tkinter.BOTTOM)






 # Bucle principal
root.mainloop()