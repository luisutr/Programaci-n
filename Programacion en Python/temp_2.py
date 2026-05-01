def CV_a_kW (cv):
    return cv * 0.73539875


from math import sqrt,pi
def traslacion (mp,ms,d):
    return sqrt((4*(pi**2)*(d**3))/(6.674e-11)*(mp+ms))




print(traslacion(76529.00737310888, 100, 1))# 1
print(traslacion(2.2202206833271636e+16, 1000, 200))# 1e8),
print(traslacion(73331475687.81886, 1e5, 1e4))# 1e5


def decimalToBinary(n):
    return bin(n).replace("0b","")

