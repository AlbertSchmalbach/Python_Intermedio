""" Definir una función superposicion() que tome dos listas y devuelva True si tienen al menos 1 miembro en común o devuelva False de lo contrario. Escribir la función usando el bucle for anidado. """

def superposicion(list1, list2):
    elemt_comun = []
    for i in list1:
        for j in list2:
            if i == j:
                elemt_comun.append(i)
                #return True
            
    print(elemt_comun)
            


def main():
    lista1 = ['x', 'y', 'a', 'z', 'u']
    lista2 = ['t', 'a', 'm', 'n', 'x']
    
    print(superposicion(lista1, lista2))

if __name__=='__main__':
    main()