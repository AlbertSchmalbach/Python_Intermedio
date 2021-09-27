from list_and_dicts import clearConsole, main
import math


clearConsole()


def run():
    """ list_dicts = {i: i**3 for i in range(1,101) if i % 3 != 0}

    print(list_dicts) """

    dist_naturales = {i: (math.sqrt(i)) for i in range(1,1001)}

    print('1000 PRIMEROS NUMEROS NATURALES CON SU RAIZ CUADRADA COMO VALOR: ')
    print()
    print(dist_naturales)

if __name__ == '__main__':
    run()