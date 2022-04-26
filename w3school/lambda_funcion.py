# FUNCION LAMBDA

#Una función lambda puede tomar cualquier cantidad de argumentos, pero solo puede tener una expresión.

# lambda arguments : expression

x = lambda a : a + 10
print(x(5))

x = lambda a, b : a * b
print(x(5, 6))

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytriple = myfunc(3)

print(mydoubler(11))
print(mytriple(11))