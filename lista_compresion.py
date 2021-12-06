from typing import Match


import math
nombres = ['Alberto', 'Paola', 'Kiara', 'Marcela', 'Hugo', 'Pedro', 'Paula']

#Lista con los nombres que finalizan con la letra a dentro de la lista nombres
names = [name for name in nombres if name[-1] == 'a']

print(names)

#Raiz cuadrada de los numeros pares del 1 al 100 con dict compression
numeros_raiz = {i:math.sqrt(i) for i in range(1,100) if i % 2 == 0 }

print(numeros_raiz)