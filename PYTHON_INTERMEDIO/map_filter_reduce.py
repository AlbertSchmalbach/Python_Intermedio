from functools import reduce

# 1 - funcion map()

# lista = [1,2,3,4,5]

# list_cuadrado = list(map(lambda x : x**2, lista))

# print('Lista base: ',lista)
# print('Lista base al cuadrado: ', list_cuadrado)

def multiplicar(x):
    return (x*x)
def sumar(x):
    return (x+x)

funcs = [multiplicar, sumar]
for i in range(5):
    valor = list(map(lambda x: x(i), funcs))
    # print(valor)


# 2 - funcion filter()

lista = range(-5, 5)
#print(lista)
menor_cero = list(filter(lambda x: x < 0, lista))
# print(menor_cero)

# 3 - funcion reduce()

producto = reduce((lambda x, y: x * y), [1, 2, 3, 4])
print(producto)


