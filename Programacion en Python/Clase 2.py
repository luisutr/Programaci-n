def CV_a_kW(cv):
    kw=0.73539875
    if cv == 1:
        return kw
    return cv*kw

#print(CV_a_kW(1))
#print(CV_a_kW(10))
#print(CV_a_kW(100))

from math import sqrt,pi
def traslacion(mp,ms,d):
    traslacion = sqrt((4*(pi**2)*d**3) / (6.67408*10**-11)*(mp+ms))
    return traslacion

#print(traslacion(76529.00737310888, 100, 1))# 1
#print(traslacion(2.2202206833271636e+16, 1000, 200))# 1e8),
#print(traslacion(73331475687.81886, 1e5, 1e4))# 1e5

#Ejercicio 7
from math import pi,sin
def lados_triangulo(alpha,theta,p):
    rho=180-alpha-theta
    a=sin(alpha)
    b=sin(theta)
    c=sin(rho)
    return a,b,c

#print(lados_triangulo(pi/2, pi/6, 100)) #(21.132486540518705,36.60254037844386,42.26497308103742),
#print(lados_triangulo(pi/3, pi/3, 120)) #(40,40,40),
#print(lados_triangulo(pi/2, pi/4, 100)) #(29.289321881345252,29.289321881345252,41.42135623730951),

def sustentacion(p, V, A, C):
    fs=0
    fs = 1/2*(p*(V**2)*A*C)
    return fs

#print(sustentacion(1.29e3, 11.5, 360, 0.298)) #9151118.1),
#print(sustentacion(1.29e2, 5, 60, 0.298)) #28831.5),
#print(sustentacion(1.29e4, 1, 20, 0.298)) #38442.0)


# Descomenta la siguiente línea y la última para ejecutar las pruebas
from unittest import TestCase, main
class Test(TestCase):

    def test_CV_a_kW(self):
        for cv,kw in (
                (1, .73539875),
                (10, 7.3539875),
                (100, 73.539875),
            ):
            self.assertAlmostEqual(CV_a_kW(cv), kw)

    def test_traslacion(self):
        for t, mp, ms, d in (
                (76529.00737310888, 100, 1, 1),
                (2.2202206833271636e+16, 1000, 200, 1e8),
                (73331475687.81886, 1e5, 1e4, 1e5),
            ):
            self.assertAlmostEqual(traslacion(mp,ms,d), t)

    def test_altura_tetraedro(self):
        for r, h in (
                (1, 1.4142135623730951),
                (10, 14.142135623730951),
                (100, 141.42135623730951),
            ):
            self.assertAlmostEqual(altura_tetraedro(r), h)

    def test_momento_inercia_disco(self):
        for M, R, I in (
                (1, 1, 0.5145833333333333),
                (10, 1, 5.145833333333333),
                (1, 10, 51.45833333333333),
            ):
            self.assertAlmostEqual(momento_inercia_disco(M,R), I)

    def test_rosa_polar(self):
        from math import pi
        for n, a, theta, rho in (
                (3, 1, 0, 1),
                (5, 2, 0, 2),
                (7, 3, 0, 3),
                (3, 1, pi/2, -1.8369701987210297e-16),
                (3, 1, pi/3, -1),
                (3, 1, pi/4, -0.7071067811865475),
            ):
            self.assertAlmostEqual(rosa_polar(n, a, theta), rho)

    def test_sustentacion(self):
        for rho, V, A, CL, L in (
                (1.29e3, 11.5, 360, 0.298, 9151118.1),
                (1.29e2, 5, 60, 0.298, 28831.5),
                (1.29e4, 1, 20, 0.298, 38442.0),
            ):
            self.assertAlmostEqual(sustentacion(rho,V,A,CL), L)

    def test_lados_triangulo(self):
        from math import pi
        for a, b, P, L in (
                (pi/2, pi/6, 100, (21.132486540518705,36.60254037844386,42.26497308103742)),
                (pi/3, pi/3, 120, (40,40,40)),
                (pi/2, pi/4, 100, (29.289321881345252,29.289321881345252,41.42135623730951)),
            ):
            self.assertTriangleEqual(lados_triangulo(a,b,P), L)

    def test_deflexion_viga(self):
        for P, EI, L, x, y in (
                (100, 1e4, 1, 0, -0.0033333333333333333),
                (2e5, 1e6, 1, 0, -0.06666666666666666),
                (3e5, 1e7, 1, 0, -0.01),
                (3e5, 1e7, 1, 0.5, -0.003125),
                (3e5, 1e7, 1, 1, 0),
                (3e5, 1e7, 2, 0, -0.08),
            ):
            self.assertAlmostEqual(deflexion_viga(P, EI, L, x), y)

    def test_freq_resonancia(self):
        for L, C, f in (
                (1e-3, 1e-5, 1591.5494309189535),
                (1e-4, 1e-6, 15915.494309189535),
                (2e-3, 2e-5, 795.7747154594767),
            ):
            self.assertAlmostEqual(freq_resonancia(L,C), f)

    def test_i_diodo(self):
        for Is, T, Vd, I in (
                (5e-5, 25, 0.6, -4.999999999639529e-05),
                (4e-5, 28, 0.7, -3.999999999992283e-05),
                (3e-5, 29, 1, -3e-05),
                (2e-5, 25, 1.6, -2e-05),
            ):
            self.assertAlmostEqual(i_diodo(Is, T, Vd), I)

    def assertTriangleEqual(self, a, b):
        for ai,bi in zip(sorted(a),sorted(b)):
            self.assertAlmostEqual(ai,bi)

# Si usas Jupyter descomenta la segunda línea
main() # IDLE, Python, PyCharm
# main(argv=['first-arg-is-ignored'], exit=False) # Jupyter
