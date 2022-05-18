try:
    file = open('archivo.txt', 'w', encoding='utf8')
    file.write('PROGRAMAR: Darle instrucciones a un sistema.\n')
    file.write('ALGORITMO: Secuencia de pasos logicos.')
except Exception as e:
    print(e)
finally:
    print('Archivo cerrado')
    file.close()