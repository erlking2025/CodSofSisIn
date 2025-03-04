por = float(input("escribe el porcentaje del alumno"))

if por > 90:
	grado = "a"
elif por > 80:
	grado = "b"
elif por >= 60:
	grado = "c"
else:
	grado = "d"

print("el grado del alumno es", grado)

bic = float(input("cuál es el precio de la bicicleta? "))

if bic > 100000:
	imp = bic * 0.15
elif bic > 50000:
	imp = bic * 0.10
else:
	imp = bic *0.5

print("La bicicleta cuesta", bic, "y te cobrarán", imp, "de impuestos. Sumando todo, el total que pagarás sería", bic + imp)

a = input("escribe un año")
if a.isdigit():
	a = int(a)

	if (a % 4 == 0 and a % 100 != 0) or (a % 400 == 0):
		print("el año", a, "es bisiesto")
	else:
		print("el año", a, "no es bisiesto")
else:
	print("escribe un número válido")

dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
num = int(input("ingresa un número, 1-7"))
if 1 <= num <= 7:
	print(f"El día correspondiente es: {dias[num - 1]}")
else:
	print("Número fuera de rango. Debes ingresar un número entre 1 y 7.")
