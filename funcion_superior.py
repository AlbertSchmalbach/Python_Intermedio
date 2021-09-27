from list_and_dicts import clearConsole

def saludo(func):
    func()

def hola():
    print('Hola, como estas?')

def adios():
    print('Adios')

def main():

    clearConsole()

   
    saludo(hola)
    saludo(adios)

if __name__ =='__main__':
    main()