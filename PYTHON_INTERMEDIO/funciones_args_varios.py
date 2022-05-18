def datos(text, *numbers):
  listNum = []
  print(text)
  for n in numbers:
    listNum.append(n)
  print(listNum)

datos('Mi lista de numeros', 3,8,4,7,1)

def misDatos(**kwargs):
  for key, value in kwargs.items():
    print(key,' = ', value)

misDatos(nombre='Albert', edad=39, cargo='programador')

def misDatos2(dato, *args, **kwargs):
  print(dato)
  print(args)
  print(kwargs)

misDatos2('Funcion especial',2,8,5,10,color='blue')