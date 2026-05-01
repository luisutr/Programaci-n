__author__ = 'luisutrilla'

class ClaseEjemplo:
    def __init__(self):
        self.publico = 'variable publica'
        self.__privado = 'variable privada'
    def cambiar_privado(self, cambio):
        self.__privado = cambio
    def obtener_privado(self):
        print self.__privado


otro_ejemplo = ClaseEjemplo()

print otro_ejemplo.publico
# 'variable publica'

otro_ejemplo.publico = "cambio la variable publica"
otro_ejemplo.cambiar_privado("cambio de contenido privado")
print  otro_ejemplo.publico

otro_ejemplo.obtener_privado()
# variable privada