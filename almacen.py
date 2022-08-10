
import time 
import random

productos = {
    "frutas_verduras" : {1: "platano", 2: "manzana", 3: "sandia", 4: "melon", 5:"pera", 6:"frutilla", 7:"naranja"},
    "abarrotes" : {1: "arroz", 2: "azucar", 3: "fideos", 4: "salsa", 5: "porotos enlatados", 6: "cafe", 7: "te", 8: "sal"},
}
mensaje = ["Excelente eleccion!!!", "Buena Compra!!", "Es producto internacional!!", "Es producto Nacional!!", "Acaban de llegar!!"]
bolsa = []
def seleccionar_producto(opcion):

    while True:
        if opcion == 1:
            
            print("\n**************Bienvenido al Almacen donde no hay na'!!************")
            print(f"Contenido de la bolsa: {bolsa}")
            print("1.-Platano\n2.-Manzana\n3.-Sandia\n4.-Melon\n5.-Pera\n6.-Frutilla\n7.-Naranja\n8.-Salir\n")
            a = int(input("Elija frutas/verduras o salir:\n"))
            if a == 8:
                print("saliendo...")
                time.sleep(2)
                break
            
            for fruta in productos["frutas_verduras"].keys():
                if fruta == a:
                    bolsa.append(productos["frutas_verduras"][fruta])
                    a = productos["frutas_verduras"][fruta].title()
            print(f"{a}, {mensaje[random.randint(0, 4)]}1")

        elif opcion == 2:
            print("1.-Arroz\n2.-Azucar\n3.-Fideos\n4.-Salsa\n5.-Porotos enlatados\n6.-Cafe\n7.-Te\n8.-sal")
            print("\n***********Bienvenido al Almacen donde no hay na'!!************")
            print(f"Contenido de la bolsa: {bolsa}")
            a = int(input("\nElija Abarrotes:"))
            if a == 8:
                print("saliendo...")
                time.sleep(2)
                break
            
            for abarrote in productos["frutas_verduras"].keys():
                if abarrote == a:
                    bolsa.append(productos["abarrotes"][abarrote])
        
        elif opcion == 3:
            print("Gracias por su compra!...")
            time.sleep(2)
            return False
            
        else:
            print("ingrese nuevamente una opcion")       
    return bolsa

while True:
    print("----------------------------------------")
    print("****Bienvenido al Almacen donde no hay na'!!*******\n")
    print("Elija una categoria:\n\n 1.-Frutas y verduras\n 2.- Abarrotes\n 3.-Mejor me voy\n")
    productos_seleccionados = seleccionar_producto(int(input("Ingrese opcion:\n")))
    if productos_seleccionados == False:
        break

