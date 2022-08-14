

class Cafeteria:

    def __init__(self):

        self.nombre = "Cafe-negro"
        self.ubicacion = "La serena"
        self.horario = 700
        self.variedad_cafe = {
        "americano" :{"id": 1, "ingredientes" : ["cafe", "agua", "azucar"], "precio" : {"chico": 1500, "grande": 2000}},
        "capuccino" : {"id" : 2, "ingredientes" : ["leche", "cafe cafe expresso", "cacao en polvo", "canela"], "precio" : {"chico": 1800, "grande": 2100}},
        "cafe vienes" : {"id" : 3, "ingredientes" : ["cafe expreso", "azucar", "nata montada", "cacao en polvo"], "precio" : {"chico": 1700, "grande": 2200}},
        "cafe arabe" : {"id" : 4, "ingredientes" : ["agua", "cardamomo", "cafe negro", "azafran"], "precio" : {"chico": 1400, "grande": 2050} },
        "cafe irlandes" : {"id" : 5, "ingredientes" : ["whiskey", "cafe", "crema de leche", "nata montada", "canela", "azucar"], "precio" : {"chico": 1900, "grande": 2500}},
        }

        self.total_venta = 0
        self.productos_comprados= {}

    def mostrar_productos(self):
        print("MENU:\n----------------")
        for k in self.variedad_cafe.keys():
            print(f"-{k.title()}-")

            for precio in self.variedad_cafe[k]:
                
                if precio == "precio":
                    print(precio, "- Tamaño chico: ", "$",self.variedad_cafe[k]["precio"]["chico"])
                    print(precio, "- Tamaño grande: ", "$", self.variedad_cafe[k]["precio"]["grande"])
                    print("--------------------------------")
                

    def vender_cafe(self, tipo_cafe, tamaño):
        self.total_venta += self.variedad_cafe[tipo_cafe]["precio"][tamaño]

        self.productos_comprados[tipo_cafe] = self.variedad_cafe[tipo_cafe]["precio"][tamaño]
        print(tipo_cafe, " añadido a su carrito!!") 
        return self
    
    def mostrar_carrito_compra(self):
        print("----------------")
        for productos in self.productos_comprados:
            print(f"{productos}: $ {self.productos_comprados[productos]}")
        print(f"\nTotal: $ {self.total_venta}")
        print("-------------------------------")


# karla.mostrar_productos()
# karla.vender_cafe("americano", "chico").vender_cafe("capuccino", "grande").vender_cafe("cafe irlandes", "grande").mostrar_carrito_compra()
