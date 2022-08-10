import random

print("Adivina el numero!\n")

a = ["Entre tongoy y los vilos!", "Si vas asi no terminaras nunca!", "uuuff  casi!!!", "muy cerca!", "Dedicate a otra cosa!!"]

numero = random.randint(1, 10)

while True:
    resp = int(input("Ingresa un numero: "))
    if resp == numero:
        break
    print(f"{a[random.randint(0, 4)]}\n")
print("Genio Numero adivinado!!")


print("----------------------------------")

print("Quieres saber tu futuro y lo que te repara el destino? Hazme una pregunta")

respuestas = ["Si, definitivamente", "Esto ya esta decido", "No hay ninguna duda que sera asi, calma", 
"No puedo ver la respuesta, haz otra pregunta", "Pregunta de nuevo mas tarde", "Mejor no decirte ahora", "Mis espiritus dicen que no", 
"Muy dudoso, las espectativas no son muy buenas"]

cont = 0
while True:
    if cont == 3:
        print("No puedo responder mas preguntas, se acabo la sesion :)")
        break
    pregunta = input("Que deseas saber? ")
    print(f"{respuestas[random.randint(0, 7)]}\n")
    cont += 1
    