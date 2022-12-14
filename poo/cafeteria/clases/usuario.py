from clases import Cafeteria

class Usuario:

    def __init__(self, nombre):
        self.nombre = nombre
        self.carrito = {
            "carrito" : Cafeteria()
        }

    def ver_productos(self):
        self.carrito["carrito"].mostrar_productos()
        return self

    def ver_carrito(self):
        print("\nCarrito de", self.nombre)
        self.carrito["carrito"].mostrar_carrito_compra()
        return self
    
    def comprar_cafe(self, tipo_cafe, tamaño):
        self.carrito["carrito"].vender_cafe(tipo_cafe, tamaño)
        return self


