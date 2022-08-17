import os

directorio = os.getcwd()

with os.scandir(path=directorio) as ruta:
    for i in ruta:
        if i.is_file():
            print('Es un archivo => ', i.name)
        elif i.is_dir():
            print('Es una carpeta => ', i.name)