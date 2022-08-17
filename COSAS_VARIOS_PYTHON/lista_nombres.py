names = ['Alberto', 'Gissel', 'Nazly', 'Silvana', 'Paola']

file = open('names.txt', 'a', encoding='utf-8')

for n in names:
    nombre = n + '\n'
    file.write(nombre)
    

file.close()