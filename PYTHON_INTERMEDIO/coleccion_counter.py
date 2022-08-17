# El uso de counter nos permite contar el número de elementos que una llave tiene. Por ejemplo, puede ser usado para contar el número de colores favoritos de diferentes personas.

from collections import Counter

colours = (
    ('Covadonga', 'Amarillo'),
    ('Pelayo', 'Azul'),
    ('Xavier', 'Verde'),
    ('Pelayo', 'Negro'),
    ('Covadonga', 'Rojo'),
    ('Amaya', 'Plata'),
)

favs = Counter(name for name, colour in colours)
print(favs)
# Salida: Counter({
#    'Covadonga': 2,
#    'Pelayo': 2,
#    'Xavier': 1,
#    'Amaya': 1
# })