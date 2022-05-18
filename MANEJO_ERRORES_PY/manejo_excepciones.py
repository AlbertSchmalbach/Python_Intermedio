from Numeros_Identicos import NumerosIdenticosExcept

resultado = None

try:
    a = int(input('Ingrese el primer numero: '))
    b = int(input('Ingrese el segundo numero: '))

    if a == b:
        raise NumerosIdenticosExcept('Numeros identicos')

    resultado = a / b

except ZeroDivisionError as ZeroError:
    print(f'Error tipo: {ZeroError}, Tipo: {type(ZeroError)}')


except TypeError as TyError:
    print(f'Error tipo: {TyError}, Tipo: {type(TyError)}')

except Exception as e:
    print(f'Error tipo: {e}, Tipo: {type(e)}')

else:
    print('Programa sin alertas de error')

finally:
    print('resultado en curso...')

print(f'El resultado es: {resultado}')
print('Fin...')