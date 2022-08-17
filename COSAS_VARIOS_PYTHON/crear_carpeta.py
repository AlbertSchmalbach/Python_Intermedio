import os

nombre_carpeta = input("Nombre de la carpeta: ")
directorio_actual = os.getcwd()
path = os.path.join(directorio_actual, nombre_carpeta)

if os.path.exists(path):
    print('La Carpeta ya existe')
else:
  os.mkdir(path)  
  print("Succesfull...")



