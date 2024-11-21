class Persona:

  def __init__(self, nombre, edad):
    
    self.nombre = nombre
        
    self.edad = edad

  def cumpleaños(self): 
    self.edad += 1

nombre = input("Ingrese el nombre: ")

edad = int(input(" Ingrese su edad: "))

p = Persona(nombre, edad)

p.cumpleaños()

p.cumpleaños()

print(f" {p.nombre} cumple ahora {p.edad} años. ")
