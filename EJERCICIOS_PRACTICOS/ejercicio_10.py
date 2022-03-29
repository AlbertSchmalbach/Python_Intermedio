""" Diseña un algoritmo que calcule el IVA (16%) de un producto dado su precio de venta sin IVA. """

producto = input('Nombre del producto: ')
precio = float(input('Precio: $'))

iva = (precio * 16)/100

precioIVA = precio + iva 

print('*' * 100)
print(f'El precio del producto => {producto} con IVA del 16% es: ${precioIVA}')
print('*' * 100)