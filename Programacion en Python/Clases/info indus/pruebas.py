

mesaje = "1:2:4:2,4,5,6:4,6,7,8"

mesaje = mesaje.split(":")
print(mesaje)
opc, n_v, N, v_1, v_2 = mesaje

v_1 = v_1.split(",")

v_2 = v_2.split(",")

print(opc, n_v, N, v_1, v_2)

if opc == "1":
    suma = 0
    for i in v_1:
        if int(i)%2==0:
            suma = suma+int(i)
    for i in v_2:
        if int(i)%2==0:
            suma = suma+int(i)
print(suma)