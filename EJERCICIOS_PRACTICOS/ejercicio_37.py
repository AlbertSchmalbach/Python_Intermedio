""" Diseña un programa que pida el valor de los tres lados de un triangulo y calcule el valor de su area y perimetro.
Recuerda que el area A de un triangulo puede calcularse a partir de sus tres lados, a, b y c, asi: A = √ s(s - a)(s - b)(s - c), donde s = (a + b + c)/2.
(Prueba que tu programa funciona correctamente con este ejemplo: si los lados miden 3, 5 y 7, el perimetro sera 15.0 y
el area 6.49519052838.) """

import math  

a = 3
b = 5
c = 7

s = (a + b + c)/2

sa = s - a
sb = s - b
sc = s - c

#Area del triangulo
A = math.sqrt(s*((sa)*(sb)*(sc)))

#Perimetro del triangulo
P = a + b + c

print('Area del triangulo: ', A)
print('Perimetro del triangulo: ', P)

