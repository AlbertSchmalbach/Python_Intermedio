# Diseña un programa que solicite por teclado el numero de personas con cada una de las cuatro calificaciones y muestre el resultado en porcentajes de aprobados, suspensos y desaprobados.


p = int(input('Numero de estudiantes: '))

c = 1


aprobados = 0
suspensos = 0
desaprobados = 0

while(c <= p):

    nota = 0

    name = input('Nombre del estudiante: ')
    for n in range(4):
        nota += float(input(f'Ingrese la nota {n+1}: '))
        
    print(nota)
    
    promNota = round((nota / 4),2)

    print(promNota)
    
    if promNota >= 4:
        aprobados+=1
        
    elif promNota >= 3 and promNota < 4:
        suspensos+=1
        
    else:
        desaprobados+=1
        
    c+=1


print(50*'+')
porAprobados = round(aprobados/p * 100)
print('Aprobados: ', aprobados)
print(f'Porcentaje aprobados: {porAprobados}%')
print(50*'+')
porSuspensos = round(suspensos/p * 100)
print('Suspensos: ', suspensos)
print(f'Porcentaje suspensos: {porSuspensos}%')
print(50*'+')
porDesaprobados = round(desaprobados/p * 100)
print('Desaprobados: ', desaprobados)
print(f'Porcentaje desaprobados: {porDesaprobados}%')



