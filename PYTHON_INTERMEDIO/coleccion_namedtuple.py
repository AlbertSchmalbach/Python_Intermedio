# Se trata de un tipo que convierte las tuplas en contenedores bastante útiles para tareas simples. Con ellas, no necesitas usar índices enteros para acceder a los miembros de la misma. Puedes pensar en ellas como si fuesen diccionarios, con la salvedad de que son inmutables. Veamos un ejemplo.

from collections import namedtuple

Animal = namedtuple('Animal', 'nombre edad tipo')
perry = Animal(nombre="perry", edad=31, tipo="cat")

print(perry)
# Salida: Animal(nombre='perry', edad=31, tipo='cat')

print(perry.nombre)
# Salida: 'perry'