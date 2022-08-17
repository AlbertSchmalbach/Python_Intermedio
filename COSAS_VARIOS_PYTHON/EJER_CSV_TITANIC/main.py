import csv

titanic = []
dic = {}
dic['problema1'] = {}
dic['problema1']['vivos'] = 0
dic['problema1']['muertos'] = 0
dic['problema3'] = {}
dic['problema3']['clases'] = []
dic['problema4'] = {}
dic['problema4']['sexo'] = {'m':0, 'f':0}

with open('titanic.csv') as archivo:
    datos = csv.reader(archivo, delimiter="\t")
    for linea in datos:
        titanic.append(linea)

# print(titanic[0])
titulos = titanic[0]
del(titanic[0])
# print(titanic[0])
for pasajero in titanic:
    if pasajero[1] == "1":
        dic['problema1']['vivos'] += 1
    elif pasajero[1] == "0":
        dic['problema1']['muertos'] += 1
    if pasajero[2] not in dic['problema3']['clases']:
        dic['problema3']['clases'].append(pasajero[2])
    if pasajero[4] == 'male':
        dic['problema4']['sexo']['m'] += 1
    else:
        dic['problema4']['sexo']['f'] += 1


totalPasajeros = dic['problema1']['vivos'] + dic['problema1']['muertos']
totalSobrevivientes = dic['problema1']['vivos']
porc_Sobrevivientes = (totalSobrevivientes/totalPasajeros)*100
clases = dic['problema3']['clases']
masculino = dic['problema4']['sexo']['m']
femenino = dic['problema4']['sexo']['f']

print('PASAJEROS'.center(50, '='))
print()
print('TOTAL: ', totalPasajeros)
print()
print('SOBREVIVIENTES'.center(50, '='))
print()
print('TOTAL: ', totalSobrevivientes)
print()
print('PORCENTAJE SOBREVIVIENTES'.center(50, '='))
print()
print('PORCENTAJE: {:.2f}%'.format(porc_Sobrevivientes))
print()
print('CLASES'.center(50, '='))
print()
print('CANTIDAD: ', len(clases))
print()
print('SEXO'.center(50, '='))
print()
print('CANT HOMBRES: ', masculino)
print('CANT MUJERES: ', femenino)
print()
print('FIN'.center(50, '='))

    