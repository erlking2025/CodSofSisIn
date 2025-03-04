enero = 31
febrero = 28 
marzo = 31
abril = 30 
mayo = 31 
junio = 30 
julio = 31
agosto = 31 
septiembre = 30
octubre = 31
noviembre = 30
diciembre = 31

dia_nac = 13
mes_nac = mayo
año_nac = 2009

dia_hoy = 20
mes_hoy = febrero
año_actual = 2025

dias_vividos = (año_actual - año_nac - 1) * 365  

for año in range(año_nac + 1, año_actual):
    if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
        dias_vividos += 1  

dias_vividos += sum([mes_nac] + [enero, febrero, marzo, abril, mayo, junio, julio, agosto, septiembre, octubre, noviembre, diciembre][(mes_nac):]) - dia_nac  

dias_vividos += sum([enero, febrero, marzo, abril, mayo, junio, julio, agosto, septiembre, octubre, noviembre, diciembre][:mes_hoy - 1]) + dia_hoy  

print(f"Has vivido aproximadamente {dias_vividos} días.")
