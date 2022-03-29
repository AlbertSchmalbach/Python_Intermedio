from Productos import Producto
from Orden import Orden


producto1 = Producto('Camisa', 100000)
producto2 = Producto('Pantalón', 150000)
producto3 = Producto('Zapatos', 230000)
producto4 = Producto('Blusa', 75000)

productos1 = [producto1, producto2]
productos2 = [producto3, producto4]

orden1 = Orden(productos1)
print(orden1)

orden2 = Orden(productos2)
print(orden2)