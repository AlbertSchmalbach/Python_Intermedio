# deque proporciona una cola con dos lados, lo que significa que puedes añadir y eliminar elementos de cualquiera de los lados de la cola. Primero debes importar el módulo de la librería de colecciones o collections:

from collections import deque

# d = deque()

# d.append('1')
# d.append('2')
# d.append('3')
# d.popleft()

# print(len(d))
# Salida: 3

# print(d[0])
# Salida: '1'

# print(d[-1])
# Salida: '3'

# También podemos limitar la cantidad de elementos que la cola deque puede almacenar. Al hacer esto, simplemente quitará elementos del otro lado de la cola si el límite es superado. Se ve mejor con un ejemplo como se muestra a continuación:

d = deque([0, 1, 2, 3, 5], maxlen=5)
print(d)
# Salida: deque([0, 1, 2, 3, 5], maxlen=5)

d.extend([6])
print(d)
#Salida: deque([1, 2, 3, 5, 6], maxlen=5)