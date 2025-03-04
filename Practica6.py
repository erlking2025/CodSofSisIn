tupla = (10, "Hola", 3.14)
print(tupla)

tupla = (1,2,3,4,5)
print(tupla[2])  

tupla1 = (1,2,3)
tupla2 = (4,5,6)
tupla_final = tupla1 + tupla2
print(tupla_final)

tupla = ('a','b','c')
var1, var2, var3 = tupla
print(var1, var2, var3)

tupla = (1,3,5,7,9)
existe = 7 in tupla
print(existe)

tupla = (0,1,2,3,4,5)
resultado = tupla[2:5]  
print(resultado)

tupla = (10,20,30,40,50)
length = len(tupla)
print(length)

tupla = (7, 8, 9)
resultado = tupla * 3
print(resultado)

lista = [1,2,3]
tupla = tuple(lista)
print(tupla)

tupla = (5,12,3,8,15)
valor_minimo = min(tupla)
valor_maximo = max(tupla)
print('Minimo:', valor_minimo, 'Maximo:', valor_maximo)
