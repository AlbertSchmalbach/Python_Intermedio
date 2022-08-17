from functools import wraps

# TOD_O ES UN OBJETO EN PYTHON

def hola(nombre="Albert"):
    return "Hola " + nombre

# print(hola())
# Salida: 'Hola Albert'

# Podemos asignar una función a una variable
# saluda = hola
# No usamos () porque no la estamos llamando, sino que la estamos
# asignado a una variable

# print(saluda())
# Salida: 'Hola Albert'

# También podemos eliminar la función asignada a la variable con del
# del hola
# print(hola())
#Salida: NameError

# print(saluda())
#Salida: 'Hola Albert'

# DEFINIR FUNCIONES DENTRO DE FUNCIONES:

def hola(nombre="Albert"):
    print("Estás dentro de la función hola()")

    def saluda():
        return "Estás dentro de la función saluda()"

    def bienvenida():
        return "Estás dentro de la función bienvenida()"

    print(saluda())
    print(bienvenida())
    print("De vuelta a la función hola()")

# hola()
#Salida:Estas dentro de la función hola()
#       Estás dentro de la función saluda()
#       Estás dentro de la función bienvenida()
#       De vuelta a la función hola()

# Esto muestra como cada vez que llamas a la función hola()
# se llama en realidad también a saluda() y bienvenida()
# Sin embargo estas dos últimas funciones no están accesibles
# fuera de hola(). Si lo intentamos, tendremos un error.

# saluda()
#Saluda: NameError: name 'saluda' is not defined

# DEVOLVIENDO FUNCIONES DESDE FUNCIONES:

def hola(nombre="Albert"):
    def saluda():
        return "Estás dentro de la función saluda()"

    def bienvenida():
        return "Estás dentro de la función bienvenida()"

    if nombre == "Albert":
        return saluda
    else:
        return bienvenida

a = hola()
# print(a)
#Salida: <function saluda at 0x7f2143c01500>

#Es decir, la variable 'a' ahora apunta a la función
# saluda() declarada dentro de hola(). Por lo tanto podemos llamarla.

# print(a())
#Salida: Estás dentro de la función saluda()

# USANDO FUNCIONES COMO ARGUMENTOS DE OTRAS:

def hola():
    return "¡Hola!"

def hazEstoAntesDeHola(func):
    print("Hacer algo antes de llamar a func")
    print(func())

# hazEstoAntesDeHola(hola)
#Salida: Hacer algo antes de llamar a func
#        ¡Hola!

# TU PRIMER DECORADOR:

def nuevo_decorador(a_func):
    @wraps(a_func)
    def envuelveLaFuncion():
        print("Haciendo algo antes de llamar a a_func()")
        a_func()
        print("Haciendo algo después de llamar a a_func()")
    return envuelveLaFuncion

# def funcion_a_decorar():
    # print("Soy la función que necesita ser decorada")

# funcion_a_decorar()
#Salida: "Soy la función que necesita ser decorada"

# funcion_a_decorar = nuevo_decorador(funcion_a_decorar)
#Ahora funcion_a_decorar está envuelta con el decorador que hemos creado

# funcion_a_decorar()
#Salida: Haciendo algo antes de llamar a a_func()
#        Soy la función que necesita ser decorada
#        Haciendo algo después de llamar a a_func()

@nuevo_decorador
def funcion_a_decorar():
    print("Soy la función que necesita ser decorada")

# funcion_a_decorar()
#Salida: Haciendo algo antes de llamar a a_func()
#        Soy la función que necesita ser decorada
#        Haciendo algo después de llamar a a_func()

#El uso de @nuevo_decorador es simplemente una forma acortada
#de hacer lo siguiente.
# funcion_a_decorar = nuevo_decorador(funcion_a_decorar)

# print(funcion_a_decorar.__name__)
# Output: envuelveLaFuncion


from functools import wraps
def nombre_decorador(f):
    @wraps(f)
    def decorada(*args, **kwargs):
        if not can_run:
            return "La función no se ejecutará"
        return f(*args, **kwargs)
    return decorada

@nombre_decorador
def func():
    return("La función se esta ejecutando")

can_run = True
print(func())
# Salida: La función se esta ejecutando

can_run = False
print(func())
# Salida: La función no se ejecutará