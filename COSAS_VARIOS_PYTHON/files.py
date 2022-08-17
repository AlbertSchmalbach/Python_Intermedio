from unicodedata import name


f = open('data.txt', 'r', encoding='utf-8')
# 1 - name => propiedad para nombre del archivo contenido
# print(f.name)
# 2 - read => metodo para leer el archivo. Con argumentos para limitar lectura
# print(f.read())
# print(f.read(20))
# 3 - tell => Metodo, valor entero como argumento
# print(f.tell())
# 4 - isatty => Metodo, valor booleano como argumento.
# print(f.isatty())
# 5 - seek => Metodo
# print(f.seek())
# print(f.readline())
# 6 - readlines
print(f.readlines())
