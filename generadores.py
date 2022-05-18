# def funcion_generadora():
#     for i in range(10):
#         yield i

# for item in funcion_generadora():
#     print(item)

# def fibon(n):
#     a = b = 1
#     for i in range(n):
#         yield a
#         a, b = b, a + b

# for x in fibon(50):
#     print(x)

# def funcion_generadora():
#     for i in range(3):
#         yield i

# gen = funcion_generadora()
# print(next(gen))
# # Salida: 0
# print(next(gen))
# # Salida: 1
# print(next(gen))
# # Salida: 2
# print(next(gen))

my_string = "Pelayo"
my_iter = iter(my_string)
print(next(my_iter))
# Salida: 'P'