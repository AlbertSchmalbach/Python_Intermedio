from collections import namedtuple

# return

def suma(valor1, valor2):
    return valor1 + valor2

resultado = suma(3, 5)
print(resultado)
# Salida: 8

# global

def suma(valor1, valor2):
    global resultado
    resultado = valor1 + valor2

suma(3,5)
print(resultado)

def perfil():
    nombre = "Pelayo"
    edad = 30
    return (nombre, edad)

datos_perfil = perfil()
print(datos_perfil[0])
# Salida: Pelayo

print(datos_perfil[1])
# Salida: 30

def perfil():
    nombre = "Pelayo"
    edad = 30
    return nombre, edad

nombre_perfil, edad_perfil = perfil()
print(nombre_perfil)
# Salida: Pelayo
print(edad_perfil)
# Salida: 30


def perfil():
    Persona = namedtuple('Persona', 'nombre edad')
    return Persona(nombre="Pelayo", edad=31)

# Usando el namedtuple
p = perfil()
print(p, type(p))
# Persona(nombre='Pelayo', edad=31) <class '__main__.Persona'>
print(p.nombre)
# Pelayo
print(p.edad)
#31

# Otra forma de usar la namedtuple
p = perfil()
print(p[0])
# Pelayo
print(p[1])
#31

# También se puede hacer el unpacking
nombre, edad = perfil()
print(nombre)
# Pelayo
print(edad)
#31