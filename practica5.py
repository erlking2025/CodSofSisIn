while True:
	nombre = input("Ingresa tu nombre: ")
	if nombre:
		break
	print("no puedes dejar este campo en blanco, lo siento. ")

while True:
	apellido = input("Ingresa tu apellido: ")
	if apellido:
		break
	print("no puedes dejar este campo en blanco, lo siento. ")

print("Nombre invertido:", nombre[::-1])
print("Apellido invertido:", apellido[::-1])

cyear = 2025

while True:
	edad = int(input("¿Cuántos años tienes? "))
	if edad:
		break
	print("campo en blanco. Inténtalo de nuevo")

año_nac = cyear - edad
año_100 = año_nac + 100

print("Tienes", edad, "años. Eso significa que, como el año actual es", cyear, ", probablemente hayas nacido en el año", año_nac, ". Tendrías 100 años en el año", año_100, ".")
