from Clear import clearConsole
from functools import reduce
from math import sqrt

clearConsole()

#Funcion lambda o anonima en pyhton
#mayoriaEdad = lambda edad: 'Es mayor de edad' if edad > 17 else 'Es menor de edad'

#print(mayoriaEdad(25))

#funcion filter

nombres = ['Alberto', 'Sofia', 'Mariana', 'Angelica','Paola', 'Yuliana']

#dato = list(filter(lambda nombre : len(nombre)> 5, nombres))

#print(dato)

#funcion map 

#dato_2 = list(map(lambda name :name.count('a') if 'a' in name else 'Null', nombres))

#print(dato_2)

#funcion reduce

numbers = [20,4,80,25]

dato_3 = reduce(lambda n,m: n+ m, numbers)

print(dato_3)
