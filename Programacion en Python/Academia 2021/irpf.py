def calcula_irpf(sueldo):
    if sueldo>=0 and sueldo  <= 12450:
        return "19%"
    elif sueldo > 12450 and (sueldo-12450) <= 20200:
        return "19% 12.450 y 24%"+str(sueldo-12450)
    elif sueldo > 20200 and sueldo <= 35200:
        return "19%"
    #...
    else:
        return "47%"

def irpf2(sueldo):
    virpf = [12450, 20200, 35200, 60000, 300000]
    pirpf = [19, 24, 30, 37, 45, 47]
    for i in range(len(virpf)):
        if sueldo >virpf[i]:
            print((str(pirpf[i])+"%",virpf[i]))
            sueldo-=virpf[i]
        else:
            return (str(pirpf[i])+"%", sueldo)

print(irpf2(15000))
