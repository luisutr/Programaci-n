def fase_carga(voltios,amperios):
    if 0<=voltios<14.5 and (amperios>=1.):
        return "Bulk"
    elif voltios>14.5 and (amperios<.1):
        return "Flotacion"
    else:
        return "Absorcion"

#print(fase_carga(14.5,.5))



vec = [5,2,3,1,2,3,4,3,2,1]
max = 0
pos = 0
for i in vec:
    if max < vec.count(i):
        max = vec.count(i)
        pos = vec.index(i)
print(vec[pos])

num = 10
vector = ""
for i in range(num):
    vector += input("Dame entero: ")+":"
print(vector[0:-1])