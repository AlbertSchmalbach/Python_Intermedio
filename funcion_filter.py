from list_and_dicts import clearConsole


clearConsole()

list_num = [1,2,3,4,5,6,7,8,9,10,11,12]

impares = list(filter(lambda x: x % 2 != 0, list_num))

print(impares)