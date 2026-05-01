import struc as st
from mensaje import *
# Abrimos el puerto del arduino a 115200
PuertoSerie = abrirPort("COM2") # cambiar al puerto apropiado
# [a, b, result]
struct = [0, 0, 0.0]
r = [-1]# a -1 para que no sea 0 y entre en el while
while r[0]!="0":
    print( "Esperando petición ...")
    r = receiveMensaje(PuertoSerie)
    r = r.split("-")
    print(r)
    mensa=r[1].split(";")
    st.setA(struct, int(mensa[0]))
    st.setB(struct, int(mensa[1]))
    if r[0]=="[S]": # Suma
        st.Suma(struct)
    elif r[0]=="[R]": # resta
        st.Resta(struct)
    elif r[0]=="[M]": # multiplicar
        st.Multiplicar(struct)
    elif r[0]=="[D]": # dividir
        st.dividir(struct)
    elif r[0]=="[O]": # peticion de resultado
        sendMensaje(PuertoSerie, str(st.getResult(struct))+"\n" )
    elif r[0]=="[L]": # envio de la estructura completa
        sendMensaje(PuertoSerie, str(struct)+"\n" )
    print("struct =", struct)