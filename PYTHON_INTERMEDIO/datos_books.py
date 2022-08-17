from libros import BOOKS

books = BOOKS

# 1 - Obtener titulos de libros
# 2 - Obtener libros de autoria de cisco

def main():
    # ACTIVIDAD 1
    libros = list(filter(lambda book : book['id'], books))
    titulos = list(map(lambda book : book['title'], libros))

    print('TITULOS DE LIBROS'.center(50, '='))
    print()
    for title in titulos:
        print(title)
    print()
    print('[]'.center(50, '='))

    # ACTIVIDAD 2
    libros_cisco = list(filter(lambda book : book['author'] == 'Cisco Systems Inc.', libros))
    libros_cisco = list(map(lambda book : book['title'], libros_cisco))
    
    print('LIBROS CISCO'.center(50, '='))
    print()
    for lib_cisco in libros_cisco:
        print(lib_cisco)
    print()
    print('[]'.center(50, '='))


if __name__ == '__main__':
    main()