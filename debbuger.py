from list_and_dicts import clearConsole

def divisors(num):
    divisors=[]
    try:
        if num < 0:
            raise  ValueError('No puede ingresar numeros negativos')
        [divisors.append(i) for i in range(1, num + 1) if num % i == 0]
        return divisors
    except ValueError as ve:
        print(ve)
        return False
        

def run():
    clearConsole()
    try:
        num = int(input('Ingrese un numero: '))
        print(divisors(num))
        print('Finalizo ejecucion del programa')
    except:
        print('Tiene que ingresar un numero')

if __name__ == '__main__':
    run()