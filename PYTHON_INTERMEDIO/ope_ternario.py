# 1 - Forma:

    # condition_if_true if condition else condition_if_false

esBonito = True
estado = 'Es bonita' if esBonito else 'No es bonita'
print(estado)

# 2 - Forma:

# (if_test_is_false, if_test_is_true)[test]
isPretty = False
apariencia = ('feo', 'bonito')[isPretty]
print('El gato es', apariencia)

# 3 - Abreviación ternaria

""" 
>>> True or "Valor"
True
>>>
>>> False or "Valor"
'Valor' 
"""
salida = None
msg = salida or "No se devolvió nada"
print(msg)

def mi_funcion(nombre_real, nombre_opcional=None):
    nombre = nombre_opcional or nombre_real
    print(nombre)

mi_funcion('Nazly')
mi_funcion('Alberto', 'Beto')
