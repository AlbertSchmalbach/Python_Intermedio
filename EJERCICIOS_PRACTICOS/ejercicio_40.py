""" Haz un programa que pida el nombre de una persona y lo muestre en pantalla repetido 1000 veces, pero dejando un espacio de separacion entre aparicion y aparicion del nombre. (Utiliza los operadores de concatenacion y repeticion.) """

name = input('Escribe un nombre: ').capitalize()
name = name + ' '

print(name * 1000)