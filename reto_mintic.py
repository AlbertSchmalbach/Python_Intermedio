""" def isInt(data):

    if type(data) == int:

        return True

    elif type(data) == float:

        return False


print(isInt(5))
print(isInt(5.0))
print(isInt('5')) """

""" n = range(4)

for num in n:

    print(num - 1)

else:

    print(num) """

""" def hola():

    return

    print("¡Hola!")

print(hola()) """

""" def evenNumLst(ran):

    lst = []

    for num in range(ran):

        if num % 2 == 0:

            lst.append(num)

    return lst

print(evenNumLst(11)) """

""" a = 1

def fun():

    a = 2

    print(a)

fun()

print(a) """

""" x = "1"



if x == 1:

    print("uno")

elif x == "1":

    if int (x)> 1:

        print("dos")

    elif int (x) < 1:

        print("tres")

    else:

        print("cuatro")

if int (x) == 1:

    print("cinco")

else:

    print("seis")  """

""" lst = [1, 2, 3, 4, 5]

lst.insert(1, 6)

del lst[0]

lst.append(1)

print(lst) """

""" def hola():

    print("hola")

hola(5)
 """

""" def fun(a):

    if a > 30:

        return 3

    else:

        return a + fun(a + 3)

print(fun(25))
 """

""" x = input()
y = int(input())
print(x * y) """

""" a = '1'

b = "1"

print(a + b) """

""" x = 1

y = 0

z = ((x == y) and (x == y)) or not(x == y)   

print(not(z))
print((2**4), (2*4.), (2*4)) """

""" hola()

def hola():

    print("hola!") """

""" def factorial(n):

    return n * factorial(n - 1)

print(factorial(4)) """

def message():

    alt = 1

    print("Hola, mundo!")

print(alt)