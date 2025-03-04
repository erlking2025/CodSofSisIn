#Conversor de divisas

#calcular en base a un valor dado por el usuario
#su equivalencia en las diferentes divisas definidas

#china
yuan=2.81
#japon
yen=0.14
#Estados Unidos
dolar=20.49
#union europea
euro=21.28
#Reino Unido
libra=25.5

pesos = float(input("Ingresa la cantidad de pesos a convertir: "))

print(f"Los pesos equivalen a:\n"
      f"{pesos / yuan:.2f} yuanes\n"
      f"{pesos / yen:.2f} yenes\n"
      f"{pesos / dolar:.2f} dólares\n"
      f"{pesos / euro:.2f} euros\n"
      f"{pesos / libra:.2f} libras")