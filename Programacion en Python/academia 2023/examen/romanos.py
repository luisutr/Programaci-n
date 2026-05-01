def pasaafechanormal(nromano):
    numerosnormales = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    suma = 0
    L = list(nromano)
    for i in range(len(nromano)):
        # Si es el último símbolo o el valor actual es mayor o igual al siguiente, sumar
        if i == len(L) - 1 or numerosnormales[L[i]] >= numerosnormales[L[i + 1]]:
            suma += numerosnormales[L[i]]
        else:  # Si el valor actual es menor que el siguiente, restar
            suma -= numerosnormales[L[i]]

    return suma

print(pasaafechanormal("MCM"))       # 1900
print(pasaafechanormal("MCMXXVII")) # 1927
print(pasaafechanormal("XXI"))      # 21
print(pasaafechanormal("XVI"))      # 16