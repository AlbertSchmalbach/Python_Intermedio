from ManejoRecursos import ManejoRecursos
# with open('archivo.txt', 'r', encoding='utf-8') as archivo:
#     print(archivo.read())

with ManejoRecursos('archivo.txt') as archivo:
    print(archivo.read())
