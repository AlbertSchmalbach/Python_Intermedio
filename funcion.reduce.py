from list_and_dicts import clearConsole
from functools import reduce


clearConsole()

list_num = [1,2,3,4,5]

impares = reduce(lambda a, b: a * b, list_num)

print(impares)