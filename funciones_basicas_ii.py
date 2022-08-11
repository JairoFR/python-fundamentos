#Practicas con funciones basicas en python

print("1.- Cuena regresiva")

def cuenta_regresiva(numero):
    lista = []
    for numero in range(5, -1, -1):
        lista.append(numero)
    return lista
list = cuenta_regresiva(5)
print(list)

print("----------------------------------------------------")
print("2.- Imprimir y devolver: crea una función que reciba una lista con dos números. Imprime el primer valor y devuelve el segundo.")

def imprime_devuelve(lista):
    print(lista[0])
    return lista[1]


print(imprime_devuelve([1, 2]))

print("----------------------------------------------------")
print("3.-Primero más longitud: crea una función que acepte una lista y devuelva la suma del primer valor de la lista, más la longitud de la lista.")

def primero_mas_longitud(list):
    return list[0] + len(list)

print(primero_mas_longitud([1,2,3,4,5]))


print("----------------------------------------------------")
print("Valores mayores que el segundo")
#crear una nueva lista con los valores mayores que el segundo valor de la lista dada como argumento en la funcion
# e imprimir el largo de la nueva funcion, devolver falso si la lista dada es es menor a 2

def mayores_queSegundo(list):

    if (len(list) < 2):
        False

    new_list = []
    for num in range(0, len(list)):
        if (list[num] > list[1]):
            new_list.append(list[num])

    print(len(new_list))
    return new_list

print(mayores_queSegundo([5,2,3,2,1,4]))

print("----------------------------------------------------")
#aceptar dos enteros y y devolver una lista donde el num1 repite la cantidad de veces del num2
print("length_and_value")

def length_and_value(num1, num2):
   lista = []   
   for i in range(0, num1):
        lista.append(num2)
   return lista

print(length_and_value(4, 7))