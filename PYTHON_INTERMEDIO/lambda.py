suma = lambda x, y: x + y

print(suma(3, 5))
# Salida: 8

# Ordenar una lista

a = [(1, 2), (4, 1), (9, 10), (13, -3)]
a.sort(key=lambda x: x[1])

print(a)
# Salida: [(13, -3), (4, 1), (1, 2), (9, 10)]

# Ordenar listas paralelamente

datos = zip(lista1, lista2)
datos.sort()
lista1, lista2 = map(lambda t: list(t), zip(*datos))