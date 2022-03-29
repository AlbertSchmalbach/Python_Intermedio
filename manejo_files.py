from importlib.resources import path
from io import open
from os import path

def manejando_file():
    file = open('texto.txt', 'w', encoding='utf-8')
    file.write('Una generacion va y otra viene, pero la tierra existe para siempre')
    file.close()


def read_files():
    if path.isfile('texto.txt'):
        file = open('texto.txt', 'r')
        #textos = file.read()
        textos = file.readlines()
        file.close()

        print(textos)
    else:
        print('No existe el archivo')

def agregar_datos():
    if path.isfile('texto.txt'):
        file = open('texto.txt', 'a')
        file.write('\nEl mundo esta bajo el control del maligno')
        file.close()

    else:
        print('No existe el archivo')

def modificar_datos():
    if path.isfile('texto.txt'):
        file = open('texto.txt', 'r+')
        texto = file.readlines()
        #print(texto)
        texto[1] = 'De oidas he sabido de ti, pero ahora de veras te veo\n'
        #print(texto)
        file.seek(0)
        file.writelines(texto)
        file.close()
        print(texto)

    else:
        print('No existe el archivo')

def eliminar_datos():
    archivo = open('texto.txt', 'w')
    archivo.close()

#manejando_file()
#agregar_datos()
#modificar_datos()
#read_files()
eliminar_datos()
