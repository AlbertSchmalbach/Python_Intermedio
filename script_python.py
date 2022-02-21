from email.charset import Charset
from encodings import utf_8
from sys import argv 
from Clear import clearConsole as clear

def main():
    
    clear()
    
    if len(argv)== 4:
        nombre = argv[1]
        edad = int(argv[2])
        year = int(argv[3])
        
        print('NOMBRE: {}\nEDAD: {}\nAÑO: {}'.format(nombre, edad, year))
    else:
        print('Error, datos incorrectos')
        print('Ejemplo: main.py "nombre" 20')


if __name__ == '__main__':
    main()