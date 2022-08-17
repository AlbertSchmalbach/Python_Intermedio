from ast import NodeTransformer


names = ['Alberto', 'Gissel', 'Nazly', 'Anibal', 'Silvana', 'Paola', 'Ana', 'Sara']

filtro1 = []
for name in names:
    if name[0]== 'S':
        filtro1.append(name)

print(filtro1)

filtro2 = [name for name in names if name[0] == 'A']
print(filtro2)