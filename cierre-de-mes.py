import pandas as pd

df = pd.read_csv("listings.csv")

df['last_review'] = pd.to_datetime(df['last_review'], errors='coerce')

mayo = df[df['last_review'].dt.month == 11]

if not mayo.empty:
	año_mayo_mas_reciente = mayo['last_review'].dt.year.max()
	mayo_reciente = mayo[mayo['last_review'].dt.year == año_mayo_mas_reciente]
	ultima_fecha_mayo = mayo_reciente['last_review'].max()
	anuncios_cierre_mayo = mayo_reciente[mayo_reciente['last_review'] == ultima_fecha_mayo]

	print(f"Cierre de mes más reciente: {ultima_fecha_mayo.date()}")
	print("Anuncios con esa fecha:")
	print(anuncios_cierre_mayo[['id', 'name', 'last_review']])
else:
	print("No hay reseñas registradas en ningún mes de mayo.")
