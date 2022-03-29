from Clear import clearConsole

def calculo_collatz(n):
    
    print()
    print('Entrada: ', n)
    print()
    
    pasos = 0

    while n > 1:
        c = 0
        if n % 2 == 0:
            c = n//2
        else:
            c = 3*n + 1
        n = c
        pasos+=1   
        print(c)

    print()
    print(15*'*')   
    print('Pasos = ', pasos)
    print(15*'*')
    print()

clearConsole()

userNum = int(input('Ingresa un numero mayor a 1: '))

if userNum > 1:
    calculo_collatz(userNum)
else:
    while userNum <= 1:
        print('El numero ingresado es menor o igual a 1')
        userNum = int(input('Ingresa un numero mayor a 1: '))
        if userNum > 1:
            calculo_collatz(userNum)
        
    

