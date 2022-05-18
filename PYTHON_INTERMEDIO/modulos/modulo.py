from math import sin, pi
# from module import nombre as alias
# from module import n as a, m as b, o as c

print(sin(pi/2))

pi = 3.14

def sin(x):
    if 2 * x == pi:
        return 0.99999999
    else:
        return None

print(sin(pi/2))