from figuras import Rectangulo, Circulo, probar_figura


def main():
    while True:
        menu = """
        AREA Y PERIMETRO DE FIGURAS GEOMETRICAS
        
        1 - Rectangurlo
        2 - Circulo 
        3 - Salir 
        Ingrese una Opcion: """

        opcion = input(menu)

        if (opcion == '1'):
            base = float(input('Ingrese Base: '))
            altura = float(input('Ingrese Altura: '))
            rec = Rectangulo('Rectangulo', base, altura)
            probar_figura(rec)
        elif (opcion == '2'):
            radio = float(input('Ingrese el radio del circulo: '))
            circ = Circulo('Circulo', radio)
            probar_figura(circ)
        elif (opcion == '3'):
            print('Cerrando sistema...')
            break
        else:
            print('opcion invalida, escoja una de las indicadas en el menu')


if __name__ == '__main__':
    main()
