import os

# 1 - LEER ARCHIVO

# file = open("demofile.txt") # se omite el valor por defecto("rt").
# file = open("demofile.txt", "rt") genera la misma accion que el anterior.

# leer contenido del archivo
# print(file.read())

# puede especificar cuántos caracteres desea devolver
# print(file.read(5))

# Puede devolver una línea utilizando el metodo readline()
# print(file.readline())

# Al llamar dos veces readline(), puede leer las dos primeras líneas.
# print(file.readline())
# print(file.readline())

# Recorra el archivo línea por línea
# file = open("demofile.txt", "r")
# for x in file:
#   print(x)

# Cerrar el archivo con close()
# file = open("demofile.txt", "r")
# print(file.readline())
# file.close()

# 2 - ESCRIBIR ARCHIVO

# file = open("demofile2.txt", "a")
# file.write("Now the file has more content!")
# file.close()

# #open and read the file after the appending:
# file = open("demofile2.txt", "r")
# print(file.read())

# Abra el archivo "demofile2.txt" y sobrescriba el contenido
# file = open("demofile2.txt", "w")
# file.write("Woops! I have deleted the content!")
# file.close()

# #open and read the file after the appending:
# file = open("demofile2.txt", "r")
# print(file.read())

# 3 - CREAR ARCHIVO

# Cree un archivo llamado "myfile.txt"
# file = open("myfile.txt", "x")

# Cree un nuevo archivo si no existe
# file = open("myfile2.txt", "w")

# 4 - ELIMINAR ARCHIVO

# os.remove("demofile.txt")

# Verifique si el archivo existe, luego elimínelo

if os.path.exists("demofile2.txt"):
  os.remove("demofile2.txt")
  print('El archivo se ha removido!')
else:
  print("The file does not exist")

# Para eliminar una carpeta completa, utilice el método os.rmdir()
os.rmdir("myfolder")