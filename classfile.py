class Persona:
	def __init__(self, nombre, comida, edad):
		self.nombre = nombre
		self.comida= comida
		self.edad = edad

	def save(self, archivo):
		with open(archivo, "a") as f:
			f.write(f"Nombre: {self.nombre}\n")
			f.write(f"comida favorita: {self.comida}\n")
			f.write(f"edad: {self.edad}\n\n")

nombre = input("cómo te llamas? ")
comida = input("cuál es tu comida favorita? ")
edad = input("ingresa tu  edad: ")

persona = Persona(nombre, comida, edad)
persona.save("datos.txt")
print("datos guardados en datos.txt")