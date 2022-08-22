from clases import Mascota

class Ninja:

    def __init__(self, nombre, apellido, mascota, premio, comida_mascota):
        self.nombre = nombre
        self.apellido = apellido
        self.mascota = mascota
        self.premio = premio
        self.comida_mascota = comida_mascota
    
    def caminar(self):
        self.mascota.jugar()
        return self

    def alimentar(self):
        self.mascota.comer()
        return self

    def bañar(self):
        print("\nA bañarse!!!")
        self.mascota.sonido()
        return self
    
    def sleep(self):
        self.mascota.dormir()
        return self