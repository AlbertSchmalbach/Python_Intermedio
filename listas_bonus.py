from copy import copy


equipos = ['real madrid', 'barcelona', 'psg', 'bayer munich', 'liverpool']

equipos.append('roma')
equipos.sort()
print(equipos.index('psg'))
print(equipos.count('psg'))
equipos.pop()
equipos.remove('psg')
print(len(equipos))
equipos.extend(['Milan', 'Chelsea', 'Napoles'])
equipos.insert(2, 'Manchester United')
equipos.reverse()
equipos2 = copy(equipos)
equipos.clear()
print(equipos)
print('Copia=>', equipos2)