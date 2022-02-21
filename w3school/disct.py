autos = {
    'marca': 'Ford',
    'modelo': 'fiesta',
    'year': 2022
}

print(autos['marca'])

autos['year'] = 2020
autos.update({'year':2021})
autos.update({'garantia': '3 años'})

#autos.pop('year')
#autos.popitem()
del autos['modelo']
autos.clear()

print(autos.get('modelo'))

llaves = autos.keys()
print(llaves)

valor = autos.values()
print(valor)

items = autos.items()
print(items)

if 'modelo' in autos:
    print('Si, se encuentra')
    
    