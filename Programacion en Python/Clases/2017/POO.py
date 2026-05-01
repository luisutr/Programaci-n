class clase():
    def __init__(self, alumnos, mesas):
        self.alumnos = alumnos
        self.mesas = mesas
        print('Se ha creado una clase, con '+str(alumnos)+' alumnos y '+str(mesas))

    def matriculacion(self, numero):
        self.alumnos += numero
        print('Se han matriculado:'+str(numero)+'.')
        print('Ahora hay '+str(self.alumnos)+' alumnos.')

    def comprarmesas(self, numero):
        self.mesas += numero
        print('Ahora hay '+str(self.mesas)+' mesas.')

    def mesasclase(self):
        if self.mesas <= self.alumnos:
            print('No hay mesas disponibles')
            decision = input("Quieres comprar las mesas?(si/no):")
            if decision == "si":
                self.comprarmesas(self.alumnos-self.mesas)
        else:
            print('Genial, hay mesas suficientes')

aula = clase(10,10)
aula.matriculacion(5)
aula.mesasclase()