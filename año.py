import pandas as pd

df = pd.read_csv("listings.csv")
df['last_review'] = pd.to_datetime(df['last_review'], errors='coerce')

nombres_meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio',
                 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']

while True:
	try:
		cyear = int(input("Ingresa el año que quieres consultar: "))
		break
	except ValueError:
		print("Por favor, escribe un año válido.")

yreviews = df[df['last_review'].dt.year == cyear]

if not yreviews.empty:
	rm = yreviews['last_review'].dt.month.value_counts().sort_index()
	total = rm.sum()

	print(f"\nTotal de reseñas en {cyear}: {total}\n")

	for mes, cantidad in rm.items():
		nombre_mes = nombres_meses[mes - 1]
		print(f"{nombre_mes}: {cantidad}")

	mes_mas_reviews = rm.idxmax()
	cantidad_max = rm.max()
	print(f"\nMes con más reseñas: {nombres_meses[mes_mas_reviews - 1]} ({cantidad_max} reseñas)")
else:
	print(f"No hay reseñas registradas en el año {cyear}.")
