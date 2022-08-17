foo = ['hola']
print(foo)
# Salida: ['hola']

bar = foo
bar += ['adios']

print(foo)
# Salida esperada: ['hola']
# Salida: ['hola', 'adios']

print(bar)
# Salida: ['hola', 'adios']

def agrega(num, target=[]):
    target.append(num)
    return target

agrega(1)
# Salida: [1]

agrega(2)
# Salida: [1, 2]

agrega(3)
# Salida: [1, 2, 3]

def agrega(element, target=None):
    if target is None:
        target = []
    target.append(element)
    return target

print(agrega(18))
# Salida: [42]

print(agrega(24))
# Salida: [42]

print(agrega(42))
# Salida: [42]