
class Mascota:

    def __init__(self, nombre, tipo, truco, ruido):

        self.nombre = nombre
        self.tipo = tipo
        self.truco = truco
        self.ruido = ruido
        self.salud = 50 
        self.energia = 100
    
    def dormir(self):
        self.energia += 25
        print("aaaww Que sueño reparador... haz recuperado 25 de energia")
        return self

    def comer(self):
        self.energia += 5
        self.salud += 10
        print("mmmmm que deliciosa comida +5 de energia y +10 de salud")
        return self

    def jugar(self):
        self.salud += 10
        self.energia -= 2
        print("El ejercicio estimula la salud +10, y -2 gasto de energia")
        return self


    def sonido(self):
        print(self.ruido)
        return self
    
    def niveles(self):
        print("\n*************************")
        print(f"{self.tipo.title()} {self.nombre}")
        print(f"Energia :{self.energia} - Salud : {self.salud}")
        print("*************************\n")