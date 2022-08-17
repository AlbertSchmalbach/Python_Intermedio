from pprint import pprint
import itertools

my_dict = {'name': 'Pelayo', 'age': 'undefined', 'personality': 'collaciu'}
# print(dir(my_dict))

# pprint(dir(my_dict))

# python -c "import csv,json;print(json.dumps(list(csv.reader(open('cars.csv')))))" #(En la CLI)

lista = [[1, 2], [3, 4], [5, 6]]
# print(list(itertools.chain.from_iterable(lista)))
# Salida: [1, 2, 3, 4, 5, 6]

# Otra forma
# print(list(itertools.chain(*lista)))
# Salida: [1, 2, 3, 4, 5, 6]

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print( n, 'igual', x, '*', n/x)
            break
    else:
        # Si no se llama a break, se entra al else
        print(n, 'es un número primo')