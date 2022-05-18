""" Escribir una función sum() y una función multip() que sumen y multipliquen respectivamente todos los números de una lista. Por ejemplo: sum([1,2,3,4]) debería devolver 10 y multip([1,2,3,4]) debería devolver 24. """

def sum(list):
    s = 0
    for i in list:
        s+=i
    return s

def multip(list):
    m = 1
    for i in list:
        m*=i
    return m

def main():
    numeros1 = [1,2,3,4]
    
    suma = sum(numeros1)
    multiplicacion = multip(numeros1)
    
    print('Resultado suma: ', suma)
    print('Resultado multiplicacion: ', multiplicacion)

if __name__ == '__main__':
    main()