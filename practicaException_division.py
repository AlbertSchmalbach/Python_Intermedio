from list_and_dicts import clearConsole

def div(num):
    result = num/2
    return result


def run():
    clearConsole()
    #Forma clasica de manejar excepciones
    """ try:
        numero = int(input('Ingresa un numero: '))
        print(div(numero))
    except ValueError:
        print('No puede ingresar un string')
 """
    #Otra Forma  de manejar excepciones
    numero = input('Ingresa un numero: ')
    assert numero.isnumeric(), 'No puede ingresar un string'
    print(div(int(numero)))

if __name__== '__main__':
    run()