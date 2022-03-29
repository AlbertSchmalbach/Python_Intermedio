""" Diseña un algoritmo para calcular el area de un circulo dado su radio. (Recuerda que el ´area de un c´ırculo es π veces
el cuadrado del radio.) """

import math
from random import random


radio = int(input('Ingrese el radio del circulo: '))

area = round((math.pi*(radio**2)),2)

print(f'El area del circulo es: {area}')