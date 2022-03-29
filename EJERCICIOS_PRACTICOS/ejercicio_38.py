""" El area A de un triangulo se puede calcular a partir del valor de dos de sus lados, a y b, y del angulo θ que estos forman entre si con la formula A = 1/2ab sin(θ). Diseña un programa que pida al usuario el valor de los dos lados (en metros), el angulo que estos forman (en grados), y muestre el valor del area. 

(Ten en cuenta que la funcion sin de Python trabaja en radianes, asi que el angulo que leas en grados deberas pasarlo a radianes sabiendo que π radianes son 180 grados. Prueba que has hecho bien el programa introduciendo los siguientes datos:
a = 1, b = 2, θ = 30; el resultado es 0.5)
"""

import math


a = 1
b = 2
angulo = 30

# Convertir angulo en grado a radianes
radianes = math.radians(30)

# Calculando area del triangulo
A = round((((a*b)/2) * math.sin(radianes)), 2)

print(A)

