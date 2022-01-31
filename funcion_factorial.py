def factorial(n):

    if n>1:
        n = n * factorial(n-1)

f = factorial(5)

print(f)