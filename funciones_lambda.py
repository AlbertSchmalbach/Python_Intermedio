from list_and_dicts import clearConsole, main



clearConsole()

palindromo = lambda nombre: nombre == nombre[::-1]

name = input('Digite una palabra: ')

name = name.lower()

if palindromo(name) == True:
    print('Soy un palindromo')
else:
    print('No soy un palindromo')

#print(palindromo(name))