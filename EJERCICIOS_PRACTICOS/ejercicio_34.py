""" Diseña un programa que pida el valor del lado de un cuadrado y muestre el valor de su perimetro y el de su area.
(Prueba que tu programa funciona correctamente con este ejemplo: si el lado vale 1.1, el perimetro sera 4.4, y el area
1.21.) """

lado = 1.1

area_cuadrado = round((lado * lado), 2)
perimetro_cuadrado = lado * 4

print('El perimetro del cuadrado es: ', perimetro_cuadrado)
print('El area del cuadrado es: ', area_cuadrado)