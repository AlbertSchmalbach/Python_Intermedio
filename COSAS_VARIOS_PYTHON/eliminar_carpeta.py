import os

eliminar_carpeta = input("Nombre de la carpeta: ")
directorio_actual = os.getcwd()
path = os.path.join(directorio_actual, eliminar_carpeta)

if os.path.exists(path):
  os.rmdir(path)
  print('La carpeta fue removida!')
else:
  print("La carpeta especificada no existe")