# Las excepciones se pueden manejar usando la declaración try. El bloque try generará una excepción, porque x no está definido:

# try:
#   print(x)
# except:
#   print("An exception occurred")

# Imprima un mensaje si el bloque try genera un NameError y otro para otros errores

# try:
#   print(x)
# except NameError:
#   print("Variable x is not defined")
# except:
#   print("Something else went wrong")

# Puede usar la palabra clave else para definir un bloque de código que se ejecutará si no se generan errores.

# try:
#   print("Hello")
# except:
#   print("Something went wrong")
# else:
#   print("Nothing went wrong")

#  El bloque finally, si se especifica, se ejecutará independientemente de si el bloque try genera un error o no.

# try:
#   print(x)
# except:
#   print("Something went wrong")
# finally:
#   print("The 'try except' is finished")

# try:
#   f = open("demofile.txt")
#   try:
#     f.write("Lorum Ipsum")
#   except:
#     print("Something went wrong when writing to the file")
#   finally:
#     f.close()
# except:
#   print("Something went wrong when opening the file")

# Como desarrollador de Python, puede optar por generar una excepción si se produce una condición. Para lanzar (o generar) una excepción, use la palabra raise clave. La palabra clave raise  se utiliza para generar una excepción. Puede definir qué tipo de error generar y el texto para imprimir al usuario.

# x = -1

# if x < 0:
#   raise Exception("Sorry, no numbers below zero")

x = "hello"

if not type(x) is int:
  raise TypeError("Only integers are allowed")