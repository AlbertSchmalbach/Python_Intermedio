file = open('archivo.txt', 'r', encoding='utf8')

# Leer todo el contenido
# print(file.read())

# Leer parte del contenido
# print(file.read(9))

# Leer primera linea del contenido
# print(file.readline())

# Iterar todo el contenido
# for linea in file:
#     print(linea)

# Lista de contenido
# print(file.readlines())

# Esctraer parte de la lista de contenido.
# print(file.readlines()[1])

# CREAR COPIA DE ARCHIVO

file2 = open('texto_copia.txt', 'a', encoding='utf8')
# Copiando archivo
file2.write(file.read())
file.close()
file2.close()

