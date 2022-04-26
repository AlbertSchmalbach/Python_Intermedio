from winsound import PlaySound
from modulos import sumar, person1
#import mymodule as mx
import platform


num1 = 8
num2 = 10

resultado = sumar(num1,num2)

print(resultado)

print('Nombre: ', person1['name'])
print('Edad: ', person1['age'])

x = platform.system()

y = dir(platform)

print(x)
print(y)




