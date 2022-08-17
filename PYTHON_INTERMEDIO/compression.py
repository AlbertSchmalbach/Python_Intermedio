# 1 - list comprehensions

# variable = [out_exp for out_exp in input_list if out_exp == 2]

multiples = [i for i in range(30) if i % 3 == 0]
print(multiples)
# Salida: [0, 3, 6, 9, 12, 15, 18, 21, 24, 27]

squared = [x**2 for x in range(10)]
print(squared)

# 2 - dict comprehensions

d = {i: i*5 for i in range(1,5)}
print(d)

# 3 - set comprehensions

squared = {x**2 for x in [1, 1, 2]}
print(squared)
# Output: {1, 4}

# 3 - generator comprehensions

multiples_gen = (i for i in range(30) if i % 3 == 0)
print(multiples_gen)
# Salida: <generator object <genexpr> at 0x7fdaa8e407d8>
for x in multiples_gen:
  print(x)
  # Salida numbers
