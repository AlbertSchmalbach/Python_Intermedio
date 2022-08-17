mi_lista = ['Ibias', 'Pesoz', 'Tineo', 'Boal']
for c, valor in enumerate(mi_lista, 1):
    print(c, valor)

# Salida:
# 1 Ibias
# 2 Pesoz
# 3 Tinero
# 4 Boal

lista_contador = list(enumerate(mi_lista, 1))
print(lista_contador)