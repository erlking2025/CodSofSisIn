while True:
	nombre = input("¿Cómo te llamas? ").strip()
	if nombre:
		break
	print("No puedes dejar este campo en blanco.")

while True:
	edad = input("¿Qué edad tienes? ").strip()
	if edad:
		break
	print("No puedes dejar este campo en blanco.")

while True:
	profesion = input("¿Qué deseas estudiar? ")
	if profesion:
		break
	print("No puedes dejar este campo en blanco.")

print(f"¡Hola! Me llamo {nombre} y tengo {edad} años. También siempre he querido estudiar {profesion}.")