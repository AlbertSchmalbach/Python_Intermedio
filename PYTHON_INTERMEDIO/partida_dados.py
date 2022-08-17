from random import random
import random


obj = random.randint(2,12)

partida = 1

print('objetivo: ', obj)
print()

while True:
    jug = input('Nombre de jugador: ').upper()
    suma = 0
    for i in range(2):
        dado = random.randint(1,6)
        suma+=dado

    if jug == 'EXIT':
        break
    
    print(f'Suma de dados jugador {jug}: ', suma)

    if suma== obj:
        print()
        print(f'!EXCELENTE {jug} GANASTE...')
        break
    else:
        print(f'!PERDISTE {jug}')
    print()
        
    partida+=1

    print('Numero de partida en juego: ',partida)

print('Total partidas: ', partida)





        

    

