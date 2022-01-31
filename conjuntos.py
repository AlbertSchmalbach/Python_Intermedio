from Clear import clearConsole

def run():
    clearConsole()

    #Union de 2 o mas cojuntos
    a = {1, 2, 3, 4}
    b = {2, 4, 6, 8}
    print('Union: ', a | b)

    #Intersección de conjuntos en Python
    a = {1, 2, 3, 4}
    b = {2, 4, 6, 8}
    print('Intersección: ',a & b)

    #Diferencia de conjuntos en Python
    a = {1, 2, 3, 4}
    b = {2, 4, 6, 8}
    print('Diferencia: ',a - b)

    #Diferencia simétrica de conjuntos en Python
    a = {1, 2, 3, 4}
    b = {2, 4, 6, 8}
    print('Diferencia simetrica: ',a ^ b)

    #Inclusión de conjuntos en Python
    a = {1, 2, 3, 4}
    b = {2, 4, 6, 8}
    print('Inclucion: ', a>=b)

    #Conjuntos disjuntos en Python
    a = {1, 2}
    b = {1, 2, 3, 4}
    print('Disjuntos: ',a.isdisjoint(b))

    #Igualdad de conjuntos en Python
    a = {1, 2, 3, 4}
    b = {2, 4, 6, 8}
    print('id(a): ',id(a))
    print('id(b): ',id(b))
    print('Igualdad: ',a==b)
    print('Descartar: ',a.discard(3))
    
    #EJERCICIO PRACTICO

    """ caracteres = {'@', '.', 'gmail', 'outlook', 'hotmail', 'yahoo'}

    correo = input('Correo: ')
    correo = set(correo)

    if correo & caracteres:
        print('Correo valido')
    else:
        print('Correo invalido')
 """
if __name__ == '__main__':
    run()
