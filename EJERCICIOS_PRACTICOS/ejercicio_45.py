# Diseña un programa que solicite el radio de una circunferencia y muestre su area y perimetro con solo 2 decimales.

import math
from random import random


radio = int(input('Ingrese el radio del circulo: '))

print()

area = round((math.pi*(radio**2)),2)

perimetro = round((2 * math.pi * radio),2)

print(f'El area del circulo es: {area}')
print()
print(f'El perimetro del circulo es: {perimetro}')


