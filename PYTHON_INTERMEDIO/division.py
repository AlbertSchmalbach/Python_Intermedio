def div():
    num1 = int(input('Ingresa un numero: '))
    num2 = int(input('Ingresa un segundo numero: '))

    assert num2 > 0, 'Debes ingresar un numero mayor a cero'

    result = num1 / num2

    return result


print(div())