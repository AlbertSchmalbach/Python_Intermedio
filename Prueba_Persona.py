from os import name
from Persona import *
from Clear import clearConsole

clearConsole()

persona2 = Persona(name,lastname,sex,age, 'Nazly', 'Maria Fernanda', 'Yisel', sueldo=2500000, ubicacion='Magangue')

print('Creacion de objetos'.center(30, '*'))
print()
persona2.mostrarDatos()

print()
print('Eliminacion de objetos'.center(30, '*'))
print()
del persona2