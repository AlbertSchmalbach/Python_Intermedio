from dominio.Pelicula import Pelicula
from servicio.catalogo_peliculas import CatalogoPeliculas as cp

opcion = None
menu = '''
Opciones: 

    1. Agregar pelicula
    2. Listar peliculas
    3. Eliminar catalogo peliculas
    4. Salir
    '''

while opcion != 4:
    try:
        print(menu)
        opcion = int(input('Escoge una opcion (1 - 4): '))

        if opcion == 1:
            nombre_pelicula = input('Proporciona el nombre de la pelicula: ')
            pelicula = Pelicula(nombre_pelicula)
            cp.agregar_pelicula(pelicula)

        elif opcion == 2:
            cp.listar_peliculas()
            
        elif opcion == 3:
            cp.eliminar_peliculas()
            
        else:
            print('Opcion invalida')

    except Exception as e:
        print(f'Ocurrio un error {e}')
        opcion = None
else:
    print('Salimos del programa...')