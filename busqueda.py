import pandas as pd
#este era un intento de hacer barias prácticas en una.
#se comporta raro al buscar por muchos filtros, pero creo que funciona?

def buscar_resenas():
	df = pd.read_csv("listings.csv")
	df['last_review'] = pd.to_datetime(df['last_review'], errors='coerce')
	df = df.dropna(subset=['last_review'])

	while True:
		df_filtrado = df.copy()

		if input("¿Buscar por nombre? (s/n): ").strip().lower() == 's':
			while True:
				termino = input("Escribe una palabra del nombre: ").strip().lower()
				if termino:
					df_filtrado = df_filtrado[df_filtrado['name'].str.lower().str.contains(termino, na=False)]
					break
				else:
					print("Debes escribir al menos una palabra.")

		if input("¿Filtrar por año? (s/n): ").strip().lower() == 's':
			while True:
				try:
					anio = int(input("Escribe el año (ej: 2024): "))
					df_filtrado = df_filtrado[df_filtrado['last_review'].dt.year == anio]
					break
				except ValueError:
					print("Por favor, escribe un año válido.")

		if input("¿Filtrar por mes? (s/n): ").strip().lower() == 's':
			while True:
				try:
					mes = int(input("Escribe el mes (1 a 12): "))
					if 1 <= mes <= 12:
						df_filtrado = df_filtrado[df_filtrado['last_review'].dt.month == mes]
						break
					else:
						print("El mes debe estar entre 1 y 12.")
				except ValueError:
					print("Por favor, escribe un número válido.")

		if input("¿Filtrar por día? (s/n): ").strip().lower() == 's':
			while True:
				try:
					dia = int(input("Escribe el día (1 a 31): "))
					if 1 <= dia <= 31:
						df_filtrado = df_filtrado[df_filtrado['last_review'].dt.day == dia]
						break
					else:
						print("El día debe estar entre 1 y 31.")
				except ValueError:
					print("Por favor, escribe un número válido.")

		df_filtrado = df_filtrado.sort_values(by='last_review', ascending=False)
		cantidad = df_filtrado.shape[0]

		print(f"\nSe encontraron {cantidad} resultados.\n")

		if cantidad == 0:
			print("No hay resultados con esos filtros.")
		elif cantidad <= 10:
			print(df_filtrado[['id', 'name', 'last_review']])
		else:
			print("Mostrando los primeros 10 resultados:\n")
			print(df_filtrado[['id', 'name', 'last_review']].head(10))
			if input("\n¿Deseas guardar todos los resultados en un archivo de texto? (s/n): ").strip().lower() == 's':
				with open("resultados_filtrados.txt", "w", encoding="utf-8") as f:
					f.write(f"Total de resultados: {cantidad}\n\n")
					for _, fila in df_filtrado[['id', 'name', 'last_review']].iterrows():
						f.write(f"ID: {fila['id']} | Nombre: {fila['name']} | Reseña: {fila['last_review'].date()}\n")
				print("Archivo 'resultados_filtrados.txt' guardado con éxito.")

		if input("\n¿Quieres hacer otra búsqueda? (s/n): ").strip().lower() != 's':
			print("Hasta la próxima.")
			break

buscar_resenas()
