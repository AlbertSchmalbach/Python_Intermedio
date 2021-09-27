from list_and_dicts import clearConsole, main



clearConsole()

palindromo = lambda nombre: nombre == nombre[::-1]

name = input('Digite una palabra: ')

name = name.lower()

print(palindromo(name))