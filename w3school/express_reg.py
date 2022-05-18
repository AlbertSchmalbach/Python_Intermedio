import re
import string

text = 'La casa en el aire'

# La search()función busca una coincidencia en la cadena y devuelve un objeto Match si hay una coincidencia.Si hay más de una coincidencia, solo se devolverá la primera aparición de la coincidencia

#x = re.search('casa*', text)

# La función findall() devuelve una lista que contiene todas las coincidencias
x = re.findall('[a-m]', text)
x = re.findall('[arn]', text)
x = re.findall('[^arn]', text)
x = re.findall('[0123]', text)
x = re.findall('[0-9]', text)
x = re.findall('[0-5][0-9]', text)
x = re.findall('[a-zA-Z]', text)
x = re.findall('[+]', text)

# if x:
#     print('Si se encuentra')
# else:
#     print('No se encuentra')

# print(x)

# La función split() devuelve una lista donde la cadena se ha dividido en cada coincidencia. Puede controlar el número de ocurrencias especificando el maxsplit parámetro.

#x = re.split('\s', text, 2)

# print(x)

# La función sub() reemplaza las coincidencias con el texto de su elección

x = re.sub('\s','-',text)

# print(x)

# El objeto Match tiene propiedades y métodos que se utilizan para recuperar información sobre la búsqueda y el resultado:

# .span() devuelve una tupla que contiene las posiciones inicial y final de la coincidencia.
# .string devuelve la cadena pasada a la función
# .group() devuelve la parte de la cadena donde hubo una coincidencia

# La expresión regular busca cualquier palabra que comience con una "S" mayúscula:
x = re.search(r'\bS\w+', text)
# print(x.span())

# Imprime la cadena pasada a la función:
x = re.search(r'\bS\w+', text)
# print(x.string)

# La expresión regular busca cualquier palabra que comience con una "S" mayúscula:
x = re.search(r'\bS\w+', text)
print(x.group())