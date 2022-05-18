# SET
# Creando set

set1 = {'red', 'blue', 'green'}
print(type(set1))
# Salida: <type 'set'>

# EJEMPLO DE DUPLICADOS EN LISTA
lista = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

duplicados = []
for value in lista:
    if lista.count(value) > 1:
        if value not in duplicados:
            duplicados.append(value)

# print(duplicados)
# Salida: ['b', 'n']

# Con sets

duplicados = set([x for x in lista if lista.count(x) > 1])
print(duplicados)

# Intersección
set2 = set(['amarillo', 'rojo', 'azul', 'verde', 'negro'])
set3 = set(['rojo', 'marrón'])
print(set3.intersection(set2))
# Salida: set(['rojo'])

# Diferencia
print(set3.difference(set2))
# Salida: set(['marrón'])