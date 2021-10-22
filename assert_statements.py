from list_and_dicts import clearConsole

def divisors(num):
    divisors=[]
    [divisors.append(i) for i in range(1, num + 1) if num % i == 0]
    return divisors
    
        

def run():
    clearConsole()
    try:
        num = input('Ingrese un numero: ')
        assert num.isnumeric(), 'Debes ingresar un numero'
        print(divisors(int(num)))
        print('Finalizo ejecucion del programa')
    except:
        assert num.isnumeric(), 'El numero no debe ser negativo'

   
if __name__ == '__main__':
    run()