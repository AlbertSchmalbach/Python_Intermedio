import math


MOVIES = [
    {
    'id':1,
    'titulo': 'Los vengadores 4',
    'genero': 'ficcion',
    'taquilla': 250000,
    'año': 2019
    },

    {
    'id':2,
    'titulo': 'Mision imposible 7',
    'genero': 'accion',
    'taquilla': 150000,
    'año': 2019
    },

    {
    'id':3,
    'titulo': 'Spaiderman not way home',
    'genero': 'ficcion',
    'taquilla': 200000,
    'año': 2022
    },

    {
    'id':4,
    'titulo': 'La era del llelo 5',
    'genero': 'animado',
    'taquilla': 200000,
    'año': 2018
    },

    {
    'id':5,
    'titulo': 'Superman 5',
    'genero': 'ficcion',
    'taquilla': 180000,
    'año': 2020
    }
]

# 1 - Filtrar nombres de peliculas de ficcion

movies_ficcion = list(filter(lambda movie : movie['genero']=='ficcion', MOVIES))
movies_ficcion_name = list(map(lambda movie : movie['titulo'], movies_ficcion))
print('PUNTO 1'.center(70,'-'))
for movie in movies_ficcion_name:
    print(movie)

# 2 - Nombre de pelicula mas taquillera y valor de taquilla

movies_taquilla = list(map(lambda movie : movie['taquilla'], MOVIES))
max_taquilla = max(movies_taquilla)
movie_name_taquilla = list(filter(lambda movie : movie['taquilla']== max_taquilla, MOVIES))
movie_name = list(map(lambda movie : movie['titulo'], movie_name_taquilla))
movie_name = "".join(movie_name)

print('PUNTO 2'.center(70,'-'))
print(f'La pelicula mas taquillera: {movie_name} - Taquilla: ${max_taquilla} dolares')

# 3 - La mas reciente
movies_year = list(map(lambda movie : movie['año'], MOVIES))
movie_recent = max(movies_year)

movie_recent_name = [movie['titulo'] for movie in MOVIES if movie['año']== movie_recent]
print('PUNTO 3'.center(70,'-'))
print("".join(movie_recent_name))

# 4 - Total taquilla ficcion
'''Primera forma'''
# print(sum(movies_taquilla))

'''Segunda forma'''
total_taquilla = 0

for valor in movies_taquilla:
    total_taquilla+= valor
print('PUNTO 4'.center(70,'-'))
print("El valor total de la taquilla: $",total_taquilla, " dolares")
