""" FUNCIONES EN PYTHON 

       def nombreFuncion():
            pass
"""

def main():
  #Parametrizadas
  print()
  print('1 - Funcion parametrizada')
  print()
  def names(name, lastname):
      return f'Hola {name} {lastname}, saludos!'

  persona = names('Alberto', 'Schmalbach')
  print(persona)

  #Parametros indeterminados
  print()
  print('2 - Funcion parametros indeterminados (*args)')
  print()

  def fnames(*args):
      for n in args:
          print(n)

  fnames('Said', 'Melany', 'Moises', 'Maria Victoria')
  

  #Argumentos con llave-valor
  print()
  print('3 - Funcion argumentos llave-valor')
  print()

  def my_function(child3, child2, child1):
    print("The youngest child is " + child3)

  my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

  #Parametros por defecto
  print()
  print('4 - Funcion parametros llave-valor por defecto')
  print()
  def nombres(name='Jhon', lastname = 'Doe'):
      return f'Hola {name} {lastname}, saludos!'

  nombre = nombres()
  print(nombre)

  #Funciones Llave-valor indeterminados
  print()
  print('5 - Funcion parametros llave-valor indeterminados (**keyword)')
  print()
  def cargos(**keys):
      for name, cargo in keys.items():
          print(f'Empleado:[Name: {name} - Cargo: {cargo}]')

  cargos(Alberto='Desarrollador', Maria='Asistente', Silvana='Recepcionista', Camila='Asistente2', Juan='Gerente')

  #Funciones recursivas
  print()
  print('2 - Funciones recursivas')
  print()

  def tri_recursion(k):
    if(k > 0):
      result = k + tri_recursion(k - 1)
      print(result)
    else:
      result = 0
    return result

  print("\n\nResultados de ejemplo recursion")
  tri_recursion(6)


if __name__ == '__main__':
    main()