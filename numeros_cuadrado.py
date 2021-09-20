from list_and_dicts import clearConsole

def main():

    clearConsole()

    num_cuadrado = []
    cant = int(input('digita una cantidad: '))

    """ for i in range(cant):
        num = pow(i,2)
        num_cuadrado.append(num) """

    #[element for element in iterable if condition]
    
    [num_cuadrado.append(i**2) for i in range(cant)]

    print(num_cuadrado)
    

if __name__ == '__main__':
    main()