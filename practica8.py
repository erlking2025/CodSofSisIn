ciudades = {
	"delhi": "red fort",
	"parís": "torre eifel",
	"nueva york": "estatua de la libertad",
	"rio de janeiro": "cristo redentor"
}

ciudad = input("Introduce el nombre de una ciudad: ").lower()

if ciudad in ciudades:
	print("El monumento más famoso de", ciudad.capitalize(), "es:", ciudades[ciudad].capitalize())
else:
	print("no hay datos sobre esa ciudad que escribiste. lo siento")

edad = int(input("ingresa tu edad"))
if edad < 18:
	print("no puedes votar")
if edad >= 18:
	print(" puedes votar")

numeros = []
for i in range(2):
	numeros.append(float(input(f"Ingresa el número {i+1}: ")))

nmin = min(numeros)
print("el número menor es", nmin,)

edades = []
for i in range(4):
	edades.append(int(input(f"Escribe el valor {i+1}: ")))

ned = min(edades)
print("la persona con menor edad tiene", ned, "años")

palabra = input("Ingresa una palabra: ")

for letra in palabra:
    if letra.isupper():
        print(f"'{letra}' es mayúscula.")
    elif letra.islower():
        print(f"'{letra}' es minúscula.")
    else:
        print(f"'{letra}' no es una letra.")